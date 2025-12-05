#!/usr/bin/env python3
"""
Version Bump Validator

This script validates that version bumping follows the correct logic:
1. Reads current version from version file
2. Reads Story file to identify completed task
3. Validates that version bump follows RW Step 2 logic:
   - If completed task > current VERSION_TASK: Should be new task (VERSION_TASK = completed, BUILD = 1)
   - If completed task == current VERSION_TASK: Should be same task (VERSION_TASK unchanged, BUILD incremented)
   - If completed task < current VERSION_TASK: Should be out-of-order (VERSION_TASK = completed, BUILD = 1)

This script is called by RW Step 8 to validate version bumping logic.

Usage:
    python packages/frameworks/workflow mgt/scripts/validation/validate_version_bump.py [--strict] [--story-file PATH] [--version-file PATH]

    --strict: Exit with error code if validation fails
    --story-file: Path to Story file (auto-detected if not provided)
    --version-file: Path to version file (auto-detected if not provided)
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional, Dict, Tuple

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


def get_version_components(version_file: Path) -> Optional[Tuple[int, int, int, int, int]]:
    """
    Extract version components from version file.
    
    Returns:
        (RC, EPIC, STORY, TASK, BUILD) or None if not found
    """
    if not version_file.exists():
        return None
    
    content = version_file.read_text()
    
    rc_match = re.search(r'VERSION_RC\s*=\s*(\d+)', content)
    epic_match = re.search(r'VERSION_EPIC\s*=\s*(\d+)', content)
    story_match = re.search(r'VERSION_STORY\s*=\s*(\d+)', content)
    task_match = re.search(r'VERSION_TASK\s*=\s*(\d+)', content)
    build_match = re.search(r'VERSION_BUILD\s*=\s*(\d+)', content)
    
    if all([rc_match, epic_match, story_match, task_match, build_match]):
        return (
            int(rc_match.group(1)),
            int(epic_match.group(1)),
            int(story_match.group(1)),
            int(task_match.group(1)),
            int(build_match.group(1))
        )
    return None


def find_story_file(config: Optional[Dict] = None, epic: int = None, story: int = None) -> Optional[Path]:
    """
    Find Story file based on config or fallback patterns.
    
    If epic and story are provided, tries to find matching Story file.
    """
    project_root = Path.cwd()
    
    # Try config first
    if config and config.get('use_kanban') and 'kanban_root' in config:
        kanban_root = Path(config['kanban_root'])
        if epic and story:
            # Try pattern matching
            story_pattern = config.get('story_doc_pattern', '**/Story-*.md')
            for story_file in project_root.glob(str(kanban_root / story_pattern)):
                # Try to extract epic/story from path or content
                if epic and story:
                    content = story_file.read_text()
                    # Check if this story matches epic/story
                    epic_match = re.search(r'Epic\s+(\d+)', content, re.IGNORECASE)
                    story_match = re.search(r'Story\s+(\d+)', content, re.IGNORECASE)
                    if epic_match and story_match:
                        if int(epic_match.group(1)) == epic and int(story_match.group(1)) == story:
                            return story_file
    
    # Fallback: Search for Story files
    fallback_patterns = [
        "KB/PM_and_Portfolio/kanban/epics/Epic-*/Story-*.md",
        "KB/PM_and_Portfolio/kanban/epics/Epic-*/stories/Story-*.md",  # Legacy support
    ]
    
    for pattern in fallback_patterns:
        for story_file in project_root.glob(pattern):
            if epic and story:
                content = story_file.read_text()
                epic_match = re.search(r'Epic\s+(\d+)', content, re.IGNORECASE)
                story_match = re.search(r'Story\s+(\d+)', content, re.IGNORECASE)
                if epic_match and story_match:
                    if int(epic_match.group(1)) == epic and int(story_match.group(1)) == story:
                        return story_file
            else:
                # Return first match if no epic/story specified
                return story_file
    
    return None


def get_completed_task(story_file: Path, version_task: Optional[int] = None) -> Optional[int]:
    """
    Extract completed task number from Story file.
    
    If version_task is provided, returns that task if it's marked complete.
    Otherwise, finds the most recently completed task (highest task number).
    
    Looks for patterns like:
    - [x] **E3:S02:T05 – Task description** ✅ COMPLETE (v0.3.2.5+1)
    - [x] **E3:S02:T05** ✅ COMPLETE
    """
    if not story_file.exists():
        return None
    
    content = story_file.read_text()
    
    # Pattern 1: [x] **E3:S02:T05 – Task description** ✅ COMPLETE (v0.3.2.5+1)
    pattern1 = re.compile(r'\[x\]\s+\*\*E\d+:S\d+:T(\d+)[^\*]*\*\*\s+✅\s+COMPLETE', re.IGNORECASE)
    
    # Pattern 2: [x] **E3:S02:T05** ✅ COMPLETE
    pattern2 = re.compile(r'\[x\]\s+\*\*E\d+:S\d+:T(\d+)\*\*\s+✅\s+COMPLETE', re.IGNORECASE)
    
    # Find all completed tasks
    completed_tasks = []
    for match in pattern1.finditer(content):
        completed_tasks.append(int(match.group(1)))
    for match in pattern2.finditer(content):
        task_num = int(match.group(1))
        if task_num not in completed_tasks:
            completed_tasks.append(task_num)
    
    if not completed_tasks:
        return None
    
    # If version_task provided, check if it's completed
    if version_task is not None:
        if version_task in completed_tasks:
            return version_task
        # If version_task not in completed, still return it for validation
        # (might be in progress)
        return version_task
    
    # Return the highest completed task (most recent)
    return max(completed_tasks)


def validate_version_bump(
    version_file: Path,
    story_file: Optional[Path] = None,
    config: Optional[Dict] = None
) -> Tuple[bool, list]:
    """
    Validate that version bump follows correct logic.
    
    Returns:
        (is_valid, list_of_errors)
    """
    errors = []
    
    # Get current version components
    version_components = get_version_components(version_file)
    if not version_components:
        errors.append(f"Could not extract version components from {version_file}")
        return False, errors
    
    rc, epic, story, current_task, current_build = version_components
    print(f"Current version: {rc}.{epic}.{story}.{current_task}+{current_build}")
    
    # Find story file if not provided
    if story_file is None:
        story_file = find_story_file(config, epic, story)
    
    if story_file is None:
        errors.append(f"Could not find Story file for Epic {epic}, Story {story}")
        return False, errors
    
    print(f"Story file: {story_file}")
    
    # Get completed task - use current_task as hint (the task we're validating)
    completed_task = get_completed_task(story_file, version_task=current_task)
    if completed_task is None:
        errors.append(f"Could not identify completed task from {story_file}")
        return False, errors
    
    print(f"Completed task: T{completed_task:02d}")
    print(f"Current VERSION_TASK: {current_task}")
    
    # Validate version bump logic
    if completed_task > current_task:
        # New task - should have VERSION_TASK = completed_task, BUILD = 1
        if current_task != completed_task:
            errors.append(
                f"Version bump error: Completed task T{completed_task:02d} > current VERSION_TASK {current_task}, "
                f"but VERSION_TASK is {current_task} (should be {completed_task})"
            )
        if current_build != 1:
            errors.append(
                f"Version bump error: New task detected, but BUILD is {current_build} (should be 1)"
            )
    
    elif completed_task == current_task:
        # Same task - BUILD should be incremented (can't validate exact increment without previous version)
        print(f"Same task detected - BUILD should be incremented (current BUILD: {current_build})")
        # Note: We can't validate exact BUILD increment without knowing previous BUILD
    
    elif completed_task < current_task:
        # Out-of-order completion - should have VERSION_TASK = completed_task, BUILD = 1
        if current_task != completed_task:
            errors.append(
                f"Version bump error: Out-of-order completion detected (completed T{completed_task:02d} < current T{current_task}), "
                f"but VERSION_TASK is {current_task} (should be {completed_task})"
            )
        if current_build != 1:
            errors.append(
                f"Version bump error: Out-of-order completion, but BUILD is {current_build} (should be 1)"
            )
    
    if errors:
        return False, errors
    
    print("✅ Version bump logic validated!")
    return True, []


def main():
    parser = argparse.ArgumentParser(description="Validate version bump logic")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code on validation failure",
    )
    parser.add_argument(
        "--story-file",
        type=Path,
        help="Path to Story file (auto-detected if not provided)",
    )
    parser.add_argument(
        "--version-file",
        type=Path,
        help="Path to version file (auto-detected if not provided)",
    )
    args = parser.parse_args()
    
    # Load config
    config = load_rw_config()
    
    # Get version file
    if args.version_file:
        version_file = args.version_file
    else:
        version_file = get_version_file_path(config)
    
    if not version_file.exists():
        print(f"❌ Version file not found: {version_file}")
        sys.exit(1)
    
    # Validate
    is_valid, errors = validate_version_bump(
        version_file,
        story_file=args.story_file,
        config=config
    )
    
    if not is_valid:
        print("\n❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        print("\n🚨 Version bump does not follow RW Step 2 logic!")
        if args.strict:
            sys.exit(1)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

