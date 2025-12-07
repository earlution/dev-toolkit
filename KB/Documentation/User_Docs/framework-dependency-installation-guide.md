---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-06T22:30:00Z
expires_at: null
housekeeping_policy: keep
---

# Framework Dependency Installation Guide

**Status:** Active  
**Version:** 1.0.0  
**Last Updated:** 2025-12-06  
**Epic:** Epic 5 - Documentation Management and Maintenance  
**Story:** Story 4 - Framework Documentation Management  
**Task:** E05:S04:T05 - Create comprehensive user documentation for Epic 6 framework dependency architecture

---

## Overview

This guide explains how to install Vibe Dev Kit frameworks as dependencies in your project. Frameworks can be installed using three methods: Git submodules (Phase 1), the `vibe-dev-kit` CLI tool (Phase 2), or package managers like npm/pip (Phase 3).

**What you get:** Frameworks installed as dependencies can be automatically updated when improvements are made, with notifications about available updates. This replaces the previous copy-paste approach.

---

## Prerequisites

Before installing frameworks, ensure you have:

- **Git** installed and configured
- **Python 3.8+** (for CLI tool and some frameworks)
- **Node.js 16+** (if using npm package manager)
- **A Git repository** for your project (frameworks are installed as Git dependencies)

**System Requirements:**
- Unix-like system (Linux, macOS) or Windows with Git Bash/WSL
- Terminal/command line access
- Write permissions to your project directory

---

## Installation Methods

### Method 1: Git Submodules (Phase 1 - Available Now)

Git submodules allow you to include the vibe-dev-kit repository (or specific frameworks) as a subdirectory in your project, with version control via Git tags.

#### Installation Steps

**1. Add the vibe-dev-kit repository as a submodule:**

```bash
# Navigate to your project root
cd /path/to/your/project

# Add the entire vibe-dev-kit repository as a submodule
git submodule add https://github.com/earlution/vibe-dev-kit.git .vibe-dev-kit

# Or add to a specific directory
git submodule add https://github.com/earlution/vibe-dev-kit.git frameworks/vibe-dev-kit
```

**2. Checkout a specific framework version (recommended):**

```bash
# Navigate to the submodule
cd .vibe-dev-kit

# List available framework tags
git tag | grep framework

# Checkout a specific framework version (e.g., workflow-mgmt-v2.0.0)
git checkout workflow-mgmt-v2.0.0

# Return to project root
cd ..
```

**3. Copy the framework to your project structure:**

```bash
# Copy the workflow management framework
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Or copy multiple frameworks
cp -r .vibe-dev-kit/packages/frameworks/kanban/ ./frameworks/kanban
cp -r ".vibe-dev-kit/packages/frameworks/numbering & versioning" ./frameworks/numbering-versioning
```

**4. Commit the submodule reference:**

```bash
git add .gitmodules .vibe-dev-kit frameworks/
git commit -m "Add vibe-dev-kit frameworks as Git submodule"
```

#### Updating Frameworks (Git Submodules)

**Check for updates:**

```bash
# Navigate to submodule
cd .vibe-dev-kit

# Fetch latest changes
git fetch origin

# List new tags
git tag | grep framework

# Checkout new version
git checkout workflow-mgmt-v2.1.0

# Return to project root
cd ..

# Copy updated framework
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Commit update
git add frameworks/
git commit -m "Update workflow-mgmt framework to v2.1.0"
```

**Automated update script:**

Create `scripts/update-frameworks.sh`:

```bash
#!/bin/bash
# Update all frameworks from Git submodule

cd .vibe-dev-kit
git fetch origin
git checkout workflow-mgmt-v2.1.0  # Update to desired version
cd ..

# Copy updated frameworks
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt
cp -r .vibe-dev-kit/packages/frameworks/kanban/ ./frameworks/kanban

echo "Frameworks updated. Review changes and commit."
```

#### Advantages of Git Submodules

- **Version control:** Pin frameworks to specific Git tags
- **No external dependencies:** Works with Git only
- **Explicit updates:** You control when to update
- **Full access:** Access to entire vibe-dev-kit repository

