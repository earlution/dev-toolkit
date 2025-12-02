# Packages Directory

This directory contains all packages organized by category.

## Structure

- **`frameworks/`** - Complete, reusable development frameworks
- **`tools/`** - Development tools and utilities
- **`sops/`** - Standard Operating Procedures and workflows

## Adding New Packages

1. **Choose the right category:**
   - **Frameworks** - Complete systems with full documentation (e.g., Release Workflow, Versioning Strategy)
   - **Tools** - Utilities and scripts (e.g., code generators, validators)
   - **SOPs** - Process documentation (e.g., code review procedures, deployment workflows)

2. **Create package directory:**
   ```bash
   mkdir -p packages/{category}/your-package-name
   ```

3. **Follow package structure:**
   - Include `README.md` with overview
   - Include `PACKAGE_OVERVIEW.md` for structure
   - Include `IMPLEMENTATION_GUIDE.md` for step-by-step guide
   - Add version number and update history

4. **Update main README.md** to list your new package

## Package Naming

- Use descriptive, lowercase names
- Use hyphens or spaces for multi-word names
- Be consistent with existing packages

**Examples:**
- `workflow mgt/` (framework)
- `numbering & versioning/` (framework)
- `code-generator/` (tool)
- `deployment-sop/` (SOP)

