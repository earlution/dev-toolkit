# GitHub Badges - Dynamic Badge Selection

Automatically detects repository visibility and selects appropriate badge types for GitHub README files.

## Overview

This tool solves the common problem of "REPO NOT FOUND" errors when using dynamic GitHub badges on private repositories. It automatically detects whether a repository is public or private and updates the README badges accordingly.

## Features

- ✅ Detects repository visibility (public/private)
- ✅ Automatically switches between dynamic and static badges
- ✅ Safe fallback to static badges if detection fails
- ✅ Supports both GitHub CLI and token-based authentication
- ✅ Preserves badge links and functionality

## Installation

### Prerequisites

- Python 3.7+
- `jq` (for JSON parsing)
  - macOS: `brew install jq`
  - Linux: `apt install jq` or `yum install jq`

### GitHub Authentication (Choose One)

#### Option 1: GitHub CLI (Recommended)

```bash
# Install GitHub CLI
brew install gh  # macOS
# or
apt install gh   # Linux

# Authenticate
gh auth login

# Verify
gh auth status
```

#### Option 2: GitHub Token

```bash
# Create token at: https://github.com/settings/tokens
# Scopes needed: public_repo (public repos) or repo (private repos)

# Set environment variable
export GITHUB_TOKEN=your_token_here

# Add to shell profile (optional)
echo 'export GITHUB_TOKEN=your_token_here' >> ~/.zshrc  # or ~/.bashrc
```

## Usage

### Basic Usage

```bash
cd tools/github-badges
python3 update_badges.py
```

The script will:
1. Detect repository visibility
2. Read `README.md` in the current directory
3. Update badge URLs based on visibility
4. Write updated `README.md`

### Command Line Options

```bash
python3 update_badges.py [OPTIONS]

Options:
  --repo OWNER/REPO    Specify repository (default: auto-detect from git)
  --readme PATH        Path to README.md (default: ./README.md)
  --dry-run            Show what would change without modifying files
  --help               Show this help message
```

### Examples

```bash
# Update badges in current repository
python3 update_badges.py

# Update badges for specific repository
python3 update_badges.py --repo earlution/starborn-legacy

# Dry run to see what would change
python3 update_badges.py --dry-run

# Specify custom README path
python3 update_badges.py --readme ../README.md
```

## How It Works

1. **Detection:** Uses GitHub API to check repository visibility
   - GitHub CLI: `gh api repos/OWNER/REPO --jq .private`
   - Token: `curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/repos/OWNER/REPO | jq -r .private`

2. **Badge Selection:**
   - **Public repo** → Dynamic GitHub badges (contributors, forks, stars, issues, license)
   - **Private repo** → Static badges (welcome/placeholder badges)
   - **Detection fails** → Defaults to static badges (safe fallback)

3. **README Update:** Replaces badge URLs in README.md based on visibility

## Badge Types

### Dynamic Badges (Public Repos)
- Contributors: `https://img.shields.io/github/contributors/OWNER/REPO.svg?style=for-the-badge`
- Forks: `https://img.shields.io/github/forks/OWNER/REPO.svg?style=for-the-badge`
- Stars: `https://img.shields.io/github/stars/OWNER/REPO.svg?style=for-the-badge`
- Issues: `https://img.shields.io/github/issues/OWNER/REPO.svg?style=for-the-badge`
- License: `https://img.shields.io/github/license/OWNER/REPO.svg?style=for-the-badge`

### Static Badges (Private Repos)
- Contributors: `https://img.shields.io/badge/contributors-welcome-blue.svg?style=for-the-badge`
- Forks: `https://img.shields.io/badge/forks-welcome-blue.svg?style=for-the-badge`
- Stars: `https://img.shields.io/badge/stars-welcome-blue.svg?style=for-the-badge`
- Issues: `https://img.shields.io/badge/issues-welcome-blue.svg?style=for-the-badge`
- License: `https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge`

## Integration

### Manual Usage
Run the script whenever you need to update badges (e.g., after changing repository visibility).

### Pre-commit Hook
Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python3 tools/github-badges/update_badges.py
```

### CI/CD Integration
Add to your GitHub Actions workflow:

```yaml
- name: Update Badges
  run: |
    python3 tools/github-badges/update_badges.py
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Troubleshooting

### "REPO NOT FOUND" errors
- Ensure repository name is correct
- Check GitHub authentication (CLI or token)
- Verify repository exists and you have access

### Authentication failures
- **GitHub CLI:** Run `gh auth login` and verify with `gh auth status`
- **Token:** Check `GITHUB_TOKEN` environment variable is set correctly
- Verify token has correct scopes (`public_repo` or `repo`)

### Script fails silently
- Use `--dry-run` to see what would change
- Check script output for error messages
- Verify `jq` is installed and in PATH

## Requirements

See [requirements.txt](requirements.txt) for Python dependencies.

## License

MIT License - see [LICENSE](../../LICENSE) file for details.

## Related

- Part of [Earlution Dev Toolkit](https://github.com/earlution/dev-toolkit)
- Created for use across multiple projects including [Starborn Legacy](https://github.com/earlution/starborn-legacy)

