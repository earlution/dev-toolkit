# Story 004 – RW Installer & Plug-and-Play Adoption

**Status:** IN PROGRESS  
**Priority:** HIGH  
**Estimated Effort:** [TBD]  
**Created:** 2025-12-04  
**Last updated:** 2025-12-04 (v0.2.4.5+3 – T05 build 3: Document lifecycle management spec and policy)  
**Version:** v0.2.4.5+3  
**Code:** E2S04

---

## Overview

Make the Release Workflow (RW) and workflow management framework **plug-and-play** for new projects via a simple installer and single configuration file. Reduce manual path editing and cognitive overhead so that teams with varying technical depth can adopt RW safely and consistently.

This story turns RW from a "copy & hand-wire" pattern into a guided installation experience.

---

## Goal

Provide a **project-agnostic RW installer** and configuration model that allows:

- Fast, low-friction adoption of RW in new or existing projects
- A single configuration file per project for all RW paths and options
- Clear modes (RW-only, RW+versioning, RW+versioning+Kanban)
- Non-expert users to enable RW without deep knowledge of internal wiring

---

## Task Checklist

- [x] **E2:S04:T01 – Analyze current RW adoption friction and required config** ✅ COMPLETE (v0.2.4.1+1)  
- [x] **E2:S04:T02 – Design RW config schema (`rw-config.yaml`) and modes** ✅ COMPLETE (v0.2.4.2+1)  
- [x] **E2:S04:T03 – Implement RW installer CLI** ✅ COMPLETE (v0.2.4.3+1)  
- [x] **E2:S04:T04 – Create quickstart docs and template usage examples** ✅ COMPLETE (v0.2.4.4+1)  
- [x] **E2:S04:T05 – Usability test installer on sample and real projects** ✅ COMPLETE (v0.2.4.5+1)  

---

## Tasks

### E2:S04:T01 – Analyze current RW adoption friction and required config

**Input:**  
- Current workflow mgt package structure  
- `.cursorrules` RW trigger section  
- `workflows/release-workflow.yaml`  
- Validation scripts and docs  

**Deliverable:**  
- Analysis doc summarizing all places that currently require manual path edits  
- Minimal set of required configuration keys for a project-level RW config (e.g. `version_file`, `main_changelog`, `changelog_dir`, `use_kanban`, `kanban_root`, etc.)

**Approach:**
1. Enumerate all RW integration touchpoints (version file, changelog, Kanban, scripts, docs).  
2. Identify which values are **project-specific** vs **framework-internal**.  
3. Define the minimal set of configuration parameters that must be provided per project.  
4. Document findings in a short analysis note under the workflow mgt KB.  

**Acceptance Criteria:**
- [x] All path and project-specific touchpoints are identified and listed ✅  
- [x] Minimal config key set is defined and reviewed (no unnecessary knobs) ✅  
- [x] Decision recorded on which aspects remain hard-coded vs. configurable ✅  

**Deliverable:** ✅ **DELIVERED** - See `packages/frameworks/workflow mgt/KB/Analysis/T01-rw-adoption-friction-analysis.md` for complete analysis.  

---

### E2:S04:T02 – Design RW config schema (`rw-config.yaml`) and modes

**Input:**  
- Analysis from T01  
- Existing RW YAML config structure  
- Numbering & Versioning and Kanban integration patterns  

**Deliverable:**  
- `rw-config.yaml` schema specification  
- Example config files for different modes (Simple RW, RW+Versioning, Full stack)  

**Approach:**
1. Define top-level config keys (e.g. `version_file`, `changelog`, `kanban`, `mode`).  
2. Define **modes**:  
   - Mode A: RW-only (no Kanban, arbitrary versioning).  
   - Mode B: RW + dev-kit versioning.  
   - Mode C: RW + dev-kit versioning + Kanban integration.  
3. Design defaults for each mode to minimize required answers.  
4. Create example `rw-config.yaml` files under workflow mgt KB.  

**Acceptance Criteria:**
- [x] Schema defined and documented in KB ✅  
- [x] At least three example configs (one per mode) checked into repo ✅  
- [x] Config keys map cleanly to existing RW YAML and `.cursorrules` needs ✅  

**Deliverable:** ✅ **DELIVERED** - See `packages/frameworks/workflow mgt/config/rw-config-schema.md` for schema specification and `packages/frameworks/workflow mgt/config/examples/` for example configs.  

---

### E2:S04:T03 – Implement RW installer CLI

**Input:**  
- Config schema from T02  
- Existing workflow mgt package files  

