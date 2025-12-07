---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-07T11:35:00Z
expires_at: null
housekeeping_policy: keep
---

# Framework Dependency Troubleshooting Guide

**Status:** Active  
**Version:** 1.0.0  
**Last Updated:** 2025-12-07  
**Epic:** Epic 5 - Documentation Management and Maintenance  
**Story:** Story 4 - Framework Documentation Management  
**Task:** E05:S04:T05 - Create comprehensive user documentation for Epic 6 framework dependency architecture

---

## Overview

This guide provides solutions to common issues when installing, updating, and using Vibe Dev Kit frameworks as dependencies. Each issue includes symptoms, causes, and step-by-step solutions.

**Quick Navigation:**
- [Installation Issues](#installation-issues)
- [Update Issues](#update-issues)
- [Configuration Issues](#configuration-issues)
- [Path Issues](#path-issues)
- [Version Issues](#version-issues)
- [Git Submodule Issues](#git-submodule-issues)
- [CLI Tool Issues](#cli-tool-issues)
- [Framework Functionality Issues](#framework-functionality-issues)

---

## Installation Issues

### Issue: Framework Installation Fails

**Symptoms:**
- `vibe-dev-kit install` command fails
- Error message about framework not found
- Installation completes but framework files missing

**Causes:**
- Framework name incorrect
- Version not available
- Network issues
- Permission problems
- Backend not available

**Solutions:**

**1. Verify Framework Name:**

```bash
# List available frameworks
vibe-dev-kit list

# Check exact framework name
vibe-dev-kit list --versions | grep workflow
```

**2. Check Version Availability:**

```bash
# List available versions
vibe-dev-kit list --versions workflow-mgmt

# Use available version
vibe-dev-kit install workflow-mgmt@2.0.0
```

**3. Check Network Connection:**

```bash
# Test repository access
git ls-remote https://github.com/earlution/vibe-dev-kit.git

# If fails, check network/firewall
```

**4. Check Permissions:**

```bash
# Verify write permissions
ls -la frameworks/

# Fix permissions if needed
chmod -R u+w frameworks/
```

**5. Check Backend Availability:**

```bash
# Check available backends
vibe-dev-kit list --backends

# Use different backend
vibe-dev-kit install workflow-mgmt --backend git-submodule
```

---

### Issue: Git Submodule Not Initialized

**Symptoms:**
- Framework directory exists but is empty
- `git submodule status` shows uninitialized submodule
- Framework files not accessible

**Causes:**
- Submodule not initialized after clone
- Submodule update not run
- Submodule configuration missing

**Solutions:**

**1. Initialize Submodules:**

```bash
# Initialize all submodules
git submodule update --init --recursive

# Or initialize specific submodule
git submodule update --init .vibe-dev-kit
```

**2. Clone with Submodules:**

```bash
# Clone repository with submodules
git clone --recurse-submodules <repo-url>

# Or after clone
git submodule update --init --recursive
```

**3. Check Submodule Configuration:**

```bash
# Verify .gitmodules file exists
cat .gitmodules

# Should contain:
# [submodule ".vibe-dev-kit"]
#   path = .vibe-dev-kit
#   url = https://github.com/earlution/vibe-dev-kit.git
```

---

### Issue: Framework Files in Wrong Location

**Symptoms:**
- Framework installed but files in unexpected location
- Scripts can't find framework files
- Configuration paths incorrect

**Causes:**
- Custom installation path specified
- Default path configuration incorrect
- Framework copied to wrong directory

**Solutions:**

**1. Check Installation Path:**

```bash
# Check where framework was installed
vibe-dev-kit status workflow-mgmt

# Verify path in configuration
cat .vibe-dev-kit.yaml | grep -A 5 workflow-mgmt
```

**2. Reinstall to Correct Location:**

```bash
# Remove incorrectly installed framework
vibe-dev-kit remove workflow-mgmt

# Reinstall to default location
vibe-dev-kit install workflow-mgmt

# Or specify correct path
vibe-dev-kit install workflow-mgmt --path frameworks/workflow-mgmt
```

**3. Update Configuration:**

```bash
# Edit configuration file
vim .vibe-dev-kit.yaml

# Update path:
# frameworks:
#   workflow-mgmt:
#     path: "frameworks/workflow-mgmt"  # Correct path
```

---

## Update Issues

### Issue: Update Command Fails

**Symptoms:**
- `vibe-dev-kit update` fails with error
- Update partially applied
- Framework in inconsistent state

**Causes:**
- Version not available
- Compatibility issues
- Git conflicts
- Permission problems
- Network issues

**Solutions:**

**1. Check Version Availability:**

```bash
# Verify version exists
vibe-dev-kit list --versions workflow-mgmt

# Use available version
vibe-dev-kit update workflow-mgmt@2.1.0
```

**2. Check Compatibility:**

```bash
# Check compatibility before update
vibe-dev-kit check --compatibility

# Review breaking changes
vibe-dev-kit changelog workflow-mgmt --breaking --from 2.0.0 --to 2.1.0
```

**3. Resolve Git Conflicts:**

```bash
# Check for uncommitted changes
git status

# Commit or stash changes
git add -A
git commit -m "Save work before framework update"

# Or stash
git stash

# Retry update
vibe-dev-kit update workflow-mgmt
```

**4. Force Update:**

```bash
# Force update (use with caution)
vibe-dev-kit update workflow-mgmt --force

# Verify after force update
vibe-dev-kit status workflow-mgmt
```

---

### Issue: Update Not Detected

**Symptoms:**
- Framework has newer version available but not detected
- `vibe-dev-kit check` shows up to date when update exists
- Manual check shows different version

**Causes:**
- Cache not refreshed
- Git tags not fetched
- Version detection logic issue
- Configuration incorrect

**Solutions:**

**1. Refresh Cache:**

```bash
# Clear cache and recheck
vibe-dev-kit check --refresh

# Or manually fetch tags
cd .vibe-dev-kit
git fetch origin --tags
cd ..
vibe-dev-kit check
```

**2. Verify Git Tags:**

```bash
# Check available tags
cd .vibe-dev-kit
git fetch origin --tags
git tag | grep workflow-mgmt | sort -V

# Should show latest version
```

**3. Check Configuration:**

```bash
# Verify framework version in config
cat .vibe-dev-kit.yaml | grep -A 3 workflow-mgmt

# Check if version is pinned
# If pin: true, updates won't be detected
```

---

### Issue: Update Breaks Functionality

**Symptoms:**
- Framework works before update
- After update, validation fails
- Scripts produce errors
- Configuration incompatible

**Causes:**
- Breaking changes in update
- Configuration format changed
- Path changes
- Dependency version mismatch

**Solutions:**

**1. Rollback Update:**

```bash
# Rollback to previous version
vibe-dev-kit update workflow-mgmt@2.0.0

# Or use rollback command
vibe-dev-kit rollback workflow-mgmt
```

**2. Review Changelog:**

```bash
# Check what changed
vibe-dev-kit changelog workflow-mgmt --from 2.0.0 --to 2.1.0

# Look for breaking changes
vibe-dev-kit changelog workflow-mgmt --breaking
```

**3. Update Configuration:**

```bash
# Check for deprecated settings
vibe-dev-kit validate-config

# Fix configuration issues
vibe-dev-kit validate-config --fix

# Or manually update
vim frameworks/workflow-mgmt/rw-config.yaml
```

**4. Check Dependencies:**

```bash
# Verify dependency versions
vibe-dev-kit check-compatibility

# Update dependencies if needed
vibe-dev-kit update numbering-versioning
```

---

## Configuration Issues

### Issue: Configuration Not Found

**Symptoms:**
- CLI commands fail with "configuration not found"
- `.vibe-dev-kit.yaml` missing
- Default configuration not working

**Causes:**
- Configuration file not created
- Configuration file in wrong location
- Configuration file corrupted
- Permissions issue

**Solutions:**

**1. Initialize Configuration:**

```bash
# Create configuration file
vibe-dev-kit init

# Verify file created
ls -la .vibe-dev-kit.yaml
```

**2. Check File Location:**

```bash
# Configuration should be in project root
pwd
ls -la .vibe-dev-kit.yaml

# If not found, create it
vibe-dev-kit init --path .
```

**3. Verify File Format:**

```bash
# Check YAML syntax
cat .vibe-dev-kit.yaml

# Validate configuration
vibe-dev-kit validate-config

# Fix if needed
vibe-dev-kit validate-config --fix
```

---

### Issue: Configuration Invalid

**Symptoms:**
- Configuration file exists but CLI reports errors
- Commands fail with configuration errors
- Settings not applied

**Causes:**
- YAML syntax errors
- Invalid field values
- Missing required fields
- Version mismatch

**Solutions:**

**1. Validate Configuration:**

```bash
# Check for errors
vibe-dev-kit validate-config

# Auto-fix if possible
vibe-dev-kit validate-config --fix
```

**2. Check YAML Syntax:**

```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('.vibe-dev-kit.yaml'))"

# Or use yamllint
yamllint .vibe-dev-kit.yaml
```

**3. Review Configuration Schema:**

```bash
# Check expected structure
vibe-dev-kit config list

# Compare with example
cat .vibe-dev-kit.yaml
# Should match expected structure
```

**4. Reset Configuration:**

```bash
# Backup current config
cp .vibe-dev-kit.yaml .vibe-dev-kit.yaml.backup

# Reset to defaults
vibe-dev-kit config reset

# Restore frameworks
vibe-dev-kit install workflow-mgmt@2.0.0
```

---

## Path Issues

### Issue: Framework Scripts Can't Find Files

**Symptoms:**
- Validation scripts fail with "file not found"
- Path errors in framework execution
- Configuration paths incorrect

**Causes:**
- Paths not updated after installation
- Project structure different from expected
- Configuration paths incorrect
- Relative vs absolute path issues

**Solutions:**

**1. Update Paths in Configuration:**

```bash
# Edit configuration
vim frameworks/workflow-mgmt/rw-config.yaml

# Update paths:
# project:
#   root: "."  # Current directory
# version:
#   file: "src/yourproject/version.py"  # Your actual path
```

**2. Update Paths in Scripts:**

```bash
# Find path references
cd frameworks/workflow-mgmt
grep -r "src/confidentia" .

# Replace with your paths
find . -type f \( -name "*.py" -o -name "*.yaml" \) \
  -exec sed -i '' 's|src/confidentia|src/yourproject|g' {} \;
```

**3. Use Absolute Paths:**

```bash
# In configuration, use absolute paths if relative paths fail
vim frameworks/workflow-mgmt/rw-config.yaml

# Change:
# version:
#   file: "src/yourproject/version.py"
# To:
# version:
#   file: "/absolute/path/to/project/src/yourproject/version.py"
```

**4. Verify Paths:**

```bash
# Test path resolution
cd frameworks/workflow-mgmt
python3 -c "
import os
config_path = 'rw-config.yaml'
if os.path.exists(config_path):
    print('✓ Config file found')
else:
    print('✗ Config file not found')
"
```

---

### Issue: Relative Paths Not Working

**Symptoms:**
- Scripts fail when run from different directories
- Path resolution incorrect
- Framework can't find project files

**Causes:**
- Scripts use relative paths incorrectly
- Working directory not set correctly
- Path resolution logic issue

**Solutions:**

**1. Run from Project Root:**

```bash
# Always run from project root
cd /path/to/project
vibe-dev-kit status

# Or use absolute paths in scripts
```

**2. Set Working Directory:**

```bash
# In scripts, set working directory
cd "$(dirname "$0")/../.."  # Go to project root

# Or use absolute paths
PROJECT_ROOT="/path/to/project"
cd "$PROJECT_ROOT"
```

**3. Update Script Paths:**

```bash
# Make paths relative to project root
vim frameworks/workflow-mgmt/scripts/validation/validate_branch_context.py

# Update path resolution:
# import os
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
# VERSION_FILE = os.path.join(PROJECT_ROOT, 'src/yourproject/version.py')
```

---

## Version Issues

### Issue: Version Mismatch

**Symptoms:**
- Version in `version.py` doesn't match branch
- Validation fails with version mismatch
- Changelog version incorrect

**Causes:**
- Version not updated before RW
- Branch context incorrect
- Version file out of sync
- Manual version edit

**Solutions:**

**1. Check Current Version:**

```bash
# Check version file
python3 -c "import sys; sys.path.insert(0, 'src'); from yourproject import version; print(version.VERSION_STRING)"

# Check branch
git branch --show-current
```

**2. Update Version:**

```bash
# Edit version file
vim src/yourproject/version.py

# Update to match current work:
# VERSION_EPIC = 1
# VERSION_STORY = 1
# VERSION_TASK = 1
# VERSION_BUILD = 1
```

**3. Validate Version:**

```bash
# Run validation
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_branch_context.py

# Fix any issues reported
```

---

### Issue: Version Not Incrementing

**Symptoms:**
- BUILD number not incrementing
- Version stays same after RW
- Multiple releases with same version

**Causes:**
- BUILD not incremented in version file
- RW not bumping version correctly
- Version file not updated

**Solutions:**

**1. Manually Increment BUILD:**

```bash
# Edit version file
vim src/yourproject/version.py

# Increment BUILD:
# VERSION_BUILD = 2  # Was 1, now 2
```

**2. Check RW Version Bump:**

```bash
# RW should increment BUILD automatically
# If not, check RW configuration
cat frameworks/workflow-mgmt/rw-config.yaml | grep -A 5 version
```

**3. Verify Version Update:**

```bash
# After RW, check version
python3 -c "import sys; sys.path.insert(0, 'src'); from yourproject import version; print(version.VERSION_STRING)"

# Should show incremented BUILD
```

---

## Git Submodule Issues

### Issue: Submodule Points to Wrong Commit

**Symptoms:**
- Framework files outdated
- Submodule shows different commit than expected
- Framework version incorrect

**Causes:**
- Submodule not updated after tag checkout
- Wrong tag checked out
- Submodule commit out of sync

**Solutions:**

**1. Check Submodule Status:**

```bash
# Check submodule commit
cd .vibe-dev-kit
git log -1 --oneline

# Check current tag
git describe --tags
```

**2. Checkout Correct Tag:**

```bash
# List available tags
git tag | grep workflow-mgmt

# Checkout correct tag
git checkout workflow-mgmt-v2.0.0

# Return to project root
cd ..

# Copy updated framework
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt
```

**3. Update Submodule Reference:**

```bash
# Update submodule to latest
cd .vibe-dev-kit
git fetch origin
git checkout workflow-mgmt-v2.1.0
cd ..

# Commit submodule update
git add .vibe-dev-kit
git commit -m "Update submodule to workflow-mgmt-v2.1.0"
```

---

### Issue: Submodule Update Conflicts

**Symptoms:**
- `git submodule update` fails
- Merge conflicts in submodule
- Submodule in detached HEAD state

**Causes:**
- Local changes in submodule
- Submodule commit conflicts
- Submodule branch issues

**Solutions:**

**1. Reset Submodule:**

```bash
# Navigate to submodule
cd .vibe-dev-kit

# Reset to remote state
git fetch origin
git reset --hard origin/main

# Or checkout specific tag
git checkout workflow-mgmt-v2.0.0
```

**2. Remove and Re-add Submodule:**

```bash
# Remove submodule
git submodule deinit .vibe-dev-kit
git rm .vibe-dev-kit
rm -rf .git/modules/.vibe-dev-kit

# Re-add submodule
git submodule add https://github.com/earlution/vibe-dev-kit.git .vibe-dev-kit
cd .vibe-dev-kit
git checkout workflow-mgmt-v2.0.0
cd ..
```

---

## CLI Tool Issues

### Issue: Command Not Found

**Symptoms:**
- `vibe-dev-kit` command not found
- "command not found" error
- CLI tool not in PATH

**Causes:**
- CLI tool not installed
- Not in Python PATH
- Virtual environment not activated
- Installation incomplete

**Solutions:**

**1. Check Installation:**

```bash
# Check if installed
pip show vibe-dev-kit

# If not installed, install it
pip install vibe-dev-kit
```

**2. Check Python PATH:**

```bash
# Check Python path
python3 -m site --user-base

# Add to PATH if needed
export PATH="$HOME/.local/bin:$PATH"
```

**3. Use Python Module:**

```bash
# Run as Python module
python3 -m vibe_dev_kit install workflow-mgmt

# Or use full path
~/.local/bin/vibe-dev-kit install workflow-mgmt
```

---

### Issue: CLI Configuration Errors

**Symptoms:**
- CLI commands fail with config errors
- Configuration not recognized
- Settings not applied

**Causes:**
- Configuration file format incorrect
- Configuration file missing
- Configuration version mismatch
- Permissions issue

**Solutions:**

**1. Validate Configuration:**

```bash
# Check configuration
vibe-dev-kit validate-config

# Fix issues
vibe-dev-kit validate-config --fix
```

**2. Reinitialize Configuration:**

```bash
# Backup current config
cp .vibe-dev-kit.yaml .vibe-dev-kit.yaml.backup

# Reinitialize
vibe-dev-kit init

# Restore frameworks
vibe-dev-kit install workflow-mgmt@2.0.0
```

---

## Framework Functionality Issues

### Issue: Release Workflow Fails

**Symptoms:**
- RW command fails
- Validation errors during RW
- RW steps incomplete

**Causes:**
- Branch context mismatch
- Version issues
- Changelog format errors
- Git issues
- Configuration problems

**Solutions:**

**1. Check Branch Context:**

```bash
# Verify branch matches version
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_branch_context.py

# Fix branch or version
```

**2. Check Version:**

```bash
# Verify version file
python3 -c "import sys; sys.path.insert(0, 'src'); from yourproject import version; print(version.VERSION_STRING)"

# Update if needed
vim src/yourproject/version.py
```

**3. Check Changelog:**

```bash
# Validate changelog format
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_changelog_format.py

# Fix any format issues
```

**4. Check Git Status:**

```bash
# Ensure clean working directory
git status

# Commit or stash changes
git add -A
git commit -m "Save work"
```

---

### Issue: Kanban Update Script Fails

**Symptoms:**
- Kanban board not updating
- Update script errors
- Epic/Story docs out of sync

**Causes:**
- Script path incorrect
- File permissions
- Missing dependencies
- Configuration issues

**Solutions:**

**1. Check Script Path:**

```bash
# Verify script exists
ls -la frameworks/kanban/scripts/update-kanban-docs.py

# Check script permissions
chmod +x frameworks/kanban/scripts/update-kanban-docs.py
```

**2. Run Script Manually:**

```bash
# Run script directly
cd frameworks/kanban
python3 scripts/update-kanban-docs.py

# Check for errors
python3 scripts/update-kanban-docs.py --verbose
```

**3. Check Dependencies:**

```bash
# Verify Python dependencies
python3 -c "import yaml; print('yaml OK')"
python3 -c "import json; print('json OK')"

# Install missing dependencies
pip install pyyaml
```

---

## Getting Help

### Diagnostic Information

**Collect Diagnostic Info:**

```bash
# System information
uname -a
python3 --version
git --version

# CLI information
vibe-dev-kit --version
vibe-dev-kit status --verbose

# Configuration
cat .vibe-dev-kit.yaml

# Framework status
vibe-dev-kit status
ls -la frameworks/
```

### Reporting Issues

**Create Issue Report:**

```bash
# Use CLI to report issue
vibe-dev-kit report-issue \
  --framework workflow-mgmt \
  --version 2.0.0 \
  --description "Update fails with error X"

# Or create GitHub issue with:
# - Framework name and version
# - Error message
# - Steps to reproduce
# - Diagnostic information
```

---

## References

- [Installation Guide](framework-dependency-installation-guide.md)
- [Usage Guide](framework-dependency-usage-guide.md)
- [Update Guide](framework-dependency-update-guide.md)
- [Integration Guide](framework-dependency-integration-guide.md)
- [CLI Reference](framework-dependency-cli-reference.md)