#### Limitations of Git Submodules

- **Manual updates:** Requires manual copying after submodule update
- **Git knowledge:** Requires understanding of Git submodules
- **Repository size:** Includes entire vibe-dev-kit repository

---

### Method 2: CLI Tool (Phase 2 - Coming Soon)

The `vibe-dev-kit` CLI tool provides a unified interface for installing and managing frameworks across all dependency backends.

#### Installation Steps

**1. Install the CLI tool:**

```bash
# Install via pip
pip install vibe-dev-kit

# Or install from source
git clone https://github.com/earlution/vibe-dev-kit.git
cd vibe-dev-kit
pip install -e .
```

**2. Initialize vibe-dev-kit in your project:**

```bash
cd /path/to/your/project
vibe-dev-kit init
```

This creates a `.vibe-dev-kit.yaml` configuration file:

```yaml
project_root: .
frameworks_dir: ./frameworks
backend: git_submodule  # or 'npm', 'pip'
auto_update: false
```

**3. Install a framework:**

```bash
# Install workflow management framework
vibe-dev-kit install workflow-mgmt

# Install specific version
vibe-dev-kit install workflow-mgmt@2.0.0

# Install multiple frameworks
vibe-dev-kit install workflow-mgmt kanban numbering-versioning
```

**4. Check installed frameworks:**

```bash
vibe-dev-kit status
```

Output:
```
Installed Frameworks:
  workflow-mgmt: v2.0.0 (git_submodule)
  kanban: v1.5.0 (git_submodule)
  numbering-versioning: v2.1.0 (git_submodule)
```

#### Updating Frameworks (CLI Tool)

**Check for updates:**

```bash
vibe-dev-kit check
```

Output:
```
Available Updates:
  workflow-mgmt: v2.0.0 → v2.1.0 (minor update)
  kanban: v1.5.0 → v1.6.0 (patch update)
```

**Update a framework:**

```bash
# Update specific framework
vibe-dev-kit update workflow-mgmt

# Update all frameworks
vibe-dev-kit update --all

# Update to specific version
vibe-dev-kit update workflow-mgmt@2.1.0
```

**Automatic update notifications:**

The CLI tool can be configured to check for updates and notify you:

```bash
# Enable automatic update checks
vibe-dev-kit config set auto_check true
vibe-dev-kit config set check_interval daily

# Run update check (can be added to CI/CD)
vibe-dev-kit check --notify
```

#### Advantages of CLI Tool

- **Unified interface:** Same commands for all backends
- **Automatic management:** Handles submodule/package manager details
- **Update notifications:** Built-in update checking
- **Version management:** Easy version pinning and updates

---

### Method 3: Package Managers (Phase 3 - Future)

Frameworks will be published as npm packages (for Node.js projects) and pip packages (for Python projects), enabling standard package manager workflows.

#### Installation Steps (npm - Future)

```bash
# Install workflow management framework
npm install @vibe-dev-kit/workflow-mgmt

# Install specific version
npm install @vibe-dev-kit/workflow-mgmt@2.0.0

# Install multiple frameworks
npm install @vibe-dev-kit/workflow-mgmt @vibe-dev-kit/kanban
```

#### Installation Steps (pip - Future)

```bash
# Install workflow management framework
pip install vibe-dev-kit-workflow-mgmt

# Install specific version
pip install vibe-dev-kit-workflow-mgmt==2.0.0

# Install multiple frameworks
pip install vibe-dev-kit-workflow-mgmt vibe-dev-kit-kanban
```

#### Updating Frameworks (Package Managers)

**npm:**

```bash
# Check for updates
npm outdated

# Update to latest compatible version
npm update @vibe-dev-kit/workflow-mgmt

# Update to specific version
npm install @vibe-dev-kit/workflow-mgmt@2.1.0
```

**pip:**

```bash
# Check for updates
pip list --outdated

# Update to latest version
pip install --upgrade vibe-dev-kit-workflow-mgmt

# Update to specific version
pip install --upgrade vibe-dev-kit-workflow-mgmt==2.1.0
```