**Deliverable:**  
- `install_release_workflow.py` (or similar) CLI tool in workflow mgt package  
- Ability to run installer in a target project and generate `rw-config.yaml` + wired `.cursorrules` + updated RW YAML

**Approach:**
1. Implement a CLI that can run from the target project root.  
2. Ask a small number of questions (or accept CLI flags):  
   - Where is your version file?  
   - Where is your main `CHANGELOG.md`?  
   - Do you want Kanban integration?  
   - Do you want to use dev-kit versioning schema?  
3. Write `rw-config.yaml` with the collected answers.  
4. Generate or update the RW section in `.cursorrules` using the config values.  
5. Patch `workflows/release-workflow.yaml` to reference config keys instead of hard-coded paths where appropriate.  
6. Provide a `--dry-run` mode that prints intended changes without writing files.  

**Acceptance Criteria:**
- [x] Running the installer in a clean sample project produces a usable RW setup ✅  
- [x] `.cursorrules`, RW YAML, and validation scripts all read from `rw-config.yaml` ✅  
- [x] `--dry-run` mode works and shows intended changes clearly ✅  

**Deliverable:** ✅ **DELIVERED** - See `packages/frameworks/workflow mgt/scripts/install_release_workflow.py` for installer CLI and `packages/frameworks/workflow mgt/scripts/README-rw-installer.md` for documentation. Validation scripts updated to read from `rw-config.yaml`.  

---

### E2:S04:T04 – Create quickstart docs and template usage examples

**Input:**  
- Working installer from T03  
- Existing workflow mgt `README.md` and portable implementation guide  

**Deliverable:**  
- RW Quickstart section in workflow mgt `README.md`  
- Dedicated installer/plug-and-play guide in KB  
- Example flows for greenfield and brownfield projects

**Approach:**
1. Document **greenfield** flow: using a template repo with RW pre-wired.  
2. Document **brownfield** flow: installing RW into an existing project via the installer.  
3. Provide short, copy-paste command sequences and expected outcomes.  
4. Add troubleshooting tips for common installer issues (paths, missing files, etc.).  

**Acceptance Criteria:**
- [x] README updated with a concise RW Quickstart using the installer ✅  
- [x] A dedicated KB doc exists for plug-and-play adoption with screenshots or transcripts ✅  
- [x] At least two worked examples (one greenfield, one brownfield) are documented ✅  

**Deliverable:** ✅ **DELIVERED** - See `packages/frameworks/workflow mgt/README.md` (RW Quickstart section) and `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/rw-installer-quickstart-guide.md` (dedicated guide with greenfield/brownfield examples).  

---

### E2:S04:T05 – Usability test installer on sample and real projects

**Input:**  
- Installer from T03  
- Docs from T04  
- One or more real projects (e.g., other repos you have open in different quadrants)  

**Deliverable:**  
- Usability test notes and any resulting improvements  
- Confirmed smooth adoption path for at least one real external project

**Approach:**
1. Run installer against a minimal sample repo and record any friction.  
2. Run installer against one of your real active projects (with your guidance).  
3. Capture issues (confusing prompts, missing defaults, error messages).  
4. Refine installer and docs based on findings.  
5. Optionally, gather feedback from another user or future you.  

**Acceptance Criteria:**
- [x] Installer successfully used on at least one non-dev-kit repo ✅  
- [x] Identified issues are fixed or documented ✅  
- [x] Story updated with final notes and version marker when complete ✅  

**Deliverable:** ✅ **DELIVERED** - See `packages/frameworks/workflow mgt/KB/Analysis/T05-rw-installer-usability-test.md` for complete usability test report with identified issues, recommendations, and test scenarios.  

---

## Dependencies

**Depends on:**  
- E2:S01 – RW Agent Execution & Docs (for existing RW docs and `.cursorrules` section)  
- E2:S02 – PDCA Integration into RW (for complete RW structure)  
- E2:S03 – Additional Workflows & Examples (for workflow patterns and examples)

**Blocks:**  
- Wider, low-friction adoption of RW across multiple external projects  
- Future stories that assume a simple, standardized RW installation path

---

## Success Criteria

- [ ] RW can be installed in a **fresh external project** by copying the package and running a single CLI with a short Q&A.  
- [ ] All RW path wiring lives in one config file (`rw-config.yaml`) per project.  
- [ ] Non-expert users can follow the quickstart docs to run RW successfully.  
- [ ] At least one of your other active projects has RW installed via this flow.  

