#!/usr/bin/env python3
"""
Changelog Format Validator

Validates that CHANGELOG.md follows the required format:
- Version entries follow RC.EPIC.STORY.PATCH format (old) or RC.EPIC.STORY.TASK+BUILD format (new)
- Date format is YYYY-MM-DD (old) or DD-MM-YY (new)

This script is called by pre-commit hooks and CI to enforce changelog standards.

Usage:
    python scripts/validation/validate_changelog_format.py [--strict]
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Tuple, List

# Version patterns: RC.EPIC.STORY.PATCH (old) or RC.EPIC.STORY.TASK+BUILD (new)
# Support both formats for backward compatibility
OLD_VERSION_PATTERN = re.compile(r"## \[(\d+)\.(\d+)\.(\d+)\.(\d+)\] - (\d{4}-\d{2}-\d{2})")
NEW_VERSION_PATTERN = re.compile(r"## \[(\d+)\.(\d+)\.(\d+)\.(\d+)\+(\d+)\] - (\d{2}-\d{2}-\d{2})")


def validate_changelog_file(filepath: Path) -> Tuple[bool, List[str], List[str]]:
    """
    Validate CHANGELOG.md format.

    Returns:
        (is_valid, errors, warnings)
    """
    if not filepath.exists():
        return False, [f"File does not exist: {filepath}"], []

    content = filepath.read_text()
    errors = []
    warnings = []

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

    changelog_file = Path("CHANGELOG.md")
    
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
        print("🚨 DO NOT COMMIT - Fix changelog format first!")
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
