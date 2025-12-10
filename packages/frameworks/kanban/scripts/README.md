# Kanban Migration Utilities

This directory contains utilities for detecting, analyzing, and migrating existing Kanban structures to the canonical ai-dev-kit Kanban framework format.

## Scripts

### `install_kanban_framework.py`

Main installation script with interactive mode selection. Integrates detection, analysis, and migration utilities.

**Usage:**
```bash
python3 install_kanban_framework.py [--mode MODE] [--kanban-path PATH] [--dry-run] [--force]
```

**Arguments:**
- `--mode MODE` - Installation mode: fresh, migration, update, hybrid, auto (default: auto)
- `--kanban-path PATH` - Path to Kanban directory (default: `KB/PM_and_Portfolio/kanban`)
- `--dry-run` - Preview changes without modifying files
- `--force` - Skip confirmation prompts
- `--skip-detection` - Skip detection step (use existing detection_report.json)
- `--skip-analysis` - Skip analysis step (use existing analysis_report.json)

**Example:**
```bash
# Interactive installation (recommended)
python3 install_kanban_framework.py

# Migration install with existing structure
python3 install_kanban_framework.py --mode migration

# Dry run to preview changes
python3 install_kanban_framework.py --mode migration --dry-run
```

**Workflow:**
1. Detects existing Kanban structure (if not fresh mode)
2. Analyzes structure and generates migration plan
3. Prompts for installation mode selection (or uses recommended mode)
4. Migrates structure based on selected mode
5. Validates migration

### `detect_existing_structure.py`

Scans a project directory to detect existing Kanban (Epic/Story/Task) structures and generates a detection report.

**Usage:**
```bash
python3 detect_existing_structure.py [--kanban-path PATH] [--output OUTPUT_FILE] [--verbose]
```

**Arguments:**
- `--kanban-path PATH` - Path to Kanban directory (default: `KB/PM_and_Portfolio/kanban`)
- `--output OUTPUT_FILE` - Output file for detection report (default: `detection_report.json`)
- `--verbose` - Enable verbose output

**Example:**
```bash
python3 detect_existing_structure.py \
  --kanban-path KB/PM_and_Portfolio/kanban \
  --output detection_report.json \
  --verbose
```

**Output:**
- JSON report containing detected epics, stories, tasks, and conflicts
- Summary printed to stdout

### `migrate_structure.py`

Migrates existing Kanban structures to canonical format, preserving all work items and forensic markers.

**Usage:**
```bash
python3 migrate_structure.py [--analysis-report REPORT] [--mode MODE] [--dry-run] [--backup-dir DIR]
```

**Arguments:**
- `--analysis-report REPORT` - Path to analysis report JSON (default: `analysis_report.json`)
- `--mode MODE` - Installation mode: fresh, migration, update, hybrid, auto (default: auto-detect)
- `--dry-run` - Preview changes without modifying files
- `--backup-dir DIR` - Directory for backups (default: auto-generated)
- `--kanban-path PATH` - Path to Kanban directory (default: `KB/PM_and_Portfolio/kanban`)
- `--force` - Skip confirmation prompts

**Example:**
```bash
python3 migrate_structure.py \
  --analysis-report analysis_report.json \
  --mode hybrid \
  --dry-run
```

**Output:**
- Creates backup of existing structure
- Migrates epics/stories/tasks to canonical format
- Updates epic/story/task references
- Validates migrated structure
- Generates migration report

### `analyze_structure.py`

Analyzes detected Kanban structures and maps them to canonical E/S/T format, identifying conflicts and generating migration plans.

**Usage:**
```bash
python3 analyze_structure.py [--detection-report REPORT] [--output OUTPUT_FILE] [--verbose]
```

**Arguments:**
- `--detection-report REPORT` - Path to detection report JSON (default: `detection_report.json`)
- `--output OUTPUT_FILE` - Output file for analysis report (default: `analysis_report.json`)
- `--verbose` - Enable verbose output

**Example:**
```bash
python3 analyze_structure.py \
  --detection-report detection_report.json \
  --output analysis_report.json \
  --verbose
```

**Output:**
- JSON report containing epic/story/task mappings, conflicts, gaps, and migration plan
- Summary printed to stdout including recommended installation mode and complexity assessment

## Workflow

### Recommended: Use Installation Script

The easiest way is to use the integrated installation script:

```bash
python3 install_kanban_framework.py
```

This will:
1. Detect existing structure
2. Analyze and generate migration plan
3. Prompt for installation mode
4. Migrate structure

### Manual Workflow

If you prefer to run utilities individually:

1. **Detect existing structure:**
   ```bash
   python3 detect_existing_structure.py --kanban-path KB/PM_and_Portfolio/kanban --output detection_report.json
   ```

2. **Analyze structure and generate migration plan:**
   ```bash
   python3 analyze_structure.py --detection-report detection_report.json --output analysis_report.json
   ```

3. **Review reports:**
   - Check `detection_report.json` for detected structures
   - Check `analysis_report.json` for conflicts, gaps, and migration plan
   - Review recommended installation mode (fresh, migration, update, hybrid)

4. **Proceed with migration:**
   ```bash
   python3 migrate_structure.py --analysis-report analysis_report.json --mode migration
   ```

## Report Formats

### Detection Report

```json
{
  "status": "detected",
  "detection_date": "2025-12-10T...",
  "kanban_path": "KB/PM_and_Portfolio/kanban",
  "epics": [...],
  "stories": [...],
  "tasks": [...],
  "conflicts": [...],
  "summary": {
    "epic_count": 10,
    "story_count": 46,
    "task_count": 335,
    "conflict_count": 1
  }
}
```

### Analysis Report

```json
{
  "status": "analyzed",
  "analysis_date": "2025-12-10T...",
  "epic_mappings": [...],
  "story_mappings": [...],
  "task_mappings": [...],
  "conflicts": [...],
  "gaps": [...],
  "migration_plan": {
    "recommended_mode": "hybrid",
    "steps": [...],
    "estimated_complexity": "high"
  },
  "summary": {...}
}
```

## Installation Modes

The analysis utility recommends one of four installation modes:

- **fresh** - No existing structure, clean install
- **migration** - Existing structure detected, migrate to canonical format
- **update** - Existing framework installation, update to new version
- **hybrid** - Preserve project epics, install framework epics (recommended when conflicts detected)

## Related Documentation

- BR-006: Missing Migration Support for Pre-Existing Kanban Structures
- FR-007: Migration Utilities and Installation Modes
- UXR-001: Migration User Experience Research
- Epic 4, Story 7: Migration Support and Installation Modes

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

