---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-07T11:40:00Z
expires_at: null
housekeeping_policy: keep
---

# Framework Dependency FAQ

**Status:** Active  
**Version:** 1.0.0  
**Last Updated:** 2025-12-07  
**Epic:** Epic 5 - Documentation Management and Maintenance  
**Story:** Story 4 - Framework Documentation Management  
**Task:** E05:S04:T05 - Create comprehensive user documentation for Epic 6 framework dependency architecture

---

## Overview

Frequently asked questions about installing, updating, and using Vibe Dev Kit frameworks as dependencies.

---

## General Questions

### What is the difference between copy-paste and dependency-based installation?

**Copy-paste:** Frameworks are manually copied into your project. Updates require manually copying new versions. No automatic update mechanism.

**Dependency-based:** Frameworks are installed as dependencies (Git submodules, CLI tool, or package managers). Updates can be automatic or semi-automatic with notifications.

**Benefits of dependency-based:**
- Automatic update notifications
- Version tracking
- Consistent framework versions
- Standard dependency management

### Which installation method should I use?

**Git Submodules (Phase 1):** Use if you want immediate availability, full control, and don't mind manual update steps.

**CLI Tool (Phase 2):** Use if you want a unified interface, automated updates, and easier management. (Coming soon)

**Package Managers (Phase 3):** Use if you prefer standard npm/pip workflows and automatic dependency resolution. (Future)

**Recommendation:** Start with Git submodules, migrate to CLI tool when available.

### Can I use frameworks without installing as dependencies?

Yes. You can still copy-paste frameworks manually. However, you won't get automatic update notifications or version tracking benefits.

### Do I need to install all frameworks?

No. Frameworks are modular. Install only what you need:
- **Workflow Management:** For Release Workflow (RW) automation
- **Kanban:** For project management and work tracking
- **Numbering & Versioning:** For version management

You can use them standalone or together.

---

## Installation Questions

### How do I install frameworks in a new project?

1. Initialize vibe-dev-kit: `vibe-dev-kit init`
2. Install frameworks: `vibe-dev-kit install workflow-mgmt@2.0.0`
3. Configure frameworks: Update paths and settings
4. Test installation: Run validation scripts

See the [Installation Guide](framework-dependency-installation-guide.md) for detailed steps.

### Can I install frameworks in an existing project?

Yes. You can migrate from copy-paste to dependencies:

1. Backup current frameworks
2. Remove copied frameworks
3. Install as dependencies
4. Restore customizations

See the [Integration Guide](framework-dependency-integration-guide.md) for migration steps.

### What are the system requirements?

- **Git** (required for all methods)
- **Python 3.8+** (for CLI tool and frameworks)
- **Node.js 16+** (if using npm package manager)
- Unix-like system (Linux, macOS) or Windows with Git Bash/WSL

### Do I need to update paths after installation?

Yes. Frameworks contain example paths that need to be updated for your project:

```bash
# Find example paths
grep -r "src/confidentia" frameworks/workflow-mgmt/

# Replace with your paths
find . -type f -exec sed -i '' 's/src\/confidentia/src\/yourproject/g' {} \;
```

See the [Usage Guide](framework-dependency-usage-guide.md) for configuration steps.

---

## Update Questions

### How do I know when frameworks are updated?

**CLI Tool:**
```bash
vibe-dev-kit check
```

**Git Submodules:**
```bash
cd .vibe-dev-kit
git fetch origin --tags
git tag | grep workflow-mgmt
```

**Package Managers:**
```bash
npm outdated  # npm
pip list --outdated  # pip
```

You can also configure automatic checking and notifications.

### Should I update immediately when notified?

**PATCH updates (2.0.0 → 2.0.1):** Usually safe to update immediately (bug fixes, security patches).

**MINOR updates (2.0.0 → 2.1.0):** Review changelog, test in development, then update (new features, improvements).

**MAJOR updates (2.0.0 → 3.0.0):** Review breaking changes, plan migration, test thoroughly before updating.

### What if an update breaks my project?

**Rollback:**
```bash
vibe-dev-kit update workflow-mgmt@2.0.0  # Previous version
```

**Or:**
```bash
cd .vibe-dev-kit
git checkout workflow-mgmt-v2.0.0
cd ..
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt
```

Always test updates in a development branch before applying to production.

### Can I pin frameworks to specific versions?

Yes. In `.vibe-dev-kit.yaml`:

