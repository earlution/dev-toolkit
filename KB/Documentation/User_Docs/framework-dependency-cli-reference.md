---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-07T11:30:00Z
expires_at: null
housekeeping_policy: keep
---

# Framework Dependency CLI Reference

**Status:** Active  
**Version:** 1.0.0  
**Last Updated:** 2025-12-07  
**Epic:** Epic 5 - Documentation Management and Maintenance  
**Story:** Story 4 - Framework Documentation Management  
**Task:** E05:S04:T05 - Create comprehensive user documentation for Epic 6 framework dependency architecture

---

## Overview

This document provides a complete reference for the `vibe-dev-kit` CLI tool commands. The CLI tool provides a unified interface for managing framework dependencies across all backends (Git submodules, package managers).

**Installation:**

```bash
# Install via pip
pip install vibe-dev-kit

# Or from source
git clone https://github.com/earlution/vibe-dev-kit.git
cd vibe-dev-kit/cli
pip install -e .
```

---

## Core Commands

### `vibe-dev-kit init`

Initialize vibe-dev-kit in your project.

**Usage:**

```bash
vibe-dev-kit init [--path <path>] [--backend <backend>]
```

**Options:**
- `--path <path>` - Project root directory (default: current directory)
- `--backend <backend>` - Default dependency backend (git-submodule, npm, pip)

**Example:**

```bash
# Initialize in current directory
vibe-dev-kit init

# Initialize with specific backend
vibe-dev-kit init --backend git-submodule
```

**Creates:**
- `.vibe-dev-kit.yaml` - Configuration file

---

### `vibe-dev-kit install`

Install a framework as a dependency.

**Usage:**

```bash
vibe-dev-kit install <framework>[@version] [options]
```

**Arguments:**
- `<framework>` - Framework name (required)
- `[@version]` - Specific version (optional, defaults to latest)

**Options:**
- `--backend <type>` - Dependency backend (git-submodule, git-subtree, npm, pip)
- `--path <path>` - Custom installation path
- `--dry-run` - Preview changes without applying

**Examples:**

```bash
# Install latest version
vibe-dev-kit install workflow-mgmt

# Install specific version
vibe-dev-kit install workflow-mgmt@2.0.0

# Install multiple frameworks
vibe-dev-kit install workflow-mgmt@2.0.0 kanban@1.0.0 numbering-versioning@2.0.0

# Install with specific backend
vibe-dev-kit install workflow-mgmt --backend git-submodule

# Preview installation
vibe-dev-kit install workflow-mgmt --dry-run
```

**Behavior:**
- Detects project type and suggests appropriate backend
- Creates `.vibe-dev-kit.yaml` if it doesn't exist
- Installs framework using selected backend
- Updates project configuration files
- Validates installation

**Output:**

```
Installing workflow-mgmt@2.0.0...
  Backend: git-submodule
  Path: frameworks/workflow-mgmt
  Status: ✓ Installed successfully

Framework installed:
  Name: workflow-mgmt
  Version: 2.0.0
  Backend: git-submodule
  Path: frameworks/workflow-mgmt
```

---

### `vibe-dev-kit update`

Update a framework to the latest compatible version.

**Usage:**

```bash
vibe-dev-kit update <framework>[@version] [options]
```

**Arguments:**
- `<framework>` - Framework name (required)
- `[@version]` - Specific version to update to (optional)

**Options:**
- `--all` - Update all installed frameworks
- `--check` - Check for updates without applying
- `--dry-run` - Preview updates without applying
- `--force` - Force update even if conflicts detected
- `--pin` - Pin to specific version after update

**Examples:**

```bash
# Update to latest compatible version
vibe-dev-kit update workflow-mgmt

# Update to specific version
vibe-dev-kit update workflow-mgmt@2.1.0

# Update all frameworks
vibe-dev-kit update --all

# Check for updates without applying
vibe-dev-kit update workflow-mgmt --check

# Preview update
vibe-dev-kit update workflow-mgmt --dry-run

# Force update
vibe-dev-kit update workflow-mgmt --force
```

