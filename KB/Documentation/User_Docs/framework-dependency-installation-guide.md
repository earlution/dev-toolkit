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

This guide explains how to install ai-dev-kit frameworks as dependencies in your project. Frameworks can be installed using three methods: Git submodules (Phase 1), the `ai-dev-kit` CLI tool (Phase 2), or package managers like npm/pip (Phase 3).

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

### Setting Up a Git Repository

If you don't have a Git repository yet, set one up first:

**1. Initialize Local Git Repository:**

```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize Git repository
git init

# Create initial commit (optional but recommended)
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"
```

**2. Create GitHub Repository (Optional but Recommended):**

```bash
# Create repository on GitHub (via web interface or GitHub CLI)
# Then connect local repository to remote:

git remote add origin https://github.com/yourusername/your-project.git

# Or using SSH:
git remote add origin git@github.com:yourusername/your-project.git

# Push initial commit
git branch -M main
git push -u origin main
```

**Note:** You can install frameworks with just a local Git repository. A GitHub (or other remote) repository is optional but recommended for:
- Backup and collaboration
- CI/CD integration
- Framework update notifications (if using GitHub Actions)

**3. Verify Git Setup:**

```bash
# Check Git is working
git --version

# Check repository is initialized
git status

# Check remote (if configured)
git remote -v
```

**Alternative: Use ai-dev-kit as a GitHub Template**

Instead of creating a repository from scratch, you can use `ai-dev-kit` as a template:

**1. Create Repository from Template:**