```yaml
frameworks:
  workflow-mgmt:
    version: "2.0.0"
    pin: true  # Prevents automatic updates
```

Or use Git tags to pin submodule versions.

---

## Configuration Questions

### Where is the configuration file?

Configuration file: `.vibe-dev-kit.yaml` in your project root.

Framework-specific configuration:
- Workflow Management: `frameworks/workflow-mgmt/rw-config.yaml`
- Kanban: Framework-specific configs in `frameworks/kanban/`

### How do I configure update notifications?

```bash
# Enable automatic checking
vibe-dev-kit config set auto_check true
vibe-dev-kit config set check_interval daily

# Configure notification channel
vibe-dev-kit config set notification_channel console
```

### Can I use different backends for different frameworks?

Yes. Each framework can use a different backend:

```yaml
frameworks:
  workflow-mgmt:
    backend: git-submodule
  kanban:
    backend: npm
```

---

## Version Questions

### What versioning scheme do frameworks use?

Frameworks use **Semantic Versioning (SemVer):** `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes (2.0.0 → 3.0.0)
- **MINOR:** New features, backward compatible (2.0.0 → 2.1.0)
- **PATCH:** Bug fixes, backward compatible (2.0.0 → 2.0.1)

### How do I check framework versions?

```bash
# CLI tool
vibe-dev-kit status

# Git submodules
cd .vibe-dev-kit
git describe --tags

# Package managers
npm list @vibe-dev-kit/workflow-mgmt  # npm
pip show vibe-dev-kit-workflow-mgmt  # pip
```

### What if frameworks have version conflicts?

```bash
# Check compatibility
vibe-dev-kit check-compatibility

# Resolve conflicts
vibe-dev-kit update --resolve-conflicts

# Or update specific framework
vibe-dev-kit update workflow-mgmt@2.1.0
```

---

## Git Submodule Questions

### How do I update Git submodules?

**Manual:**
```bash
cd .vibe-dev-kit
git fetch origin
git checkout workflow-mgmt-v2.1.0
cd ..
cp -r .vibe-dev-kit/packages/frameworks/workflow\ mgt/ ./frameworks/workflow-mgmt
```

**Automated:**
```bash
./scripts/update-frameworks.sh workflow-mgmt 2.1.0
```

### What if submodule is not initialized?

```bash
# Initialize submodules
git submodule update --init --recursive

# Or clone with submodules
git clone --recurse-submodules <repo-url>
```

### Can I use Git subtrees instead of submodules?

Yes. The CLI tool supports Git subtrees:

```bash
vibe-dev-kit install workflow-mgmt --backend git-subtree
```

Subtrees merge framework code directly into your repository (no separate submodule directory).

---

## CLI Tool Questions

### When will the CLI tool be available?

The CLI tool is planned for Phase 2 (short-term). Git submodules (Phase 1) are available now.

### How do I install the CLI tool?

```bash
# Via pip (when available)
pip install vibe-dev-kit

# From source
git clone https://github.com/earlution/vibe-dev-kit.git
cd vibe-dev-kit/cli
pip install -e .
```

### What if CLI command is not found?

```bash
# Check installation
pip show vibe-dev-kit

# Install if missing
pip install vibe-dev-kit

# Check PATH
echo $PATH

# Use Python module
python3 -m vibe_dev_kit install workflow-mgmt
```

---

## Framework Functionality Questions

### How do I use the Release Workflow (RW)?

1. Ensure you're on correct branch: `git branch --show-current`
2. Update version file: `vim src/yourproject/version.py`
3. Type "RW" in your AI assistant (Cursor, GitHub Copilot, etc.)
4. RW executes 14 steps automatically

See the [Usage Guide](framework-dependency-usage-guide.md) for details.

### What if RW fails validation?

```bash
# Check branch context
cd frameworks/workflow-mgmt
python3 scripts/validation/validate_branch_context.py

# Check changelog format
python3 scripts/validation/validate_changelog_format.py

# Fix issues and retry
```

### How do I update Kanban documentation?

```bash
# Run update script
cd frameworks/kanban
python3 scripts/update-kanban-docs.py

