---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:54Z
expires_at: null
housekeeping_policy: keep
---

# Debug Path Framework

**Portable Package:** This directory contains the Debug Path Framework (DPF) and Debug Round Workflow (DRW) for structured debugging of test failures, regressions, and production bugs.

**Source:** Originally developed for fynd.deals project, refined and adapted for vibe-dev-kit.  
**Last Updated:** 2025-12-04  
**Version:** 1.0.0

---

## 🧩 Modularity & Dependencies

This package is designed to be **fully modular** with maximum independence. It can be used standalone or combined with other packages.

### Standalone Usage

✅ **This package can be used completely independently** without requiring any other `vibe-dev-kit` packages.

**What you get standalone:**
- Complete Debug Round Workflow (DRW) methodology
- Checklist-driven debugging process
- Templates for all debug path documents
- Structured debugging patterns (assumption validation, solution space mapping)
- Knowledge extraction and archival process

**Hard dependencies (required):**
- None — this is a pure documentation/template package

**Independence score:** 10/10 — Pure documentation/templates, no runtime dependencies.

---

### Combined Usage

**With Kanban Package:**
- Debug paths can be linked to Kanban Stories for traceability
- Integration: Debug paths document investigation, Stories track resolution
- Optional: Can use debug paths without Kanban (standalone debugging)

**With Workflow Management Package:**
- Debug Path Workflow can automate DRW phases (future)
- Integration: Agent-driven debugging following DRW methodology
- Optional: Can use debug paths manually without workflow automation

**With Both Packages:**
- Complete integration: Debug paths linked to Stories, automated via workflows
- Full traceability: Debug investigation → Story resolution → Release

---

## 📋 Package Overview

The Debug Path Framework provides a **checklist-driven, multi-phase protocol** for investigating and resolving test failures, regressions, and production bugs. It follows a structured **Debug Round Workflow (DRW)** with 6 phases:

1. **Phase 1: Testing** — Execute tests, document results
2. **Phase 2: Analysis** — Analyze failures, root causes
3. **Phase 3: Strategy** — Update plan, hypotheses, approach
4. **Phase 4: Planning** — Implementation steps, success criteria
5. **Phase 5: Implementation** — Code/test changes, rationale
6. **Phase 6: Verification & Archival** — Archive, extract lessons

**Key Features:**
- ✅ Checklist-driven workflow (prevents skipped steps)
- ✅ Context snapshot pattern (maintains focus)
- ✅ Solution space mapping (prevents repeated failures)
- ✅ Assumption validation (prevents confirmation bias)
- ✅ Round-based iteration (supports complex investigations)
- ✅ Knowledge extraction (builds institutional memory)

---

## 🎯 When to Use Debug Paths

**Use Debug Paths when:**
- ✅ Test failure or regression needs investigation
- ✅ Production bug requires structured debugging
- ✅ Simple project doesn't need full Kanban structure
- ✅ Focused debugging session (not feature development)
- ✅ Team wants structured debugging without Epic/Story overhead

**Use Kanban (instead) when:**
- ✅ Feature development or planned work
- ✅ Multiple related tasks need coordination
- ✅ Full project management structure needed
- ✅ Integration with versioning and release workflows needed

---

## 📚 Package Contents

### Core Documentation

1. **`README.md`** — This file — package overview and quick reference
2. **`PACKAGE_OVERVIEW.md`** — Complete package structure and usage scenarios
3. **`DRW-METHODOLOGY.md`** — Debug Round Workflow methodology guide

### Templates

4. **`templates/debug-path-main-template.md`** — Main debug path document template
5. **`templates/debug-path-process-template.md`** — Process tracking template
6. **`templates/debug-path-analysis-template.md`** — Analysis template
7. **`templates/debug-path-strategy-template.md`** — Strategy template
8. **`templates/debug-path-history-template.md`** — History template
9. **`templates/debug-path-tests-template.md`** — Tests template
10. **`templates/debug-path-index-template.md`** — Index entry point template

### Integration Guides

11. **`integration/kanban-integration.md`** — How to integrate with Kanban package
12. **`integration/workflow-mgt-integration.md`** — How to integrate with Workflow Management package

### Future (Planned)

13. **`workflows/debug-path-workflow.yaml`** — Agent-driven Debug Path Workflow
14. **`KB/Documentation/Developer_Docs/vwmp/debug-path-workflow-agent-execution.md`** — Workflow execution guide

---

## 🚀 Quick Start

### 1. Create a New Debug Path

1. Copy `templates/debug-path-main-template.md` to your debug paths directory
2. Rename to `DP-001-[title].md` (or your numbering scheme)
3. Fill in the context snapshot (problem statement, expected vs actual behavior)
4. Define testing scope (test files, source files, test command)

### 2. Follow the DRW Workflow

1. **Phase 1:** Execute tests, document results in `DP-001-tests.md`
2. **Phase 2:** Analyze failures, document in `DP-001-analysis.md`
3. **Phase 3:** Update strategy in `DP-001-strategy.md`
4. **Phase 4:** Create implementation plan in `DP-001-process.md`
5. **Phase 5:** Execute changes, document in `DP-001-process.md`
6. **Phase 6:** Verify, archive round, extract lessons in `DP-001-history.md`

### 3. Track Progress

- Use the checklist in `DP-001-process.md` to track round progress
- Check off each item as completed
- Archive completed checklist in `DP-001-history.md` at round end

---

## 📖 Documentation

**Start Here:** Read `PACKAGE_OVERVIEW.md` for complete package structure and usage scenarios.

**Methodology:** Read `DRW-METHODOLOGY.md` for detailed Debug Round Workflow guide.

**Integration:** See `integration/` directory for integration with other packages.

---

## 🔗 Related Packages

- **Kanban:** Link debug paths to Stories for traceability
- **Workflow Management:** Automate DRW phases via Debug Path Workflow (future)
- **Numbering & Versioning:** Version debug paths if needed (optional)

---

## 📝 Copy Pattern

**⚠️ CRITICAL: Copy, Don't Reference**

Projects must **copy** this package into their repository, not link to it.

**Why copy?**
- Projects need to customize templates and workflows
- Projects evolve independently and may need project-specific adaptations
- Copying ensures projects have full control over their debugging process
- Prevents breaking changes in `vibe-dev-kit` from affecting consuming projects

**What to copy:**
1. All files in `packages/frameworks/debug-path/`
2. Maintain directory structure
3. Customize templates with project-specific paths and commands
4. Update examples with project-specific details

**Customization boundaries:**
- ✅ **CAN customize:** File paths, test commands, document structure, numbering scheme
- ❌ **MUST keep:** DRW 6-phase structure, checklist-driven workflow, assumption validation pattern, solution space mapping

---

**Last Updated:** 2025-12-04  
**Version:** 1.0.0

