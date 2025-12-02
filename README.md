# Vibe Dev Kit

**Repository for "Vibe Coding [for Dummies]" Book Project**

This repository contains tools, SOPs, frameworks, and other resources developed for the book project. All packages are portable, reusable, and designed to be adapted for use in real-world projects.

---

## 📚 About This Repository

This repository supports the **"Vibe Coding [for Dummies]"** book project (working title). It serves as a central collection of:

- **Frameworks** - Complete, reusable development frameworks
- **Tools** - Development tools and utilities
- **SOPs** - Standard Operating Procedures and workflows
- **Templates** - Ready-to-use templates for common tasks
- **Examples** - Reference implementations and examples

All packages are designed to be:
- ✅ **Portable** - Can be copied and adapted to any project
- ✅ **Well-Documented** - Comprehensive guides and examples
- ✅ **Versioned** - Tracked versions for stability
- ✅ **Tested** - Used in real projects (fynd.deals, etc.)

---

## 📦 Package Categories

### Frameworks (`packages/frameworks/`)

Complete, reusable development frameworks with full documentation and implementation guides.

**Current Packages:**
- **Workflow Management** - Release Workflow (RW) trigger and agent-driven workflow execution (v2.0.0)
- **Numbering & Versioning** - Semantic versioning and numbering strategies (v2.0.0)

**Coming Soon:**
- Architecture frameworks
- Testing frameworks
- Documentation frameworks

### Tools (`packages/tools/`)

Development tools and utilities for common tasks.

**Coming Soon:**
- Code generators
- Validation tools
- Automation scripts

### SOPs (`packages/sops/`)

Standard Operating Procedures and workflows for development practices.

**Coming Soon:**
- Code review processes
- Deployment procedures
- Incident response workflows

---

## 🚀 Quick Start

### Browse Available Packages

```bash
# List all frameworks
ls packages/frameworks/

# List all tools
ls packages/tools/

# List all SOPs
ls packages/sops/
```

### Use a Package

1. **Choose a package** from the appropriate category
2. **Read the package README** for overview and quick start
3. **Copy to your project** and customize as needed
4. **Follow the implementation guide** for step-by-step setup

**Example:**
```bash
# Copy a framework to your project
cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/

# Follow the package's README for customization
cd /path/to/your/project/workflow\ mgt/
cat README.md
```

---

## 📁 Repository Structure

```
vibe-dev-kit/
├── README.md                    # This file
├── packages/
│   ├── frameworks/              # Complete development frameworks
│   │   ├── workflow mgt/        # Release Workflow framework
│   │   └── numbering & versioning/  # Versioning strategy framework
│   ├── tools/                   # Development tools and utilities
│   └── sops/                    # Standard Operating Procedures
├── templates/                   # Project templates (coming soon)
├── examples/                    # Reference implementations (coming soon)
└── docs/                        # Additional documentation (coming soon)
```

---

## 📦 Current Packages

### Frameworks

#### 1. Workflow Management (`packages/frameworks/workflow mgt/`)

Complete package for implementing the Release Workflow (RW) trigger and agent-driven workflow execution pattern.

**Features:**
- 10-step Release Workflow with intelligent agent execution
- "ALL sections" requirement for documentation consistency
- Atomicity and blocked protocol (accessibility-critical)
- Epic branch workflow enforcement
- Validation scripts for branch context and changelog format

**Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source:** fynd.deals (Epic 15, Story 1)

---

#### 2. Numbering & Versioning (`packages/frameworks/numbering & versioning/`)

Complete policy package for implementing numbering and versioning strategies.

**Features:**
- Semantic versioning schema: `RC.EPIC.STORY.TASK+BUILD`
- Epic renumbering strategy (legacy vs. new format separation)
- Forensic traceability
- Kanban integration
- Templates for Epic and Story documents

**Version:** 2.0.0  
**Last Updated:** 2025-12-02  
**Source:** fynd.deals (Epic 15, Story 1)

---

## 🔄 Package Updates

When packages are updated:

1. Changes are committed to this repository
2. Version numbers are incremented
3. Update summaries are included in package directories
4. Projects can pull updates as needed

**Current Repository Version:** 1.0.0 (2025-12-02)

---

## 🤝 Contributing

To contribute new packages or improvements:

1. **Create a new package** in the appropriate category (`frameworks/`, `tools/`, or `sops/`)
2. **Follow package structure** - Include README, implementation guide, examples
3. **Document thoroughly** - Clear usage instructions and customization notes
4. **Test in real projects** - Validate packages work in practice
5. **Submit pull request** - Include clear description and version number

### Package Structure Template

Each package should include:
- `README.md` - Overview and quick start
- `PACKAGE_OVERVIEW.md` - Package structure and usage scenarios
- `IMPLEMENTATION_GUIDE.md` - Step-by-step implementation guide
- Templates/examples as needed
- Version number and update history

---

## 📝 License

See individual package documentation for license information.

---

## 🔗 Related Projects

Packages are developed and refined in real projects:
- **fynd.deals** - Epic 15, Story 1 (Documentation)

---

## 📚 Book Project

This repository supports the **"Vibe Coding [for Dummies]"** book project. Packages here represent:

- **Proven practices** - Tested in real-world projects
- **Complete solutions** - Ready to use, not just concepts
- **Learning resources** - Examples and guides for readers
- **Reference implementations** - Code and configurations readers can study

---

**Repository:** https://github.com/earlution/vibe-dev-kit  
**Book Project:** "Vibe Coding [for Dummies]" (working title)  
**Last Updated:** 2025-12-02
