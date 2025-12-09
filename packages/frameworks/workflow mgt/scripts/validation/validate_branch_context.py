#!/usr/bin/env python3
"""
Branch Context Validator

This script validates that:
1. Current branch matches the work being done
2. Version number matches branch schema
3. CHANGELOG entries match the branch
4. No cross-epic contamination

Run this BEFORE every commit to prevent branch mix-ups.

Usage:
    python scripts/validation/validate_branch_context.py [--strict]

    --strict: Exit with error code if validation fails (for pre-commit hooks)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Dict

try:
    import yaml
except ImportError:
    yaml = None

def load_rw_config(project_root: Path = None) -> Optional[Dict]:
    """Load rw-config.yaml if it exists."""
    if project_root is None:
        project_root = Path.cwd()
    
    config_path = project_root / "rw-config.yaml"
    if not config_path.exists() or yaml is None:
        return None
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def get_version_file_path(config: Optional[Dict] = None) -> Path:
    """Get version file path from config or use default."""
    if config and 'version_file' in config:
        return Path(config['version_file'])
    # Default fallback
    return Path("src/fynd_deals/version.py")


def get_current_branch():
    """Get current git branch."""
    result = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def get_version(config: Optional[Dict] = None):
    """Get version from version.py."""
    version_file = get_version_file_path(config)
    if not version_file.exists():
        return None
    # Try to import and get the actual version value
    try:
        import sys
        import importlib.util
        spec = importlib.util.spec_from_file_location("version", version_file)
        version_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(version_module)
        return version_module.VERSION_STRING
    except (ImportError, AttributeError, Exception):
        # Fallback: Parse from file content
        content = version_file.read_text()
        # Match VERSION_STRING = f"0.9.21.17" or "0.9.21.3+1" or __version__ = "..."
        # Handle both f-strings and regular strings
        match = re.search(r'(?:VERSION_STRING|__version__)\s*=\s*(?:f?"|")([^"]+)', content)
        if match:
            version_str = match.group(1)
            # If it's an f-string template, try to evaluate it
            if '{' in version_str and '}' in version_str:
                # It's an f-string, we need to evaluate it
                # Extract the components and build the version
                rc_match = re.search(r'VERSION_RC\s*=\s*(\d+)', content)
                epic_match = re.search(r'VERSION_EPIC\s*=\s*(\d+)', content)
                story_match = re.search(r'VERSION_STORY\s*=\s*(\d+)', content)
                task_match = re.search(r'VERSION_TASK\s*=\s*(\d+)', content)
                build_match = re.search(r'VERSION_BUILD\s*=\s*(\d+)', content)
                if all([rc_match, epic_match, story_match, task_match, build_match]):
                    return f"{rc_match.group(1)}.{epic_match.group(1)}.{story_match.group(1)}.{task_match.group(1)}+{build_match.group(1)}"
            return version_str
        return None


def parse_branch_epic(branch: str) -> Optional[int]:
    """Extract epic number from branch name (e.g., epic/10-fastapi-migration -> 10)."""
    # Match patterns like: epic/10, epic/10-fastapi-migration, epic/11-architecture-refactoring
    match = re.match(r"^epic/(\d+)", branch)
    if match:
        return int(match.group(1))
    return None


def is_maintenance_branch(branch: str) -> bool:
    """
    Detect maintenance/update branches that should skip epic/version validation.

    Examples:
    - update/ai-dev-kit
    - maintenance/workflow-mgt
    - upgrade/deps
    """
    return re.match(r"^(update|maintenance|upgrade)/", branch) is not None


def parse_version_epic(version: str) -> Optional[int]:
    """Extract epic number from version string (RC.EPIC.STORY.PATCH or RC.EPIC.STORY.TASK+BUILD)."""
    # Format: RC.EPIC.STORY.PATCH (old) or RC.EPIC.STORY.TASK+BUILD (new)
    # Try new format first
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)\+(\d+)$", version)
    if match:
        return int(match.group(2))  # EPIC is the second component
    # Try old format
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", version)
    if match:
        return int(match.group(2))  # EPIC is the second component
    return None


def parse_version_story(version: str) -> Optional[int]:
    """Extract STORY number from version string (RC.EPIC.STORY.PATCH or RC.EPIC.STORY.TASK+BUILD)."""
    # Format: RC.EPIC.STORY.PATCH (old) or RC.EPIC.STORY.TASK+BUILD (new)
    # Try new format first
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)\+(\d+)$", version)
    if match:
        return int(match.group(3))  # STORY is the third component
    # Try old format
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", version)
    if match:
        return int(match.group(3))  # STORY is the third component
    return None


def parse_version_patch(version: str) -> Optional[int]:
    """Extract PATCH number from version string (RC.EPIC.STORY.PATCH)."""
    # Format: RC.EPIC.STORY.PATCH
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", version)
    if match:
        return int(match.group(4))  # PATCH is the fourth component
    return None


def check_changelog(branch, config: Optional[Dict] = None):
    """Check CHANGELOG.md for cross-epic contamination (supports both old and new format)."""
    if config and 'main_changelog' in config:
        changelog_file = Path(config['main_changelog'])
    else:
        changelog_file = Path("CHANGELOG.md")
    
    if not changelog_file.exists():
        return True, []

    issues = []

    # Get expected epic number for this branch
    expected_epic = parse_branch_epic(branch)

    if expected_epic is not None:
        # Check staged changes to CHANGELOG.md
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--unified=0", "--", "CHANGELOG.md"],
                capture_output=True,
                text=True,
                check=False,
            )
            
            # Extract version from staged additions
            for line in result.stdout.splitlines():
                if line.startswith("+## ["):
                    # Match RC.EPIC.STORY.PATCH (old) or RC.EPIC.STORY.TASK+BUILD (new) format
                    match = re.match(r"\+## \[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(?:\+\d+)?)\]", line)
                    if match:
                        staged_version = match.group(1)
                        version_epic = parse_version_epic(staged_version)
                        if version_epic is None:
                            issues.append(
                                f"Staged CHANGELOG entry '{staged_version}' has invalid format "
                                f"(expected RC.EPIC.STORY.PATCH or RC.EPIC.STORY.TASK+BUILD)"
                            )
                        elif version_epic != expected_epic:
                            issues.append(
                                f"Staged CHANGELOG entry '{staged_version}' has Epic {version_epic} "
                                f"but branch '{branch}' expects Epic {expected_epic}"
                            )
        except subprocess.CalledProcessError:
            pass  # No staged changes

    return len(issues) == 0, issues


def validate_branch_context():
    """Main validation function."""
    print("🔍 Validating branch context...")
    print()

    # Load config if available
    config = load_rw_config()

    # Get current branch
    branch = get_current_branch()
    print(f"Current branch: {branch}")

    # Get version
    version = get_version(config)
    print(f"Current version: {version}")

    # Check branch-epic mapping
    maintenance_branch = is_maintenance_branch(branch)
    if branch == "main":
        expected_epic = None  # main branch can have any epic
    elif maintenance_branch:
        expected_epic = None  # maintenance/update branches intentionally skip epic validation
        print("Detected maintenance/update branch pattern; skipping epic/version enforcement.")
    else:
        # Parse epic number from branch name (e.g., epic/10-fastapi-migration -> 10)
        expected_epic = parse_branch_epic(branch)

    errors = []
    warnings = []

    if expected_epic is not None:
        print(f"Expected epic number: {expected_epic}")
        if version:
            version_epic = parse_version_epic(version)
            if version_epic is None:
                errors.append(
                    f"Invalid version format: '{version}' "
                    f"(expected RC.EPIC.STORY.PATCH or RC.EPIC.STORY.TASK+BUILD)"
                )
            elif version_epic != expected_epic:
                errors.append(
                    f"Version mismatch: Branch '{branch}' expects Epic {expected_epic} "
                    f"but version '{version}' has Epic {version_epic}"
                )
    elif branch != "main" and not maintenance_branch:
        warnings.append(f"Branch '{branch}' not in known mapping - cannot validate version")

    # Check CHANGELOG
    changelog_ok, changelog_issues = check_changelog(branch, config)
    if not changelog_ok:
        errors.extend(changelog_issues)

    print()
    if errors:
        print("❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        print()
        print("🚨 DO NOT COMMIT - Fix issues first!")
        return 1

    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
        print()

    print("✅ Branch context validation passed!")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate branch context before commit")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code on validation failure (for pre-commit hooks)",
    )
    args = parser.parse_args()

    exit_code = validate_branch_context()

    # In strict mode, always exit with the validation result
    sys.exit(exit_code)