# Or use RW (automatically updates Kanban)
# Type "RW" in AI assistant
```

---

## Migration Questions

### How do I migrate from copy-paste to dependencies?

1. Backup current frameworks
2. Document customizations
3. Remove copied frameworks
4. Install as dependencies
5. Restore customizations
6. Test functionality

See the [Integration Guide](framework-dependency-integration-guide.md) for detailed migration steps.

### Will my customizations be lost?

No. Document your customizations before migration, then restore them after installing as dependencies.

**Common customizations:**
- Path updates (src/confidentia → src/yourproject)
- Configuration changes (rw-config.yaml)
- Custom scripts
- Documentation updates

### Can I migrate gradually?

Yes. You can migrate one framework at a time:

1. Migrate workflow-mgmt first
2. Test thoroughly
3. Migrate kanban next
4. Continue with other frameworks

---

## CI/CD Questions

### How do I integrate with CI/CD?

**GitHub Actions:**
```yaml
- name: Check for updates
  run: vibe-dev-kit check --notify
```

**GitLab CI:**
```yaml
check-updates:
  script:
    - vibe-dev-kit check --notify
```

See the [Integration Guide](framework-dependency-integration-guide.md) for complete examples.

### Can I automate framework updates?

Yes, but use with caution:

1. Check for updates automatically
2. Create PR with update
3. Require manual approval
4. Test before merging

See the [Update Guide](framework-dependency-update-guide.md) for update automation.

---

## Troubleshooting Questions

### Framework installation fails. What do I do?

1. Check framework name: `vibe-dev-kit list`
2. Verify version exists: `vibe-dev-kit list --versions`
3. Check network: `git ls-remote https://github.com/earlution/vibe-dev-kit.git`
4. Check permissions: `ls -la frameworks/`
5. Try different backend: `vibe-dev-kit install workflow-mgmt --backend git-submodule`

See the [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md) for detailed solutions.

### Update doesn't work. How do I fix it?

1. Check version availability: `vibe-dev-kit list --versions`
2. Check compatibility: `vibe-dev-kit check --compatibility`
3. Resolve Git conflicts: `git status`
4. Force update: `vibe-dev-kit update workflow-mgmt --force`

See the [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md) for more solutions.

### Configuration errors. How do I fix them?

```bash
# Validate configuration
vibe-dev-kit validate-config

# Auto-fix if possible
vibe-dev-kit validate-config --fix

# Or reinitialize
vibe-dev-kit init
```

---

## Best Practices Questions

### Should I pin framework versions?

**Development:** Pin to specific versions for stability, update regularly for new features.

**Production:** Pin to stable versions, test updates in development first.

```yaml
frameworks:
  workflow-mgmt:
    version: "2.0.0"
    pin: true
```

### How often should I check for updates?

**Recommended:**
- **PATCH updates:** Check weekly, apply immediately
- **MINOR updates:** Check monthly, review and apply quarterly
- **MAJOR updates:** Check quarterly, plan migration

```bash
# Set automatic checking
vibe-dev-kit config set check_interval weekly
```

### Should I commit framework files to Git?

**Git Submodules:** Commit submodule reference, not framework files (they're in submodule).

**CLI Tool/Package Managers:** Framework files are managed by dependency system, commit configuration only.

**Customizations:** Commit your customizations (path updates, config changes).

---

## Support Questions

### Where can I get help?

1. **Documentation:** See guides in `KB/Documentation/User_Docs/`
2. **Troubleshooting Guide:** [framework-dependency-troubleshooting-guide.md](framework-dependency-troubleshooting-guide.md)
3. **GitHub Issues:** Create issue with diagnostic information
4. **CLI Help:** `vibe-dev-kit --help` or `vibe-dev-kit <command> --help`

### How do I report a bug?

```bash
# Use CLI to report
vibe-dev-kit report-issue \
  --framework workflow-mgmt \
  --version 2.0.0 \
  --description "Error description"

# Or create GitHub issue with:
# - Framework name and version
# - Error message
# - Steps to reproduce
# - Diagnostic information
```

### Can I contribute improvements?

Yes. Contributions are welcome:
1. Fork the repository
2. Make changes
3. Test thoroughly
4. Submit pull request

---

## References

- [Installation Guide](framework-dependency-installation-guide.md)
- [Usage Guide](framework-dependency-usage-guide.md)
- [Update Guide](framework-dependency-update-guide.md)
- [Integration Guide](framework-dependency-integration-guide.md)
- [CLI Reference](framework-dependency-cli-reference.md)
- [Troubleshooting Guide](framework-dependency-troubleshooting-guide.md)

