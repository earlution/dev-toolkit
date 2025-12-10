#!/usr/bin/env python3
"""
GitHub Badges - Dynamic Badge Selection

Automatically detects repository visibility and updates README badges accordingly.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple


def detect_repo_visibility(repo: Optional[str] = None) -> Tuple[bool, str]:
    """
    Detect repository visibility (public/private).
    
    Returns:
        Tuple of (is_private: bool, method_used: str)
    """
    # Auto-detect repository from git if not provided
    if not repo:
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True
            )
            remote_url = result.stdout.strip()
            # Extract owner/repo from URL
            # Supports: https://github.com/owner/repo.git or git@github.com:owner/repo.git
            match = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", remote_url)
            if match:
                repo = f"{match.group(1)}/{match.group(2)}"
            else:
                return False, "error"
        except subprocess.CalledProcessError:
            return False, "error"
    
    if not repo:
        return False, "error"
    
    # Try GitHub CLI first
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}", "--jq", ".private"],
            capture_output=True,
            text=True,
            check=True
        )
        is_private = result.stdout.strip().lower() == "true"
        return is_private, "gh_cli"
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    # Fallback to token-based API
    token = os.getenv("GITHUB_TOKEN")
    if token:
        try:
            result = subprocess.run(
                [
                    "curl", "-s", "-H",
                    f"Authorization: Bearer {token}",
                    f"https://api.github.com/repos/{repo}"
                ],
                capture_output=True,
                text=True,
                check=True
            )
            # Use jq to parse JSON
            jq_result = subprocess.run(
                ["jq", "-r", ".private"],
                input=result.stdout,
                capture_output=True,
                text=True,
                check=True
            )
            is_private = jq_result.stdout.strip().lower() == "true"
            return is_private, "token_api"
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    
    # Detection failed - default to private (safe fallback)
    return True, "fallback"


def get_badge_urls(repo: str, is_private: bool) -> dict:
    """Get badge URLs based on repository visibility."""
    if is_private:
        # Static badges for private repos
        return {
            "contributors": "https://img.shields.io/badge/contributors-welcome-blue.svg?style=for-the-badge",
            "forks": "https://img.shields.io/badge/forks-welcome-blue.svg?style=for-the-badge",
            "stars": "https://img.shields.io/badge/stars-welcome-blue.svg?style=for-the-badge",
            "issues": "https://img.shields.io/badge/issues-welcome-blue.svg?style=for-the-badge",
            "license": "https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge",
        }
    else:
        # Dynamic badges for public repos
        return {
            "contributors": f"https://img.shields.io/github/contributors/{repo}.svg?style=for-the-badge",
            "forks": f"https://img.shields.io/github/forks/{repo}.svg?style=for-the-badge",
            "stars": f"https://img.shields.io/github/stars/{repo}.svg?style=for-the-badge",
            "issues": f"https://img.shields.io/github/issues/{repo}.svg?style=for-the-badge",
            "license": f"https://img.shields.io/github/license/{repo}.svg?style=for-the-badge",
        }


def update_readme_badges(readme_path: Path, repo: str, is_private: bool, dry_run: bool = False) -> bool:
    """Update badge URLs in README.md."""
    if not readme_path.exists():
        print(f"Error: README not found at {readme_path}", file=sys.stderr)
        return False
    
    badge_urls = get_badge_urls(repo, is_private)
    content = readme_path.read_text()
    original_content = content
    
    # Replace badge URLs
    # Pattern: [badge-name-shield]: URL
    replacements = {
        "contributors-shield": badge_urls["contributors"],
        "forks-shield": badge_urls["forks"],
        "stars-shield": badge_urls["stars"],
        "issues-shield": badge_urls["issues"],
        "license-shield": badge_urls["license"],
    }
    
    for badge_name, new_url in replacements.items():
        # Match: [badge-name-shield]: URL
        pattern = rf"(\[{badge_name}\]):\s*https?://[^\s]+"
        replacement = rf"\1: {new_url}"
        content = re.sub(pattern, replacement, content)
    
    if dry_run:
        if content != original_content:
            print("Would update README badges:")
            print("=" * 60)
            diff_lines = [
                line for line in content.split("\n")
                if line != original_content.split("\n")[content.split("\n").index(line)]
                if line.startswith("[") and "shield" in line
            ]
            for line in diff_lines[:10]:  # Show first 10 changes
                print(line)
            print("=" * 60)
        else:
            print("No badge changes needed.")
        return True
    
    if content != original_content:
        readme_path.write_text(content)
        print(f"✅ Updated badges in {readme_path}")
        print(f"   Repository: {repo} ({'private' if is_private else 'public'})")
        return True
    else:
        print("No badge changes needed.")
        return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Update GitHub README badges based on repository visibility"
    )
    parser.add_argument(
        "--repo",
        help="Repository in format OWNER/REPO (default: auto-detect from git)"
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to README.md (default: ./README.md)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without modifying files"
    )
    
    args = parser.parse_args()
    
    # Detect repository visibility
    is_private, method = detect_repo_visibility(args.repo)
    
    if method == "error":
        print("Error: Could not detect repository. Use --repo OWNER/REPO", file=sys.stderr)
        sys.exit(1)
    
    # Get repository name
    repo = args.repo
    if not repo:
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True
            )
            remote_url = result.stdout.strip()
            match = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", remote_url)
            if match:
                repo = f"{match.group(1)}/{match.group(2)}"
        except subprocess.CalledProcessError:
            print("Error: Could not detect repository. Use --repo OWNER/REPO", file=sys.stderr)
            sys.exit(1)
    
    if not repo:
        print("Error: Repository not specified and could not be auto-detected", file=sys.stderr)
        sys.exit(1)
    
    # Update README
    readme_path = Path(args.readme)
    success = update_readme_badges(readme_path, repo, is_private, args.dry_run)
    
    if not success:
        sys.exit(1)
    
    if args.dry_run:
        print(f"\nDetection method: {method}")
        print(f"Repository: {repo} ({'private' if is_private else 'public'})")


if __name__ == "__main__":
    main()

