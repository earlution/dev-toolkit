# Tool Template Guide

This directory contains a template structure for creating new tools in the dev-toolkit repository.

## Quick Start

1. **Copy the template:**
   ```bash
   cp -r tools/_template tools/your-tool-name
   ```

2. **Rename files:**
   ```bash
   cd tools/your-tool-name
   mv tool_name.py your_tool_name.py
   ```

3. **Update template placeholders:**
   - Replace `Tool Name` with your actual tool name
   - Replace `tool_name` with your actual tool name (snake_case)
   - Update descriptions and documentation
   - Add your implementation code

4. **Update requirements.txt:**
   - Add any Python dependencies your tool needs

5. **Add to main README:**
   - Update `README.md` in the root to include your new tool

6. **Test your tool:**
   ```bash
   python3 your_tool_name.py --help
   ```

## Template Structure

```
_template/
├── README.md              # Tool documentation (required)
├── tool_name.py           # Main tool script (required)
├── requirements.txt       # Python dependencies (required)
├── .gitignore            # Git ignore rules (optional)
├── TEMPLATE_GUIDE.md     # This file
└── examples/             # Example files/scripts (optional)
```

## File Descriptions

### README.md
- **Purpose:** User-facing documentation
- **Required:** Yes
- **Content:** Overview, installation, usage, examples, troubleshooting
- **Format:** Markdown

### tool_name.py
- **Purpose:** Main executable script
- **Required:** Yes
- **Content:** Tool implementation
- **Format:** Python 3.7+ with shebang (`#!/usr/bin/env python3`)
- **Requirements:**
  - Use `argparse` for CLI
  - Include `--help` option
  - Include `--dry-run` option (if applicable)
  - Include `--verbose` option (if applicable)
  - Proper error handling
  - Exit codes: 0 for success, non-zero for errors

### requirements.txt
- **Purpose:** Python dependencies
- **Required:** Yes (even if empty)
- **Content:** One dependency per line with version specifiers
- **Format:** pip requirements format

### .gitignore
- **Purpose:** Ignore tool-specific files
- **Required:** No (but recommended)
- **Content:** Python, IDE, OS, and tool-specific ignores

### examples/
- **Purpose:** Example files, sample data, or usage examples
- **Required:** No
- **Content:** Any example files that help users understand the tool

## Best Practices

### Code Quality
- ✅ Use type hints where possible
- ✅ Include docstrings for functions
- ✅ Follow PEP 8 style guide
- ✅ Handle errors gracefully
- ✅ Provide clear error messages

### Documentation
- ✅ Clear, concise descriptions
- ✅ Usage examples for common scenarios
- ✅ Troubleshooting section for common issues
- ✅ Link to related tools or resources

### User Experience
- ✅ Provide `--help` option
- ✅ Use `--dry-run` for destructive operations
- ✅ Use `--verbose` for detailed output
- ✅ Clear, actionable error messages
- ✅ Progress indicators for long operations

### Testing
- ✅ Test with different inputs
- ✅ Test error cases
- ✅ Test edge cases
- ✅ Document known limitations

## Naming Conventions

- **Directory:** `kebab-case` (e.g., `github-badges`)
- **Python file:** `snake_case.py` (e.g., `update_badges.py`)
- **Tool name in docs:** `Title Case` (e.g., `GitHub Badges`)

## Checklist

Before submitting a new tool:

- [ ] Tool works as documented
- [ ] README.md is complete and accurate
- [ ] requirements.txt includes all dependencies
- [ ] Code follows Python best practices
- [ ] Error handling is implemented
- [ ] Tool is added to main README.md
- [ ] Examples are provided (if applicable)
- [ ] Tool is tested on target platforms

## Questions?

See the main [CONTRIBUTING.md](../../CONTRIBUTING.md) or open an issue on GitHub.

