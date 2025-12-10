# Kanban Migration Utilities

This directory contains utilities for detecting, analyzing, and migrating existing Kanban structures to the canonical ai-dev-kit Kanban framework format.

## Scripts

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
   - Use migration utility (to be implemented in Task 2)
   - Follow migration plan steps from analysis report

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