**Behavior:**
- Checks for available updates
- Validates compatibility
- Updates framework using appropriate backend
- Updates `.vibe-dev-kit.yaml` configuration
- Runs post-update validation

**Output:**

```
Updating workflow-mgmt...
  Current: 2.0.0
  Latest:  2.1.0
  Type:    MINOR
  Status:  ✓ Updated successfully

Framework updated:
  Name: workflow-mgmt
  Version: 2.0.0 → 2.1.0
  Backend: git-submodule
  Path: frameworks/workflow-mgmt
```

---

### `vibe-dev-kit check`

Check for available framework updates.

**Usage:**

```bash
vibe-dev-kit check [<framework>] [options]
```

**Arguments:**
- `<framework>` - Specific framework to check (optional, checks all if omitted)

**Options:**
- `--notify` - Show notification-style output
- `--compatibility` - Check compatibility information
- `--json` - Output in JSON format

**Examples:**

```bash
# Check all frameworks
vibe-dev-kit check

# Check specific framework
vibe-dev-kit check workflow-mgmt

# Check with notifications
vibe-dev-kit check --notify

# Check compatibility
vibe-dev-kit check --compatibility

# JSON output
vibe-dev-kit check --json
```

**Output:**

```
Framework: workflow-mgmt
  Current: 2.0.0
  Latest:  2.1.0
  Type:    MINOR
  Status:  Update available
  Breaking: None

Framework: kanban
  Current: 1.0.0
  Latest:  1.0.0
  Status:  Up to date
```

---

### `vibe-dev-kit status`

Show status of installed frameworks.

**Usage:**

```bash
vibe-dev-kit status [<framework>] [options]
```

**Arguments:**
- `<framework>` - Specific framework to show (optional, shows all if omitted)

**Options:**
- `--json` - Output in JSON format
- `--verbose` - Show detailed information

**Examples:**

```bash
# Show all frameworks
vibe-dev-kit status

# Show specific framework
vibe-dev-kit status workflow-mgmt

# JSON output
vibe-dev-kit status --json

# Verbose output
vibe-dev-kit status --verbose
```

**Output:**

```
Installed Frameworks:
  workflow-mgmt:
    Version: 2.0.0
    Backend: git-submodule
    Path: frameworks/workflow-mgmt
    Status: Update available (2.1.0)
  
  kanban:
    Version: 1.0.0
    Backend: git-submodule
    Path: frameworks/kanban
    Status: Up to date
```

---

### `vibe-dev-kit list`

List available frameworks.

**Usage:**

```bash
vibe-dev-kit list [options]
```

**Options:**
- `--versions` - Show available versions
- `--json` - Output in JSON format

**Examples:**

```bash
# List all frameworks
vibe-dev-kit list

# List with versions
vibe-dev-kit list --versions

# JSON output
vibe-dev-kit list --json
```

**Output:**

```
Available Frameworks:
  workflow-mgmt:
    Versions: 2.0.0, 2.1.0
    Description: AI-driven release and workflow automation
  
  kanban:
    Versions: 1.0.0
    Description: Kanban system implementation
  
  numbering-versioning:
    Versions: 2.0.0, 2.1.0
    Description: Numbering and versioning framework
```

---

### `vibe-dev-kit remove`

Remove a framework dependency.

**Usage:**

```bash
vibe-dev-kit remove <framework> [options]
```

**Arguments:**
- `<framework>` - Framework name (required)

**Options:**
- `--keep-files` - Keep framework files but remove dependency tracking

**Examples:**

```bash
# Remove framework
vibe-dev-kit remove workflow-mgmt

# Remove but keep files
vibe-dev-kit remove workflow-mgmt --keep-files
```

**Behavior:**
- Removes framework from `.vibe-dev-kit.yaml`
- Removes framework files (unless `--keep-files`)
- Updates project configuration