#### Advantages of Package Managers

- **Standard workflow:** Uses familiar package manager commands
- **Dependency resolution:** Automatic dependency management
- **Version locking:** `package.json` or `requirements.txt` pin versions
- **CI/CD integration:** Standard package manager workflows

---

## Post-Installation Setup

After installing frameworks, you need to configure them for your project:

### 1. Update File Paths

Frameworks contain example paths that need to be updated for your project structure:

```bash
# Example: Update paths in workflow management framework
cd frameworks/workflow-mgmt

# Search for example paths
grep -r "src/confidentia" .

# Replace with your project paths
find . -type f -name "*.md" -exec sed -i '' 's/src\/confidentia/src\/yourproject/g' {} \;
find . -type f -name "*.py" -exec sed -i '' 's/src\/confidentia/src\/yourproject/g' {} \;
```

### 2. Update Version Schema (if needed)

If your project uses a different versioning schema, update the version file:

```bash
# Edit version.py or equivalent
vim frameworks/workflow-mgmt/scripts/validation/validate_branch_context.py

# Update version schema parsing if needed
```

### 3. Configure Framework Settings

Each framework has configuration files that need customization:

```bash
# Example: Workflow management framework
vim frameworks/workflow-mgmt/rw-config.yaml

# Update:
# - Project name
# - Branch patterns
# - File paths
# - Validation settings
```

### 4. Test Installation

Verify the framework is installed correctly:

```bash
# Example: Test workflow management framework
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_branch_context.py --help

# Should show help text without errors
```

---

## Verification

After installation, verify everything is set up correctly:

### 1. Check Framework Files

```bash
# Verify framework directory exists
ls -la frameworks/workflow-mgmt/

# Check for key files
test -f frameworks/workflow-mgmt/README.md && echo "✓ README exists"
test -f frameworks/workflow-mgmt/IMPLEMENTATION_GUIDE.md && echo "✓ Implementation guide exists"
```

### 2. Test Framework Commands

```bash
# Test validation scripts
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_branch_context.py

# Should run without errors (may show warnings if not on correct branch)
```

### 3. Check Git Integration

```bash
# Verify submodule is tracked (if using Git submodules)
git submodule status

# Should show submodule with commit hash
```

---

## Troubleshooting

### Issue: Git submodule not updating

**Problem:** `git submodule update` doesn't pull latest changes.

**Solution:**
```bash
cd .vibe-dev-kit
git fetch origin
git checkout <tag-name>
cd ..
git add .vibe-dev-kit
git commit -m "Update submodule"
```

### Issue: Framework files not found after installation

**Problem:** Framework files are in submodule but not copied to project.

**Solution:**
```bash
# Manually copy framework from submodule
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Or use CLI tool
vibe-dev-kit install workflow-mgmt --force
```

### Issue: Path errors in framework scripts

**Problem:** Framework scripts reference incorrect paths.

**Solution:**
```bash
# Update paths in framework configuration
vim frameworks/workflow-mgmt/rw-config.yaml

# Update all path references to match your project structure
```

### Issue: Version conflicts

**Problem:** Multiple framework versions installed.

**Solution:**
```bash
# Remove old version
rm -rf frameworks/workflow-mgmt

# Install correct version
vibe-dev-kit install workflow-mgmt@2.0.0
```

---

## Next Steps

After installation:

1. **Read the framework README:** `frameworks/<framework-name>/README.md`
2. **Follow the implementation guide:** `frameworks/<framework-name>/IMPLEMENTATION_GUIDE.md`
3. **Configure for your project:** Update paths, version schema, and settings
4. **Test the framework:** Run validation scripts and test workflows
5. **Set up update notifications:** Configure automatic update checking

See the [Usage Guide](framework-dependency-usage-guide.md) for detailed usage instructions.

---

## References

- [Framework Dependency Architecture](../../Architecture/Standards_and_ADRs/framework-dependency-architecture.md)
- [CLI Tool Design](../../Architecture/Standards_and_ADRs/framework-update-cli-design.md)
- [Update Guide](framework-dependency-update-guide.md)
- [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md)

