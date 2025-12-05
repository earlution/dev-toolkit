# Vibe Dev Kit

[![Version](https://img.shields.io/badge/version-0.3.3.6%2B1-blue)](./CHANGELOG.md)
[![Changelog](https://img.shields.io/badge/changelog-Keep%20a%20Changelog-brightgreen)](./CHANGELOG.md)
[![Repo](https://img.shields.io/github/stars/earlution/vibe-dev-kit?style=social)](https://github.com/earlution/vibe-dev-kit)

**An opinionated collection of portable frameworks, workflows, and policies for building real projects with AI-first development workflows.**

---

## Table of Contents

- [About The Project](#about-the-project)
  - [What Problem Does This Solve?](#what-problem-does-this-solve)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Quick Start: Release Workflow](#quick-start-release-workflow)
  - [Using Multiple Frameworks Together](#using-multiple-frameworks-together)
  - [Package Structure](#package-structure)
- [Available Frameworks](#available-frameworks)
  - [Workflow Management](#workflow-management)
  - [Numbering & Versioning](#numbering--versioning)
  - [Kanban](#kanban)
  - [Debug Path Framework](#debug-path-framework)
  - [Document Lifecycle Management](#document-lifecycle-management)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact & Acknowledgments](#contact--acknowledgments)

---

## About The Project

**Vibe Dev Kit** is a collection of **portable, battle-tested frameworks** that help you build and run real software projects using AI-first development workflows. Instead of starting from scratch or cobbling together incomplete solutions, you get complete, documented frameworks that you can copy into your project and adapt to your needs.

### What Problem Does This Solve?

If you're building software with AI coding assistants (like Cursor, GitHub Copilot, or similar), you've probably encountered these challenges:

- **No Standard Workflows**: Every project reinvents release processes, versioning strategies, and project management
- **Incomplete Solutions**: You find a workflow here, a template there, but nothing that works together cohesively
- **Documentation Gaps**: Tools exist but lack clear guides for non-experts or integration instructions
- **Versioning Chaos**: Semantic versioning doesn't fit AI-driven development patterns where features emerge iteratively
- **Knowledge Loss**: Best practices exist in your head or scattered docs, not in reusable frameworks

**Vibe Dev Kit solves these problems** by providing:

✅ **Complete Frameworks** – Not just ideas, but full implementations with documentation  
✅ **Portable & Modular** – Copy what you need, adapt it to your project structure  
✅ **AI-First Design** – Built specifically for AI-assisted development workflows  
✅ **Battle-Tested** – Used in real projects (200K+ LOC commercial products)  
✅ **Well-Documented** – Clear guides for both technical and non-technical users  
✅ **Integrated Systems** – Frameworks work together seamlessly (Kanban → Versioning → Release Workflow)

### Who Is This For?

- **Solo Developers** building products with AI assistance
- **Small Teams** needing structure without bureaucracy
- **Non-Technical Founders** who want to understand and guide development
- **Junior Engineers** learning best practices through proven frameworks
- **Anyone** building software with AI coding assistants who wants to do it right

---

## Built With

The dev kit itself is **deliberately tool-agnostic** in runtime dependencies, but assumes:

- **Git & GitHub** – For source control and collaboration
- **AI Coding Assistants** – Cursor, GitHub Copilot, or similar (for workflow execution)
- **Markdown** – For documentation, policies, and knowledge base

**Design Philosophy:**

- **Portable** – Copy packages into any project, adapt locally
- **Modular** – Use one framework or combine multiple
- **Documentation-First** – Every package includes implementation guides
- **Versioned** – Using `RC.EPIC.STORY.TASK+BUILD` for forensic traceability

**Inspiration & Standards:**

- **Best-README-Template** – [`https://github.com/othneildrew/Best-README-Template`](https://github.com/othneildrew/Best-README-Template) for README structure
- **Keep a Changelog** – [`https://github.com/olivierlacan/keep-a-changelog`](https://github.com/olivierlacan/keep-a-changelog) for changelog format
- **Shields.io** – [`https://shields.io/`](https://shields.io/) for badges

---

## Getting Started

### Prerequisites

Before using Vibe Dev Kit, you'll need:

- **Git** installed on your system
- **A GitHub account** (recommended for collaboration)
- **A modern code editor** with AI assistant support:
  - [Cursor](https://cursor.sh/) (recommended)
  - GitHub Copilot
  - Or similar AI coding assistant
- **Basic familiarity** with:
  - Command line (terminal)
  - Git basics (clone, commit, push)
  - Markdown (for reading documentation)

**Don't worry if you're not an expert** – each framework includes step-by-step guides.

### Installation

Vibe Dev Kit is **not installed as a dependency**. Instead, you **copy the frameworks you need** into your own project. This keeps your project independent and allows you to customize everything.

#### Step 1: Clone This Repository

```bash
git clone https://github.com/earlution/vibe-dev-kit.git
cd vibe-dev-kit
```

#### Step 2: Browse Available Frameworks

```bash
# See what's available
ls packages/frameworks/

# Explore a specific framework
cd packages/frameworks/workflow\ mgt/
cat README.md
```

#### Step 3: Copy a Framework to Your Project

```bash
# Example: Copy the Release Workflow framework
cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/

# Or copy multiple frameworks
cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/
cp -r "packages/frameworks/numbering & versioning" /path/to/your/project/numbering-and-versioning
cp -r packages/frameworks/kanban/ /path/to/your/project/
```

#### Step 4: Follow the Framework's Implementation Guide

Each framework includes:
- **README.md** – Overview and quick start
- **PACKAGE_OVERVIEW.md** – Structure and concepts
- **IMPLEMENTATION_GUIDE.md** – Step-by-step setup instructions
- **Templates** – Ready-to-use templates and examples

Navigate to your copied framework and follow its documentation:

```bash
cd /path/to/your/project/workflow\ mgt/
cat README.md
cat IMPLEMENTATION_GUIDE.md
```

---

## Usage

### Quick Start: Release Workflow

The **Release Workflow (RW)** framework is the most popular starting point. It provides an AI-driven release process that handles versioning, changelogs, git operations, and validation automatically.

#### Option 1: Use the Installer (Recommended)

The RW framework includes an installer that sets everything up automatically:

```bash
# 1. Copy the workflow package to your project
cp -r /path/to/vibe-dev-kit/packages/frameworks/workflow\ mgt/* /path/to/your/project/

# 2. Run the installer
cd /path/to/your/project
python scripts/install_release_workflow.py

# 3. Answer a few questions (or use --mode c for full stack)
# 4. Start using RW by typing "RW" in your AI assistant!
```

**That's it!** The installer generates `rw-config.yaml`, updates `.cursorrules`, and patches workflow files automatically.

#### Option 2: Manual Setup

If you prefer manual setup, see the [RW Quickstart Guide](packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/rw-installer-quickstart-guide.md).

### Using Multiple Frameworks Together

Frameworks are designed to work together. The recommended combination:

1. **Kanban** – Organize work into Epics, Stories, and Tasks
2. **Numbering & Versioning** – Version your work using `RC.EPIC.STORY.TASK+BUILD`
3. **Release Workflow** – Automate releases with AI-driven workflows

**Installation:**

```bash
# Copy all three frameworks
cp -r packages/frameworks/kanban/ /path/to/your/project/
cp -r "packages/frameworks/numbering & versioning" /path/to/your/project/numbering-and-versioning
cp -r packages/frameworks/workflow\ mgt/ /path/to/your/project/

# Follow each framework's integration guide
```

Each framework's README includes integration instructions for working with other frameworks.

### Package Structure

Every framework follows a consistent structure:

```
framework-name/
├── README.md                    # Overview and quick start
├── PACKAGE_OVERVIEW.md          # Structure and key concepts
├── IMPLEMENTATION_GUIDE.md      # Step-by-step setup
├── templates/                   # Ready-to-use templates
├── integration/                 # Guides for integrating with other frameworks
└── KB/                          # Knowledge base (policies, examples)
```

---

## Available Frameworks

### Workflow Management

**Purpose:** AI-driven release and workflow automation  
**Version:** 2.0.0  
**Status:** ✅ Production Ready

Complete package for implementing the Release Workflow (RW) – an 11-step intelligent release process that handles versioning, changelogs, git operations, and validation automatically.

**Key Features:**
- 🤖 **AI-Driven Execution** – Type "RW" and your AI assistant handles the entire release
- 🔒 **Branch Safety Checks** – Ensures you're releasing from the correct branch
- 📝 **Automatic Changelog Generation** – Creates detailed changelogs with timestamps
- ✅ **Validation** – Validates branch context and changelog format
- 🔧 **Plug-and-Play Installer** – Set up in minutes with a single CLI command
- 📚 **Complete Documentation** – Step-by-step guides for all skill levels

**Quick Start:** See [RW Quickstart Guide](packages/frameworks/workflow%20mgt/README.md#-rw-quickstart-using-installer)

**Documentation:** [`packages/frameworks/workflow mgt/README.md`](packages/frameworks/workflow%20mgt/README.md)

---

### Numbering & Versioning

**Purpose:** Semantic versioning strategy for AI-driven development  
**Version:** 2.0.0  
**Status:** ✅ Production Ready

Complete policy package for implementing the `RC.EPIC.STORY.TASK+BUILD` versioning schema, designed specifically for iterative, AI-assisted development.

**Key Features:**
- 🏷️ **Semantic Versioning** – `RC.EPIC.STORY.TASK+BUILD` schema
- 📊 **Forensic Traceability** – Every version maps to specific work items
- 🔄 **Epic Renumbering Strategy** – Handles legacy vs. new format separation
- 🎯 **Kanban Integration** – Works seamlessly with Kanban framework
- 📋 **Templates** – Epic and Story document templates

**Documentation:** [`packages/frameworks/numbering & versioning/README.md`](packages/frameworks/numbering%20&%20versioning/README.md)

---

### Kanban

**Purpose:** Kanban governance, templates, and integration  
**Version:** 1.0.0  
**Status:** ✅ Production Ready

Kanban framework for organizing work into Epics, Stories, and Tasks, with full integration with versioning and release workflows.

**Key Features:**
- 📋 **Epic/Story/Task Structure** – Clear hierarchy for organizing work
- 🎨 **Templates** – Ready-to-use Epic and Story templates
- 🔗 **Integration Guides** – Works with Versioning and Release Workflow
- 📚 **Governance Policy** – Clear rules for FR/BR → Task → Story → Epic flow
- 🎯 **Versioning Alignment** – Maps directly to `RC.EPIC.STORY.TASK+BUILD`

**Documentation:** [`packages/frameworks/kanban/README.md`](packages/frameworks/kanban/README.md)

---

### Debug Path Framework

**Purpose:** Systematic debugging methodology for test failures and regressions  
**Version:** 1.0.0  
**Status:** ✅ Production Ready

A 6-phase, checklist-driven protocol for investigating test failures, regressions, and production bugs. Includes Debug Round Workflow (DRW) methodology.

**Key Features:**
- 🔍 **Context Snapshots** – Capture state at failure points
- 🗺️ **Solution Space Mapping** – Systematically explore possible solutions
- ✅ **Assumption Validation** – Test assumptions before implementing fixes
- 🔄 **Round-Based Iteration** – Structured approach to debugging
- 📚 **Knowledge Extraction** – Document lessons learned

**Documentation:** [`packages/frameworks/debug-path/README.md`](packages/frameworks/debug-path/README.md)

---

### Document Lifecycle Management

**Purpose:** Manage document lifecycles with TTL-like metadata  
**Version:** 1.0.0  
**Status:** ✅ Production Ready

System for managing document lifecycles using metadata fields (`lifecycle`, `ttl_days`, `created_at`, `expires_at`, `housekeeping_policy`).

**Key Features:**
- ⏰ **Time-to-Live (TTL)** – Automatic expiration for temporary documents
- 🏷️ **Lifecycle Classification** – Evergreen, timeboxed, or transient
- 🧹 **Housekeeping Policies** – Automated cleanup workflows
- 📋 **Metadata Templates** – Ready-to-use document templates

**Documentation:** [`packages/frameworks/doc-lifecycle/README.md`](packages/frameworks/doc-lifecycle/README.md)

---

## Roadmap

This roadmap reflects the internal Epics tracked in the Kanban system. For detailed task-level work, see [`KB/PM_and_Portfolio/kanban/`](KB/PM_and_Portfolio/kanban/).

### ✅ Completed Epics

- **Epic 1 – Vibe Dev Kit Core** ✅
  - Dev-kit versioning policy established
  - Package & repo architecture documented
  - Core KB structure implemented

- **Epic 2 – Workflow Management Framework** ✅
  - Release Workflow (RW) agent execution docs complete
  - PDCA integration into RW
  - Additional workflows & examples
  - RW Installer & Plug-and-Play Adoption

- **Epic 4 – Kanban Framework** ✅
  - Dev-kit Kanban implementation
  - FR/BR intake to tasks flow
  - Kanban + Versioning + RW integration

### 🚧 In Progress

- **Epic 3 – Numbering & Versioning Framework**
  - ✅ Dev-kit alignment with versioning framework
  - 🚧 Versioning cookbook & examples (in progress)
  - 📋 Versioning integration with Kanban & RW (planned)

### 📋 Planned

- **Architecture Frameworks** – Design patterns and architectural decision records
- **Testing Frameworks** – Test strategies and frameworks for AI-assisted development
- **Documentation Frameworks** – Documentation generation and management
- **Additional Tools** – Code generators, validators, automation scripts

**See the [Kanban Board](KB/PM_and_Portfolio/kanban/) for detailed task-level tracking.**

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Follow Package Structure** – Include `README.md`, `PACKAGE_OVERVIEW.md`, `IMPLEMENTATION_GUIDE.md`, templates/examples
4. **Document Thoroughly** – Clear usage instructions and customization notes
5. **Test in Real Projects** – Validate packages work in practice
6. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
7. **Push to the Branch** (`git push origin feature/AmazingFeature`)
8. **Open a Pull Request** – Include a clear description and updated version numbers

### Package Contribution Guidelines

When adding a new package:

- **Choose the right category:**
  - **Frameworks** – Complete systems with full documentation (e.g., Release Workflow, Versioning Strategy)
  - **Tools** – Utilities and scripts (e.g., code generators, validators)
  - **SOPs** – Process documentation (e.g., code review procedures, deployment workflows)

- **Follow the package structure:**
  - Include `README.md` with overview
  - Include `PACKAGE_OVERVIEW.md` for structure
  - Include `IMPLEMENTATION_GUIDE.md` for step-by-step guide
  - Add version number and update history
  - Include templates/examples where applicable

- **Update main README.md** to list your new package

### Inspiration

For structure and sectioning inspiration, see:
- **Best-README-Template** – [`https://github.com/othneildrew/Best-README-Template`](https://github.com/othneildrew/Best-README-Template)

---

## License

Licensing may vary by package. See individual package `README.md` or `PACKAGE_OVERVIEW.md` files for license notes.

---

## Contact & Acknowledgments

### Project Information

- **Repository:** [`https://github.com/earlution/vibe-dev-kit`](https://github.com/earlution/vibe-dev-kit)
- **Book Project:** *"Vibe Coding [for Dummies]"* (working title)
- **Current Repo Version:** `v0.2.4.9+2` (2025-12-04)

### Acknowledgments

This repository supports the **"Vibe Coding [for Dummies]"** book project. Packages here represent:

- **Proven Practices** – Tested in real-world projects (200K+ LOC commercial products)
- **Complete Solutions** – Ready to use, not just concepts
- **Learning Resources** – Examples and guides for readers
- **Reference Implementations** – Code and configurations readers can study

**Related Projects:**

Packages here are developed and refined in real projects, for example:
- **fynd.deals** – Epic 15, Story 1 (Documentation and dev-kit extraction)

**Resources & Inspiration:**

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template) – README structure inspiration
- [Keep a Changelog](https://github.com/olivierlacan/keep-a-changelog) – Changelog format
- [Shields.io](https://shields.io/) – Badge generation

---

## Table of Contents (Quick Links)

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Available Frameworks](#available-frameworks)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact & Acknowledgments](#contact--acknowledgments)

---

**Ready to get started?** Jump to [Getting Started](#getting-started) or explore the [Release Workflow Quickstart](packages/frameworks/workflow%20mgt/README.md#-rw-quickstart-using-installer).