---

## Configuration Commands

### `vibe-dev-kit config`

Manage CLI configuration.

**Usage:**

```bash
vibe-dev-kit config <command> [options]
```

**Commands:**
- `get <key>` - Get configuration value
- `set <key> <value>` - Set configuration value
- `list` - List all configuration
- `reset` - Reset to defaults

**Examples:**

```bash
# Get configuration value
vibe-dev-kit config get default_backend

# Set configuration value
vibe-dev-kit config set default_backend git-submodule
vibe-dev-kit config set auto_check true
vibe-dev-kit config set check_interval daily

# List all configuration
vibe-dev-kit config list

# Reset to defaults
vibe-dev-kit config reset
```

**Configuration Keys:**
- `default_backend` - Default dependency backend
- `auto_check` - Enable automatic update checking (true/false)
- `check_interval` - Update check interval (daily/weekly/manual)
- `notification_channel` - Notification channel (console/email/slack)
- `update_policy.patch` - Patch update policy (auto/notify/manual)
- `update_policy.minor` - Minor update policy (auto/notify/manual)
- `update_policy.major` - Major update policy (auto/notify/manual)

---

## Information Commands

### `vibe-dev-kit changelog`

View framework changelog.

**Usage:**

```bash
vibe-dev-kit changelog <framework> [options]
```

**Arguments:**
- `<framework>` - Framework name (required)

**Options:**
- `--from <version>` - Show changes from version
- `--to <version>` - Show changes to version
- `--breaking` - Show only breaking changes
- `--config` - Show configuration changes

**Examples:**

```bash
# Show full changelog
vibe-dev-kit changelog workflow-mgmt

# Show changes between versions
vibe-dev-kit changelog workflow-mgmt --from 2.0.0 --to 2.1.0

# Show only breaking changes
vibe-dev-kit changelog workflow-mgmt --breaking

# Show configuration changes
vibe-dev-kit changelog workflow-mgmt --config
```

---

### `vibe-dev-kit deps`

Show framework dependencies.

**Usage:**

```bash
vibe-dev-kit deps <framework>
```

**Arguments:**
- `<framework>` - Framework name (required)

**Example:**

```bash
vibe-dev-kit deps workflow-mgmt
```

**Output:**

```
Framework: workflow-mgmt
Dependencies:
  numbering-versioning: >=2.0.0
  kanban: >=1.0.0
```

---

### `vibe-dev-kit check-compatibility`

Check framework compatibility.

**Usage:**

```bash
vibe-dev-kit check-compatibility [options]
```

**Options:**
- `--json` - Output in JSON format

**Example:**

```bash
vibe-dev-kit check-compatibility
```

**Output:**

```
Framework Compatibility:
  workflow-mgmt@2.0.0: ✓ Compatible
  kanban@1.0.0: ✓ Compatible
  numbering-versioning@2.0.0: ✓ Compatible
```

---

## Utility Commands

### `vibe-dev-kit validate-config`

Validate configuration files.

**Usage:**

```bash
vibe-dev-kit validate-config [options]
```

**Options:**
- `--fix` - Automatically fix issues

**Example:**

```bash
# Validate configuration
vibe-dev-kit validate-config

# Validate and fix
vibe-dev-kit validate-config --fix
```

---

### `vibe-dev-kit migrate`

Migrate from copy-paste to dependencies.

**Usage:**

```bash
vibe-dev-kit migrate [options]
```

**Options:**
- `--detect` - Detect existing frameworks
- `--convert` - Convert to dependencies
- `--dry-run` - Preview migration

**Examples:**

```bash
# Detect existing frameworks
vibe-dev-kit migrate --detect

# Convert to dependencies
vibe-dev-kit migrate --convert

# Preview migration
vibe-dev-kit migrate --convert --dry-run
```

---

## Global Options

All commands support these global options:

- `--help` - Show command help
- `--version` - Show CLI version
- `--verbose` - Verbose output
- `--quiet` - Quiet output (errors only)
- `--config <path>` - Use custom config file