- Go to [https://github.com/earlution/ai-dev-kit](https://github.com/earlution/ai-dev-kit)
- Click the **"Use this template"** button (if template is enabled)
- Select **"Create a new repository"**
- Choose your repository name and settings
- Click **"Create repository"**

**2. Clone Your New Repository:**

```bash
# Clone your new repository (replace with your username and repo name)
git clone https://github.com/yourusername/your-project.git
cd your-project
```

**3. Post-Template Setup:**

After creating from template, you'll have:
- ✅ Complete `KB/` structure
- ✅ Framework directories (`packages/frameworks/`)
- ✅ Configuration files
- ✅ Example workflows and templates

**Next Steps:**
- Follow the [Post-Template Setup Guide](framework-dependency-post-template-setup-guide.md) for detailed customization steps
- Update `README.md` with your project information
- Review and customize `KB/` structure for your needs
- Configure Release Workflow (RW) for your project

**Note:** If the template option is not available, you can still manually clone and set up:

```bash
# Clone ai-dev-kit
git clone https://github.com/earlution/ai-dev-kit.git your-project
cd your-project

# Remove the original remote and set up your own
git remote remove origin
git remote add origin https://github.com/yourusername/your-project.git

# Push to your repository
git push -u origin main
```

---

## Use Cases

Before installing, identify which use case matches your needs:

### Use Case 1: Template → All Packages
**New project from template with all frameworks included**
- Create repository from ai-dev-kit template
- All frameworks pre-installed
- Complete KB structure included
- See [Use Cases Guide](framework-dependency-use-cases.md#use-case-1-template--all-packages) for details

### Use Case 2: Template → Some Packages
**New project from template with selected frameworks**
- Create repository from ai-dev-kit template
- Remove unused frameworks
- Keep only what you need
- See [Use Cases Guide](framework-dependency-use-cases.md#use-case-2-template--some-packages) for details

### Use Case 3: Existing Project → All Packages
**Install all frameworks into existing project**
- Add all frameworks to your existing repository
- Integrate with current structure
- See [Use Cases Guide](framework-dependency-use-cases.md#use-case-3-existing-project--all-packages) for details

### Use Case 4: Existing Project → Some Packages
**Install selected frameworks into existing project**
- Add only the frameworks you need
- Incremental adoption
- See [Use Cases Guide](framework-dependency-use-cases.md#use-case-4-existing-project--some-packages) for details

**📖 For complete use case details and additional scenarios, see the [Use Cases Guide](framework-dependency-use-cases.md)**

---

## Installation Methods

### Method 1: Git Submodules (Phase 1 - Available Now)

Git submodules allow you to include the ai-dev-kit repository (or specific frameworks) as a subdirectory in your project, with version control via Git tags.

#### Installation Steps

**1. Ensure Git repository is initialized:**

```bash
# Navigate to your project root
cd /path/to/your/project

# If not already a Git repository, initialize it
git init  # Only if needed

# Verify Git is set up
git status
```

**2. Add the ai-dev-kit repository as a submodule:**

```bash
# Add the entire ai-dev-kit repository as a submodule
git submodule add https://github.com/earlution/ai-dev-kit.git .ai-dev-kit

# Or add to a specific directory
git submodule add https://github.com/earlution/ai-dev-kit.git frameworks/ai-dev-kit
```

**3. Checkout a specific framework version (recommended):**

```bash
# Navigate to the submodule
cd .ai-dev-kit

# List available framework tags
git tag | grep framework

# Checkout a specific framework version (e.g., workflow-mgmt-v2.0.0)
git checkout workflow-mgmt-v2.0.0

# Return to project root
cd ..
```

**4. Copy the framework to your project structure:**

```bash
# Copy the workflow management framework
cp -r .ai-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Or copy multiple frameworks
cp -r .ai-dev-kit/packages/frameworks/kanban/ ./frameworks/kanban
cp -r ".ai-dev-kit/packages/frameworks/numbering & versioning" ./frameworks/numbering-versioning
```

**5. Commit the submodule reference:**

```bash
git add .gitmodules .ai-dev-kit frameworks/
git commit -m "Add ai-dev-kit frameworks as Git submodule"
```

#### Updating Frameworks (Git Submodules)

**Check for updates:**

```bash
# Navigate to submodule
cd .ai-dev-kit

# Fetch latest changes
git fetch origin

# List new tags
git tag | grep framework

# Checkout new version
git checkout workflow-mgmt-v2.1.0

# Return to project root
cd ..

# Copy updated framework
cp -r .ai-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Commit update
git add frameworks/
git commit -m "Update workflow-mgmt framework to v2.1.0"
```

**Automated update script:**

Create `scripts/update-frameworks.sh`:

```bash
#!/bin/bash
# Update all frameworks from Git submodule

cd .ai-dev-kit
git fetch origin
git checkout workflow-mgmt-v2.1.0  # Update to desired version
cd ..

# Copy updated frameworks
cp -r .ai-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt
cp -r .ai-dev-kit/packages/frameworks/kanban/ ./frameworks/kanban

echo "Frameworks updated. Review changes and commit."
```

#### Advantages of Git Submodules

- **Version control:** Pin frameworks to specific Git tags
- **No external dependencies:** Works with Git only
- **Explicit updates:** You control when to update
- **Full access:** Access to entire ai-dev-kit repository

#### Limitations of Git Submodules

- **Manual updates:** Requires manual copying after submodule update
- **Git knowledge:** Requires understanding of Git submodules
- **Repository size:** Includes entire ai-dev-kit repository

---

### Method 2: CLI Tool (Phase 2 - Coming Soon)

The `ai-dev-kit` CLI tool provides a unified interface for installing and managing frameworks across all dependency backends.

#### Installation Steps

**1. Ensure Git repository is initialized:**

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize Git if needed
git init  # Only if not already a Git repository
```

**2. Install the CLI tool:**

```bash
# Install via pip
pip install ai-dev-kit

# Or install from source
git clone https://github.com/earlution/ai-dev-kit.git
cd ai-dev-kit
pip install -e .
```

**3. Initialize ai-dev-kit in your project:**

```bash
cd /path/to/your/project
ai-dev-kit init
```

This creates a `.ai-dev-kit.yaml` configuration file:

```yaml
project_root: .
frameworks_dir: ./frameworks
backend: git_submodule  # or 'npm', 'pip'
auto_update: false
```

**4. Install a framework:**

```bash
# Install workflow management framework
ai-dev-kit install workflow-mgmt

# Install specific version
ai-dev-kit install workflow-mgmt@2.0.0

# Install multiple frameworks
ai-dev-kit install workflow-mgmt kanban numbering-versioning
```

**5. Check installed frameworks:**

```bash
ai-dev-kit status
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
ai-dev-kit check
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
ai-dev-kit update workflow-mgmt

# Update all frameworks
ai-dev-kit update --all

# Update to specific version
ai-dev-kit update workflow-mgmt@2.1.0
```

**Automatic update notifications:**

The CLI tool can be configured to check for updates and notify you:

```bash
# Enable automatic update checks
ai-dev-kit config set auto_check true
ai-dev-kit config set check_interval daily

# Run update check (can be added to CI/CD)
ai-dev-kit check --notify
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

**1. Ensure Git repository is initialized:**

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize Git if needed
git init  # Only if not already a Git repository
```

**2. Install workflow management framework:**

```bash
# Install workflow management framework
npm install @ai-dev-kit/workflow-mgmt

# Install specific version
npm install @ai-dev-kit/workflow-mgmt@2.0.0

# Install multiple frameworks
npm install @ai-dev-kit/workflow-mgmt @ai-dev-kit/kanban
```

#### Installation Steps (pip - Future)

**1. Ensure Git repository is initialized:**

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize Git if needed
git init  # Only if not already a Git repository
```

**2. Install workflow management framework:**

```bash
# Install workflow management framework
pip install ai-dev-kit-workflow-mgmt

# Install specific version
pip install ai-dev-kit-workflow-mgmt==2.0.0

# Install multiple frameworks
pip install ai-dev-kit-workflow-mgmt ai-dev-kit-kanban
```

**Note:** While package managers (npm/pip) don't strictly require Git, having a Git repository is still recommended for:
- Version control of your project
- Tracking framework versions
- CI/CD integration
- Framework update workflows

#### Updating Frameworks (Package Managers)

**npm:**

```bash
# Check for updates
npm outdated

# Update to latest compatible version
npm update @ai-dev-kit/workflow-mgmt

# Update to specific version
npm install @ai-dev-kit/workflow-mgmt@2.1.0
```

**pip:**

```bash
# Check for updates
pip list --outdated

# Update to latest version
pip install --upgrade ai-dev-kit-workflow-mgmt

# Update to specific version
pip install --upgrade ai-dev-kit-workflow-mgmt==2.1.0
```

#### Advantages of Package Managers

- **Standard workflow:** Uses familiar package manager commands
- **Dependency resolution:** Automatic dependency management
- **Version locking:** `package.json` or `requirements.txt` pin versions
- **CI/CD integration:** Standard package manager workflows

---

## Post-Installation Setup

### Enable RW Trigger in `.cursorrules` (Workflow Management Framework)

**⚠️ IMPORTANT:** If you installed the Workflow Management framework, you need to add the RW trigger section to your `.cursorrules` file to enable the "RW" command in Cursor.

**Option A: Use the RW Installer (Recommended)**

The RW installer can automatically generate and add the `.cursorrules` section:

```bash
# Navigate to your project root
cd /path/to/your/project

# Run the RW installer
python frameworks/workflow-mgmt/scripts/install_release_workflow.py

# The installer will:
# - Generate rw-config.yaml (if it doesn't exist)
# - Create or update .cursorrules with the RW trigger section
# - Update workflow YAML files with correct paths
```

**Option B: Manual Setup**

If you prefer to set it up manually:

1. **Open the cursorrules template:**
   ```bash
   # View the template
   cat frameworks/workflow-mgmt/cursorrules-rw-trigger-section.md
   ```

2. **Copy the RW trigger section:**
   - Copy everything from `### 🚀 RELEASE WORKFLOW (RW) TRIGGER` to the end of the file
   - This is the section that enables the "RW" command

3. **Add to your `.cursorrules` file:**
   ```bash
   # Create .cursorrules if it doesn't exist
   touch .cursorrules
   
   # Add the RW trigger section (paste the copied content)
   # You can add it in a "Version Control and Release Process" section
   ```

4. **Update file paths in the section:**
   - Replace `{project}` with your project name
   - Update version file path: `src/{project}/version.py` → `src/yourproject/version.py`
   - Update Kanban paths if using Kanban framework
   - Update validator script paths to match your framework location

5. **Verify the trigger works:**
   - Restart Cursor to reload `.cursorrules`
   - Type "RW" in Cursor chat
   - The agent should recognize the trigger and execute the Release Workflow

**What the RW Trigger Does:**

When you type "RW" or "rw" in Cursor, the AI assistant will:
- Execute the complete 14-step Release Workflow
- Bump version, update changelogs, commit, tag, and push
- Update Kanban documentation automatically
- Validate everything before committing

**Without `.cursorrules`:** The "RW" command won't work - you'll need to manually run the workflow steps.

**With `.cursorrules`:** The "RW" command triggers intelligent agent-driven execution of the complete workflow.

---

## Post-Installation Setup (Other Frameworks)

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

### 4. Enable RW Trigger in `.cursorrules` (Workflow Management Framework Only)

**⚠️ IMPORTANT:** If you installed the Workflow Management framework, you need to add the RW trigger section to your `.cursorrules` file to enable the "RW" command in Cursor.

**Option A: Use the RW Installer (Recommended)**

The RW installer can automatically generate and add the `.cursorrules` section:

```bash
# Navigate to your project root
cd /path/to/your/project

# Run the RW installer
python frameworks/workflow-mgmt/scripts/install_release_workflow.py

# The installer will:
# - Generate rw-config.yaml (if it doesn't exist)
# - Create or update .cursorrules with the RW trigger section
# - Update workflow YAML files with correct paths
```

**Option B: Manual Setup**

If you prefer to set it up manually:

1. **Open the cursorrules template:**
   ```bash
   # View the template
   cat frameworks/workflow-mgmt/cursorrules-rw-trigger-section.md
   ```

2. **Copy the RW trigger section:**
   - Copy everything from `### 🚀 RELEASE WORKFLOW (RW) TRIGGER` to the end of the file
   - This is the section that enables the "RW" command

3. **Add to your `.cursorrules` file:**
   ```bash
   # Create .cursorrules if it doesn't exist
   touch .cursorrules
   
   # Add the RW trigger section (paste the copied content)
   # You can add it in a "Version Control and Release Process" section
   ```

4. **Update file paths in the section:**
   - Replace `{project}` with your project name
   - Update version file path: `src/{project}/version.py` → `src/yourproject/version.py`
   - Update Kanban paths if using Kanban framework
   - Update validator script paths to match your framework location

5. **Verify the trigger works:**
   - Restart Cursor to reload `.cursorrules`
   - Type "RW" in Cursor chat
   - The agent should recognize the trigger and execute the Release Workflow

**What the RW Trigger Does:**

When you type "RW" or "rw" in Cursor, the AI assistant will:
- Execute the complete 14-step Release Workflow
- Bump version, update changelogs, commit, tag, and push
- Update Kanban documentation automatically
- Validate everything before committing

**Without `.cursorrules`:** The "RW" command won't work - you'll need to manually run the workflow steps.

**With `.cursorrules`:** The "RW" command triggers intelligent agent-driven execution of the complete workflow.

**Location of Template:**
- `frameworks/workflow-mgmt/cursorrules-rw-trigger-section.md`

### 5. Test Installation

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
# Verify Git repository is initialized
git status
# Should show repository status (not "not a git repository")

# Verify submodule is tracked (if using Git submodules)
git submodule status
# Should show submodule with commit hash

# Check remote (if configured)
git remote -v
# Shows remote repository URL if configured
```

---

## Troubleshooting

### Issue: Not a Git repository

**Problem:** `git status` shows "not a git repository" error.

**Solution:**
```bash
# Initialize Git repository
git init

# Create initial commit
git add .
git commit -m "Initial commit"

# Then proceed with framework installation
```

**Note:** You can install frameworks without a remote repository (GitHub). A local Git repository is sufficient for framework installation.

### Issue: Git submodule not updating

**Problem:** `git submodule update` doesn't pull latest changes.

**Solution:**
```bash
cd .ai-dev-kit
git fetch origin
git checkout <tag-name>
cd ..
git add .ai-dev-kit
git commit -m "Update submodule"
```

### Issue: Framework files not found after installation

**Problem:** Framework files are in submodule but not copied to project.

**Solution:**
```bash
# Manually copy framework from submodule
cp -r .ai-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt

# Or use CLI tool
ai-dev-kit install workflow-mgmt --force
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
ai-dev-kit install workflow-mgmt@2.0.0
```

---

## Next Steps

After installation:

1. **Read the framework README:** `frameworks/<framework-name>/README.md`
2. **Follow the implementation guide:** `frameworks/<framework-name>/IMPLEMENTATION_GUIDE.md`
3. **Configure for your project:** Update paths, version schema, and settings
4. **Set up `.cursorrules` for RW trigger (Workflow Management Framework only):**
   - If you installed the Workflow Management framework, you need to add the RW trigger section to your `.cursorrules` file
   - **Location:** `frameworks/workflow-mgmt/cursorrules-rw-trigger-section.md`
   - **Instructions:** Copy the section from that file into your project's `.cursorrules` file
   - **Alternative:** Use the RW installer script which can generate it automatically:
     ```bash
     python frameworks/workflow-mgmt/scripts/install_release_workflow.py
     ```
   - **Note:** Without the `.cursorrules` section, the "RW" trigger won't work in Cursor
5. **Test the framework:** Run validation scripts and test workflows
6. **Set up update notifications:** Configure automatic update checking

See the [Usage Guide](framework-dependency-usage-guide.md) for detailed usage instructions.

---

## References

- [Framework Dependency Architecture](../../Architecture/Standards_and_ADRs/framework-dependency-architecture.md)
- [CLI Tool Design](../../Architecture/Standards_and_ADRs/framework-update-cli-design.md)
- [Update Guide](framework-dependency-update-guide.md)
- [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md)

