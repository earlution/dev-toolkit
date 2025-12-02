# Vibe Dev Kit

**Central Repository for Development Workflow and Versioning Packages**

This repository contains portable, reusable packages for implementing development workflows, versioning strategies, and project management practices across multiple projects.

---

## 📦 Packages

### 1. Workflow Management (`workflow mgt/`)

Complete package for implementing the Release Workflow (RW) trigger and agent-driven workflow execution pattern.

**Features:**
- 10-step Release Workflow with intelligent agent execution
- "ALL sections" requirement for documentation consistency
- Atomicity and blocked protocol (accessibility-critical)
- Epic branch workflow enforcement
- Validation scripts for branch context and changelog format

**Quick Start:**
```bash
cd workflow\ mgt/
cat README.md
```

**Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source:** fynd.deals (Epic 15, Story 1)

---

### 2. Numbering & Versioning (`numbering & versioning/`)

Complete policy package for implementing numbering and versioning strategies.

**Features:**
- Semantic versioning schema: `RC.EPIC.STORY.TASK+BUILD`
- Epic renumbering strategy (legacy vs. new format separation)
- Forensic traceability
- Kanban integration
- Templates for Epic and Story documents

**Quick Start:**
```bash
cd numbering\ \&\ versioning/
cat README.md
```

**Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source:** fynd.deals (Epic 15, Story 1)

---

## 🚀 Getting Started

### For New Projects

1. **Choose Your Packages:**
   - Need release workflow automation? → Use `workflow mgt/`
   - Need versioning strategy? → Use `numbering & versioning/`
   - Need both? → Use both packages together

2. **Copy to Your Project:**
   ```bash
   # Copy workflow management package
   cp -r workflow\ mgt/ /path/to/your/project/
   
   # Copy numbering & versioning package
   cp -r numbering\ \&\ versioning/ /path/to/your/project/
   ```

3. **Customize:**
   - Update file paths in all documents
   - Customize version schema if needed
   - Update branch patterns if using different naming
   - Follow implementation guides in each package

### For Existing Projects

1. **Review Current Practices:**
   - Compare your current workflow with the packages
   - Identify gaps and improvements

2. **Plan Migration:**
   - Follow implementation guides
   - Grandfather existing versions if needed
   - Gradually adopt new practices

---

## 📚 Documentation

Each package includes comprehensive documentation:

- **README.md** - Overview and quick start
- **PACKAGE_OVERVIEW.md** - Package structure and usage scenarios
- **IMPLEMENTATION_GUIDE.md** - Step-by-step implementation guide
- **Templates** - Ready-to-use templates for epics, stories, etc.

---

## 🔄 Updates

This repository is maintained as a central source of truth. When packages are updated:

1. Changes are committed to this repository
2. Projects can pull updates as needed
3. Version numbers track package evolution

**Current Version:** 2.0.0 (2025-12-02)

---

## 🤝 Contributing

To contribute improvements:

1. Test changes in your project first
2. Document changes clearly
3. Update version numbers
4. Submit pull request with clear description

---

## 📝 License

See individual package documentation for license information.

---

## 🔗 Related Projects

These packages were developed and refined in:
- **fynd.deals** - Epic 15, Story 1 (Documentation)

---

**Repository:** https://github.com/earlution/vibe-dev-kit  
**Last Updated:** 2025-12-02

