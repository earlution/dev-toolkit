#!/usr/bin/env python3
"""
Changelog Format Validator

Validates that CHANGELOG.md follows the required format:
- Version entries follow RC.EPIC.STORY.PATCH format (old) or RC.EPIC.STORY.TASK+BUILD format (new)
- Date format is YYYY-MM-DD (old) or DD-MM-YY (new)
- **Canonical ordering:** Entries must be ordered by version number (RC.EPIC.STORY.TASK+BUILD), not by timestamp

This script is called by pre-commit hooks and CI to enforce changelog standards.

Usage:
    python scripts/validation/validate_changelog_format.py [--strict]
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Tuple, List, Optional, Dict

try:
    import yaml
except ImportError:
    yaml = None

# Version patterns: RC.EPIC.STORY.PATCH (old) or RC.EPIC.STORY.TASK+BUILD (new)
# Support both formats for backward compatibility
OLD_VERSION_PATTERN = re.compile(r"## \[(\d+)\.(\d+)\.(\d+)\.(\d+)\] - (\d{4}-\d{2}-\d{2})")
NEW_VERSION_PATTERN = re.compile(r"## \[(\d+)\.(\d+)\.(\d+)\.(\d+)\+(\d+)\] - (\d{2}-\d{2}-\d{2})")


def parse_version(version_str: str) -> Tuple[int, int, int, int, int]:
    """
    Parse version string (RC.EPIC.STORY.TASK+BUILD) into components.
    
    Returns:
        (RC, EPIC, STORY, TASK, BUILD)
    """
    if '+' in version_str:
        # New format: RC.EPIC.STORY.TASK+BUILD
        parts = version_str.split('+')
        build = int(parts[1])
        main_parts = parts[0].split('.')
        if len(main_parts) == 4:
            return (int(main_parts[0]), int(main_parts[1]), int(main_parts[2]), int(main_parts[3]), build)
    else:
        # Old format: RC.EPIC.STORY.PATCH (treat PATCH as TASK, BUILD=0)
        parts = version_str.split('.')
        if len(parts) == 4:
            return (int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), 0)
    
    raise ValueError(f"Invalid version format: {version_str}")


def compare_versions(v1: Tuple[int, int, int, int, int], v2: Tuple[int, int, int, int, int]) -> int:
    """
    Compare two versions using canonical ordering.
    
    Returns:
        -1 if v1 < v2
        0 if v1 == v2
        1 if v1 > v2
    
    Ordering: RC → EPIC → STORY → TASK → BUILD
    """
    rc1, epic1, story1, task1, build1 = v1
    rc2, epic2, story2, task2, build2 = v2
    
    # Compare RC
    if rc1 < rc2:
        return -1
    if rc1 > rc2:
        return 1
    
    # Compare EPIC
    if epic1 < epic2:
        return -1
    if epic1 > epic2:
        return 1
    
    # Compare STORY
    if story1 < story2:
        return -1
    if story1 > story2:
        return 1
    
    # Compare TASK
    if task1 < task2:
        return -1
    if task1 > task2:
        return 1
    
    # Compare BUILD
    if build1 < build2:
        return -1
    if build1 > build2:
        return 1
    
    return 0


def extract_changelog_versions(content: str) -> List[Tuple[str, Tuple[int, int, int, int, int]]]:
    """
    Extract all version entries from changelog content.
    
    Returns:
        List of (version_string, parsed_components) tuples
    """
    versions = []
    
    # Extract new format versions
    for match in NEW_VERSION_PATTERN.finditer(content):
        rc, epic, story, task, build, date = match.groups()
        version_str = f"{rc}.{epic}.{story}.{task}+{build}"
        try:
            parsed = parse_version(version_str)
            versions.append((version_str, parsed))
        except ValueError:
            pass
    
    # Extract old format versions (grandfathered)
    for match in OLD_VERSION_PATTERN.finditer(content):
        rc, epic, story, patch, date = match.groups()
        version_str = f"{rc}.{epic}.{story}.{patch}"
        try:
            parsed = parse_version(version_str)
            versions.append((version_str, parsed))
        except ValueError:
            pass
    
    return versions


def validate_changelog_ordering(content: str) -> Tuple[bool, List[str]]:
    """
    Validate that changelog entries are in canonical order (by version number).
    
    Returns:
        (is_valid, errors)
    """
    errors = []
    versions = extract_changelog_versions(content)
    
    if len(versions) < 2:
        return True, []  # Need at least 2 versions to check ordering
    
    # Check ordering: each version should be >= previous version
    for i in range(len(versions) - 1):
        current_version_str, current_components = versions[i]
        next_version_str, next_components = versions[i + 1]
        
        comparison = compare_versions(current_components, next_components)
        
        if comparison > 0:
            # Current version is greater than next version - ordering violation
            errors.append(
                f"Changelog ordering violation: {current_version_str} appears before "
                f"{next_version_str}, but canonical ordering requires "
                f"{next_version_str} before {current_version_str} "
                f"(RC.EPIC.STORY.TASK+BUILD comparison: {current_components} > {next_components})"
            )
        elif comparison == 0:
            # Duplicate version - also an error
            errors.append(
                f"Duplicate version detected: {current_version_str} appears multiple times"
            )
    
    return len(errors) == 0, errors


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


def get_changelog_path(config: Optional[Dict] = None) -> Path:
    """Get changelog file path from config or use default."""
    if config and 'main_changelog' in config:
        return Path(config['main_changelog'])
    return Path("CHANGELOG.md")


def validate_changelog_file(filepath: Path) -> Tuple[bool, List[str], List[str]]:
    """
    Validate CHANGELOG.md format and canonical ordering.

    Returns:
        (is_valid, errors, warnings)
    """
    if not filepath.exists():
        return False, [f"File does not exist: {filepath}"], []

    content = filepath.read_text()
    errors = []
    warnings = []
    
    # Validate canonical ordering (CRITICAL)
    ordering_valid, ordering_errors = validate_changelog_ordering(content)
    if not ordering_valid:
        errors.extend(ordering_errors)

    # Check for version entries (both old and new format)
    old_matches = OLD_VERSION_PATTERN.findall(content)
    new_matches = NEW_VERSION_PATTERN.findall(content)
    
    if not old_matches and not new_matches:
        # Check if there are any version entries at all
        if re.search(r"## \[", content):
            errors.append("CHANGELOG contains version entries but format is invalid")
        # If no entries, that's okay (might be a new project)
        return len(errors) == 0, errors, warnings

    # Validate old format entries (grandfathered)
    for match in old_matches:
        rc, epic, story, patch, date = match
        version_str = f"{rc}.{epic}.{story}.{patch}"
        
        # Validate date format
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            errors.append(
                f"Invalid date format for version {version_str}: '{date}' "
                f"(expected YYYY-MM-DD)"
            )
        else:
            # Old format is grandfathered, but warn about migration
            warnings.append(
                f"Version {version_str} uses old format (RC.EPIC.STORY.PATCH). "
                f"Consider migrating to RC.EPIC.STORY.TASK+BUILD format."
            )

    # Validate new format entries (strict enforcement)
    for match in new_matches:
        rc, epic, story, task, build, date = match
        version_str = f"{rc}.{epic}.{story}.{task}+{build}"
        
        # Validate date format (DD-MM-YY for new format)
        if not re.match(r"\d{2}-\d{2}-\d{2}", date):
            errors.append(
                f"Invalid date format for version {version_str}: '{date}' "
                f"(expected DD-MM-YY for new format)"
            )
        
        # Validate build number >= 1
        if int(build) < 1:
            errors.append(
                f"Invalid build number for version {version_str}: '{build}' "
                f"(expected >= 1)"
            )

    return len(errors) == 0, errors, warnings


def main():
    """Main validation function."""
    parser = argparse.ArgumentParser(description="Validate changelog format requirements")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code on validation failure (for pre-commit hooks)",
    )
    args = parser.parse_args()

    print("🔍 Validating changelog format...")
    print()

    # Load config if available
    config = load_rw_config()
    changelog_file = get_changelog_path(config)
    
    if not changelog_file.exists():
        print("ℹ️  CHANGELOG.md not found - skipping validation")
        return 0

    is_valid, errors, warnings = validate_changelog_file(changelog_file)

    if errors:
        print("❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  {error}")
        print()
        print("🚨 CHANGELOG FORMAT REQUIREMENTS:")
        print("  - Old format: ## [RC.EPIC.STORY.PATCH] - YYYY-MM-DD")
        print("  - New format: ## [RC.EPIC.STORY.TASK+BUILD] - DD-MM-YY")
        print("  - Examples:")
        print("    - Old: ## [0.9.21.17] - 2025-12-01")
        print("    - New: ## [0.15.1.4+2] - 02-12-25")
        print()
        print("🚨 CANONICAL ORDERING REQUIREMENT:")
        print("  - Versions MUST be ordered by version number (RC.EPIC.STORY.TASK+BUILD)")
        print("  - Ordering: RC → EPIC → STORY → TASK → BUILD")
        print("  - Example: 0.2.4.9+3 must appear before 0.3.2.4+1 (Epic 2 < Epic 3)")
        print("  - Ordering is independent of commit timestamp")
        print()
        print("🚨 DO NOT COMMIT - Fix changelog format/ordering first!")
        return 1

    if warnings:
        print("⚠️  WARNINGS (old format detected - grandfathered):")
        for warning in warnings:
            print(f"  {warning}")
        print()

    print("✅ CHANGELOG.md format validated!")
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
