# earlution Dev Toolkit

A collection of small, reusable development utilities, tools and widgets for modern software projects.

## 🎯 Purpose

This toolkit contains practical, well-documented utilities that have proven useful across multiple projects. Each tool is self-contained, easy to understand, and designed to solve specific development challenges.

Unlike frameworks (which go in [ai-dev-kit](https://github.com/earlution/ai-dev-kit)), this repository focuses on **standalone tools** that can be used independently or integrated into existing workflows.

## 🛠️ Tools

### GitHub Badges (`tools/github-badges/`)
**Dynamic badge selection based on repository visibility.**

Automatically detects whether a repository is public or private and selects appropriate badge types (dynamic GitHub badges for public repos, static badges for private repos).

- **Use case:** Eliminate "REPO NOT FOUND" errors on GitHub README badges
- **Installation:** See [tools/github-badges/README.md](tools/github-badges/README.md)
- **Quick start:** `python3 tools/github-badges/update_badges.py`

---

*More tools coming soon...*

## 🚀 Getting Started

### Using a Tool

Each tool is self-contained. Navigate to the tool directory and follow its README:

```bash
cd tools/github-badges
python3 update_badges.py --help
```

### Adding a New Tool

1. Copy the template: `cp -r tools/_template tools/your-tool-name`
2. Rename and update files (see `tools/_template/TEMPLATE_GUIDE.md`)
3. Implement your tool functionality
4. Add your tool to this README
5. Test and document your tool

## 📋 Requirements

- Python 3.7+ (for Python-based tools)
- Git (for version control)
- See individual tool READMEs for specific dependencies

## 📚 Documentation

- [Contributing Guidelines](CONTRIBUTING.md)
- See individual tool directories for tool-specific documentation

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [AI Dev Kit](https://github.com/earlution/ai-dev-kit) - Framework and package collection for AI-assisted development
- [AI Architect Kit](https://github.com/earlution/ai-architect-kit) - Framework for AI-assisted software projects

---

**Maintained by:** [@earlution](https://github.com/earlution)