**Examples:**

```bash
# Show help
vibe-dev-kit install --help

# Show version
vibe-dev-kit --version

# Verbose output
vibe-dev-kit check --verbose

# Use custom config
vibe-dev-kit status --config /path/to/config.yaml
```

---

## Configuration File

### `.vibe-dev-kit.yaml`

Configuration file for framework dependencies.

**Location:** Project root directory

**Structure:**

```yaml
version: "1.0.0"
default_backend: "git-submodule"

update_policy:
  patch: auto      # auto, notify, manual
  minor: notify
  major: manual

auto_check: true
check_interval: daily  # daily, weekly, manual

notification_channel: console  # console, email, slack

frameworks:
  workflow-mgmt:
    version: "2.0.0"
    backend: "git-submodule"
    path: "frameworks/workflow-mgmt"
    source: "https://github.com/earlution/vibe-dev-kit.git"
    tag: "workflow-mgmt-v2.0.0"
    pin: false
```

**Fields:**
- `version` - Configuration file version
- `default_backend` - Default dependency backend
- `update_policy` - Update policies by version type
- `auto_check` - Enable automatic update checking
- `check_interval` - Update check frequency
- `notification_channel` - Notification method
- `frameworks` - Installed frameworks configuration
  - `version` - Framework version
  - `backend` - Dependency backend used
  - `path` - Installation path
  - `source` - Source repository URL
  - `tag` - Git tag (for Git backends)
  - `pin` - Pin to version (prevent auto-updates)

---

## Error Codes

CLI commands return exit codes:

- `0` - Success
- `1` - General error
- `2` - Framework not found
- `3` - Version not found
- `4` - Backend not available
- `5` - Configuration error
- `6` - Update conflict
- `7` - Validation error

**Example Error Handling:**

```bash
if vibe-dev-kit install workflow-mgmt; then
  echo "Installation successful"
else
  exit_code=$?
  case $exit_code in
    2) echo "Framework not found" ;;
    3) echo "Version not found" ;;
    4) echo "Backend not available" ;;
    *) echo "Installation failed" ;;
  esac
fi
```

---

## Examples

### Complete Workflow

```bash
# Initialize project
vibe-dev-kit init

# Install frameworks
vibe-dev-kit install workflow-mgmt@2.0.0
vibe-dev-kit install kanban@1.0.0

# Check status
vibe-dev-kit status

# Check for updates
vibe-dev-kit check

# Update framework
vibe-dev-kit update workflow-mgmt@2.1.0

# Verify update
vibe-dev-kit status workflow-mgmt
```

### CI/CD Integration

```bash
# In CI/CD pipeline
vibe-dev-kit check --notify

# If updates available, create issue
if [ $? -ne 0 ]; then
  # Create GitHub issue or send notification
fi
```

### Migration

```bash
# Detect existing frameworks
vibe-dev-kit migrate --detect

# Preview migration
vibe-dev-kit migrate --convert --dry-run

# Execute migration
vibe-dev-kit migrate --convert
```

---

## Troubleshooting

### Common Issues

**Command not found:**

```bash
# Check installation
pip show vibe-dev-kit

# Reinstall if needed
pip install --upgrade vibe-dev-kit
```

**Configuration not found:**

```bash
# Initialize project
vibe-dev-kit init

# Or specify config file
vibe-dev-kit status --config /path/to/config.yaml
```

**Backend not available:**

```bash
# Check available backends
vibe-dev-kit list --backends

# Use different backend
vibe-dev-kit install workflow-mgmt --backend git-submodule
```

See the [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md) for more detailed solutions.

---

## References

- [Installation Guide](framework-dependency-installation-guide.md)
- [Usage Guide](framework-dependency-usage-guide.md)
- [Update Guide](framework-dependency-update-guide.md)
- [Integration Guide](framework-dependency-integration-guide.md)
- [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md)

