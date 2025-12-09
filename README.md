# AI Dev Kit

<div align="center">

![Version](https://img.shields.io/badge/version-v0.7.1.1%2B1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A comprehensive toolkit for AI-assisted development workflows**

[Features](#features) • [Installation](#getting-started) • [Documentation](KB/Documentation) • [Report Bug](https://github.com/earlution/ai-dev-kit/issues) • [Request Feature](https://github.com/earlution/ai-dev-kit/issues)

</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
  - [Features](#features)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Frameworks](#frameworks)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

**AI Dev Kit** is a comprehensive toolkit designed to support AI-assisted development workflows. It provides modular, reusable frameworks for project management, versioning, workflow automation, and documentation lifecycle management.

The toolkit is designed to be:
- **Modular:** Use only what you need, combine frameworks as required
- **Portable:** Frameworks can be installed as dependencies or copy-pasted
- **Auto-updating:** Framework dependencies can receive automatic updates
- **Agent-friendly:** Designed for AI-assisted development workflows

### Features

- 🎯 **Workflow Management:** Agent-driven Release Workflow (RW) with 14-step automation
- 📊 **Kanban Framework:** Comprehensive project management with Epics, Stories, and Tasks
- 🔢 **Numbering & Versioning:** Forensic traceability with `RC.EPIC.STORY.TASK+BUILD` schema
- 📚 **Document Lifecycle Management:** TTL-based expiration and automated housekeeping
- 🐛 **Debug Path Framework:** Structured debugging methodology (DRW)
- 🔄 **Framework Dependencies:** Install frameworks as Git submodules, CLI tool, or package managers
- 📖 **Comprehensive Documentation:** User guides, developer docs, and integration examples

### Built With

- **Python 3.8+** - Core scripting and CLI tool
- **Git** - Version control and dependency management
- **Markdown** - Documentation and knowledge base
- **YAML** - Configuration files
- **Node.js 16+** - Package manager support (optional)

---

## Getting Started

### Prerequisites

Before installing AI Dev Kit frameworks, ensure you have:

- **Git** installed and configured
- **Python 3.8+** (for CLI tool and some frameworks)
- **Node.js 16+** (if using npm package manager)
- **A Git repository** for your project (frameworks are installed as Git dependencies)

### Installation

AI Dev Kit frameworks can be installed using three methods:

#### Method 1: Git Submodules (Recommended for Phase 1)

```bash
# Initialize Git repository (if not already done)
git init

# Install a framework as a Git submodule
git submodule add https://github.com/earlution/ai-dev-kit.git packages/frameworks/workflow\ mgt
git submodule add https://github.com/earlution/ai-dev-kit.git packages/frameworks/kanban
git submodule add https://github.com/earlution/ai-dev-kit.git packages/frameworks/numbering\ \&\ versioning

# Initialize and update submodules
git submodule update --init --recursive
```

#### Method 2: CLI Tool (Coming Soon)

```bash
# Install CLI tool
pip install ai-dev-kit

# Initialize in your project
ai-dev-kit init

# Install frameworks
ai-dev-kit install workflow-mgmt@2.0.0
ai-dev-kit install kanban@1.0.0
ai-dev-kit install numbering-versioning@2.0.0
```

#### Method 3: Package Managers (Future)

```bash
# npm
npm install @ai-dev-kit/workflow-mgmt @ai-dev-kit/kanban

# pip
pip install ai-dev-kit-workflow-mgmt ai-dev-kit-kanban
```

**📖 For detailed installation instructions, see the [Framework Dependency Installation Guide](KB/Documentation/User_Docs/framework-dependency-installation-guide.md)**

**📋 Not sure which approach to use? See the [Use Cases Guide](KB/Documentation/User_Docs/framework-dependency-use-cases.md)**

---

## Usage

### Quick Start: Release Workflow (RW)

The Release Workflow automates versioning, changelog updates, Git operations, and Kanban tracking:

```bash
# Trigger Release Workflow (RW) command
# The agent will:
# 1. Validate branch context
# 2. Bump version (RC.EPIC.STORY.TASK+BUILD)
# 3. Update changelog
# 4. Commit and tag
# 5. Update Kanban docs
# 6. Push to remote
```

### Using Kanban Framework

```markdown
# Create an Epic
KB/PM_and_Portfolio/kanban/epics/Epic-X/Epic-X.md

# Create a Story
KB/PM_and_Portfolio/kanban/epics/Epic-X/Story-XXX-description.md

# Track work with Tasks
- [ ] **E1:S01:T01** - Task description
```

### Versioning Your Project

```python
# src/your_project/version.py
VERSION_RC = 0        # Release candidate
VERSION_EPIC = 1     # Epic number
VERSION_STORY = 1     # Story number
VERSION_TASK = 1      # Task number
VERSION_BUILD = 1     # Build number

VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"
# Result: "0.1.1.1+1"
```

**📖 For more examples, see:**
- [Framework Dependency Usage Guide](KB/Documentation/User_Docs/framework-dependency-usage-guide.md)
- [Framework Dependency Integration Guide](KB/Documentation/User_Docs/framework-dependency-integration-guide.md)
- [CLI Reference](KB/Documentation/User_Docs/framework-dependency-cli-reference.md)

---

## Frameworks

AI Dev Kit includes the following modular frameworks:

| Framework | Description | Status | Version |
|-----------|-------------|--------|---------|
| **Workflow Management** | Agent-driven Release Workflow (RW) automation | ✅ Complete | v2.0.0 |
| **Kanban** | Project management with Epics, Stories, Tasks | ✅ Complete | v1.0.0 |
| **Numbering & Versioning** | Forensic traceability versioning schema | ✅ Complete | v2.0.0 |
| **Document Lifecycle** | TTL-based expiration and housekeeping | ✅ Complete | v1.0.0 |
| **Debug Path** | Structured debugging methodology (DRW) | ✅ Complete | v1.0.0 |

**📖 Framework Documentation:**
- [Workflow Management Framework](packages/frameworks/workflow%20mgt/README.md)
- [Kanban Framework](packages/frameworks/kanban/README.md)
- [Numbering & Versioning Framework](packages/frameworks/numbering%20%26%20versioning/README.md)
- [Document Lifecycle Management](packages/frameworks/doc-lifecycle/README.md)
- [Debug Path Framework](packages/frameworks/debug-path/README.md)

---

## Roadmap

### Completed ✅

- [x] Core infrastructure and repository architecture
- [x] Workflow Management Framework (Release Workflow)
- [x] Kanban Framework
- [x] Numbering & Versioning Framework
- [x] Framework dependency architecture
- [x] Comprehensive user documentation

### In Progress 🚧

- [ ] Documentation Management Framework (Epic 5)
- [ ] Book Content Development (Epic 9)
- [ ] Framework Update CLI Tool (Phase 2)

### Planned 📋

- [ ] Examples and Adoption (Epic 7)
- [ ] Tooling and Automation (Epic 8)
- [ ] Package Manager Support (Phase 3)
- [ ] Migration tools and guides

See the [Kanban Board](KB/PM_and_Portfolio/kanban/kanban-board.md) for detailed roadmap and progress tracking.

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow the [Release Workflow](packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md) for all changes
- Use the [Kanban Framework](packages/frameworks/kanban/README.md) for work tracking
- Adhere to the [Versioning Policy](KB/Architecture/Standards_and_ADRs/dev-kit-versioning-policy.md)
- Update documentation for any framework changes

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

**Project Maintainer:** [@earlution](https://github.com/earlution)

**Project Link:** [https://github.com/earlution/ai-dev-kit](https://github.com/earlution/ai-dev-kit)

**Issues:** [https://github.com/earlution/ai-dev-kit/issues](https://github.com/earlution/ai-dev-kit/issues)

---

## Acknowledgments

- [Best README Template](https://github.com/othneildrew/Best-README-Template) - README structure inspiration
- [Keep a Changelog](https://keepachangelog.com/) - Changelog format inspiration
- [Semantic Versioning](https://semver.org/) - Versioning principles
- [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules) - Dependency management
- [Head First Series](https://www.oreilly.com/series/head-first/) - Book style inspiration

---

<div align="center">

**[⬆ Back to Top](#ai-dev-kit)**

Made with ❤️ for the AI-assisted development community

</div>
