# Contributing to Dev Toolkit

Thank you for your interest in contributing to Dev Toolkit! We welcome contributions from the community.

## How to Submit Feedback

You can submit Bug Reports, Feature Requests, or User Experience Research (UXR) reports directly through GitHub Issues. No repository access required!

### Quick Start

1. **Go to [GitHub Issues](https://github.com/earlution/ai-dev-kit/issues)**
2. **Click "New Issue"**
3. **Choose a template:**
   - 🐛 **Bug Report** - Report a bug or issue
   - ✨ **Feature Request** - Suggest a new feature
   - 🔬 **User Experience Research (UXR)** - Submit UX research findings

4. **Fill out the form** - All templates guide you through what information to provide
5. **Submit** - Your issue will be automatically processed!

### What Happens Next?

- ✅ Your submission is automatically converted to a Kanban document
- ✅ A task is created and tracked in our project management system
- ✅ You'll receive updates via GitHub Issue comments
- ✅ Your submission is linked bidirectionally between GitHub and our Kanban system

## Detailed Guides

For more detailed information on submitting reports, see:

- **[GitHub Submission Guide](packages/frameworks/kanban/FR_BR_UXR_GITHUB_SUBMISSION_GUIDE.md)** - Complete guide with examples and best practices
- **[Bug Report Guide](.github/ISSUE_TEMPLATE/bug_report.yml)** - What to include in bug reports
- **[Feature Request Guide](.github/ISSUE_TEMPLATE/feature_request.yml)** - How to write effective feature requests
- **[UX Research Guide](.github/ISSUE_TEMPLATE/ux_research.yml)** - Submitting UX research findings

## Contributing Tools

### Adding a New Tool

1. **Use the template:**
   ```bash
   cp -r tools/_template tools/your-tool-name
   cd tools/your-tool-name
   ```

2. **Implement your tool:**
   - Follow the [Template Guide](tools/_template/TEMPLATE_GUIDE.md)
   - Keep your tool completely self-contained (no dependencies on other tools)
   - Document everything in README.md

3. **Register your tool:**
   ```bash
   python3 tools/manage_tools.py update-registry
   ```

4. **Validate:**
   ```bash
   python3 tools/manage_tools.py validate
   ```

5. **Update main README.md** with your tool entry

6. **Commit and push:**
   ```bash
   git add tools/your-tool-name tools/tools-registry.yaml README.md
   git commit -m "Add your-tool-name tool"
   git push origin your-branch
   ```

### Tool Management

See [Tool Management Guide](tools/TOOL_MANAGEMENT.md) for:
- Management principles and philosophy
- Registry system
- Validation workflows
- Separation of concerns

**Key Principle:** Each tool is completely independent. No shared code, dependencies, or runtime interactions between tools.

## Code Contributions

If you'd like to contribute code to existing tools:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test thoroughly** (test the specific tool independently)
5. **Validate tool structure:**
   ```bash
   python3 tools/manage_tools.py validate
   ```
6. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
7. **Push to the branch** (`git push origin feature/AmazingFeature`)
8. **Open a Pull Request**

## Questions?

- **Tool Management:** See [Tool Management Guide](tools/TOOL_MANAGEMENT.md)
- **Tool Template:** See [Template Guide](tools/_template/TEMPLATE_GUIDE.md)
- **Issues:** Check existing [GitHub Issues](https://github.com/earlution/dev-toolkit/issues) or create a new one
- **Discussions:** Use GitHub Discussions for questions and community discussions

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

---

**Thank you for contributing to Dev Toolkit!** 🎉

