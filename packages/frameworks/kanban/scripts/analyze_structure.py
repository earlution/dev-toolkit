#!/usr/bin/env python3
"""
Analysis Utility for Existing Kanban Structures

Analyzes detected Kanban structures and maps them to canonical E/S/T format,
identifying conflicts and generating migration plans.

Part of Epic 4, Story 7, Task 1 (BR-006): Detection/analysis utilities for existing structures.

Usage:
    python3 analyze_structure.py [--detection-report REPORT] [--output OUTPUT_FILE]

Arguments:
    --detection-report REPORT  Path to detection report JSON (default: detection_report.json)
    --output OUTPUT_FILE       Output file for analysis report (default: analysis_report.json)
    --verbose                  Enable verbose output
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime


class KanbanStructureAnalyzer:
    """Analyzes detected Kanban structures and generates migration plan."""
    
    # Canonical framework epics
    CANONICAL_CORE_EPICS = set(range(1, 9))  # Epics 1-8 are core
    CANONICAL_ANCILLARY_EPICS = set(range(9, 22))  # Epics 9-21 are ancillary
    CANONICAL_CORE_PLUS_EPICS = {10, 18, 22, 23}  # Core+ recommended epics
    
    def __init__(self, detection_report: Dict, verbose: bool = False):
        self.detection_report = detection_report
        self.verbose = verbose
        self.epic_mappings: List[Dict] = []
        self.story_mappings: List[Dict] = []
        self.task_mappings: List[Dict] = []
        self.conflicts: List[Dict] = []
        self.gaps: List[Dict] = []
        self.migration_plan: Dict = {}
        
    def analyze(self) -> Dict:
        """Main analysis method. Returns analysis report."""
        if self.detection_report.get("status") != "detected":
            return {
                "status": "no_structure_to_analyze",
                "message": "No Kanban structure detected. Cannot analyze.",
                "detection_status": self.detection_report.get("status")
            }
        
        self._analyze_epics()
        self._analyze_stories()
        self._analyze_tasks()
        self._identify_gaps()
        self._generate_migration_plan()
        
        return {
            "status": "analyzed",
            "analysis_date": datetime.now().isoformat(),
            "epic_mappings": self.epic_mappings,
            "story_mappings": self.story_mappings,
            "task_mappings": self.task_mappings,
            "conflicts": self.conflicts,
            "gaps": self.gaps,
            "migration_plan": self.migration_plan,
            "summary": {
                "epics_to_migrate": len(self.epic_mappings),
                "stories_to_migrate": len(self.story_mappings),
                "tasks_to_migrate": len(self.task_mappings),
                "conflict_count": len(self.conflicts),
                "gap_count": len(self.gaps),
                "migration_complexity": self._assess_complexity()
            }
        }
    
    def _analyze_epics(self):
        """Analyze epics and map to canonical format."""
        detected_epics = self.detection_report.get("epics", [])
        
        for epic in detected_epics:
            epic_num = epic["epic_number"]
            
            # Determine if this conflicts with canonical epics
            is_canonical_core = epic_num in self.CANONICAL_CORE_EPICS
            is_canonical_ancillary = epic_num in self.CANONICAL_ANCILLARY_EPICS
            is_canonical_core_plus = epic_num in self.CANONICAL_CORE_PLUS_EPICS
            
            mapping = {
                "source_epic_number": epic_num,
                "source_directory": epic["directory"],
                "source_epic_document": epic.get("epic_document"),
                "is_canonical": is_canonical_core or is_canonical_ancillary,
                "is_canonical_core": is_canonical_core,
                "is_canonical_ancillary": is_canonical_ancillary,
                "is_canonical_core_plus": is_canonical_core_plus,
                "stories_count": epic.get("stories_found", 0),
                "tasks_count": epic.get("tasks_found", 0),
                "migration_action": self._determine_epic_migration_action(
                    epic_num, is_canonical_core, is_canonical_ancillary
                ),
                "target_epic_number": self._determine_target_epic_number(
                    epic_num, is_canonical_core, is_canonical_ancillary
                )
            }
            
            self.epic_mappings.append(mapping)
            
            # Record conflicts
            if is_canonical_core:
                self.conflicts.append({
                    "type": "epic_conflict_core",
                    "severity": "high",
                    "epic_number": epic_num,
                    "message": f"Epic {epic_num} conflicts with canonical core epic. "
                              f"Recommendation: Renumber to {mapping['target_epic_number']} or use hybrid mode.",
                    "recommended_action": mapping["migration_action"]
                })
    
    def _determine_epic_migration_action(
        self, 
        epic_num: int, 
        is_canonical_core: bool, 
        is_canonical_ancillary: bool
    ) -> str:
        """Determine migration action for an epic."""
        if is_canonical_core:
            return "preserve_as_project_epic"  # Keep as project-specific, renumber if needed
        elif is_canonical_ancillary:
            return "preserve_as_project_epic"  # Keep as project-specific
        else:
            return "preserve_as_is"  # Project-specific epic, no conflict
    
    def _determine_target_epic_number(
        self,
        epic_num: int,
        is_canonical_core: bool,
        is_canonical_ancillary: bool
    ) -> Optional[int]:
        """Determine target epic number for migration."""
        if is_canonical_core:
            # Suggest renumbering to avoid conflict
            # Find next available epic number starting from 24 (after canonical range)
            return None  # Will be determined during migration
        elif is_canonical_ancillary:
            return None  # Keep as is, or renumber if desired
        else:
            return epic_num  # No change needed
    
    def _analyze_stories(self):
        """Analyze stories and map to canonical format."""
        detected_stories = self.detection_report.get("stories", [])
        
        for story in detected_stories:
            epic_num = story["epic_number"]
            story_num = story["story_number"]
            
            # Find corresponding epic mapping
            epic_mapping = next(
                (e for e in self.epic_mappings if e["source_epic_number"] == epic_num),
                None
            )
            
            mapping = {
                "source_epic_number": epic_num,
                "source_story_number": story_num,
                "source_story_file": story["file"],
                "target_epic_number": epic_mapping["target_epic_number"] if epic_mapping else epic_num,
                "target_story_number": story_num,  # Keep same story number within epic
                "tasks_count": story.get("tasks_found", 0),
                "migration_action": "preserve_and_convert_format",
                "requires_format_conversion": True
            }
            
            self.story_mappings.append(mapping)
    
    def _analyze_tasks(self):
        """Analyze tasks and map to canonical format."""
        detected_tasks = self.detection_report.get("tasks", [])
        
        for task in detected_tasks:
            epic_num = task["epic_number"]
            story_num = task["story_number"]
            task_num = task["task_number"]
            
            # Find corresponding story mapping
            story_mapping = next(
                (s for s in self.story_mappings 
                 if s["source_epic_number"] == epic_num 
                 and s["source_story_number"] == story_num),
                None
            )
            
            mapping = {
                "source_epic_number": epic_num,
                "source_story_number": story_num,
                "source_task_number": task_num,
                "source_format": task.get("format", "unknown"),
                "source_task_file": task.get("file"),
                "target_epic_number": story_mapping["target_epic_number"] if story_mapping else epic_num,
                "target_story_number": story_mapping["target_story_number"] if story_mapping else story_num,
                "target_task_number": task_num,  # Keep same task number within story
                "migration_action": "preserve_and_convert_format",
                "requires_format_conversion": task.get("format") != "full"
            }
            
            self.task_mappings.append(mapping)
    
    def _identify_gaps(self):
        """Identify gaps in the structure (missing canonical epics, etc.)."""
        detected_epic_numbers = {
            epic["source_epic_number"] for epic in self.epic_mappings
        }
        
        # Check for missing canonical core epics
        missing_core_epics = self.CANONICAL_CORE_EPICS - detected_epic_numbers
        if missing_core_epics:
            self.gaps.append({
                "type": "missing_canonical_core_epics",
                "severity": "high",
                "message": f"Missing canonical core epics: {sorted(missing_core_epics)}",
                "epic_numbers": sorted(missing_core_epics),
                "recommendation": "Install canonical core epics during migration"
            })
        
        # Check for missing epic documents
        for epic in self.epic_mappings:
            if not epic["source_epic_document"]:
                self.gaps.append({
                    "type": "missing_epic_document",
                    "severity": "medium",
                    "epic_number": epic["source_epic_number"],
                    "message": f"Epic {epic['source_epic_number']} missing epic document",
                    "recommendation": "Create epic document from template during migration"
                })
    
    def _generate_migration_plan(self):
        """Generate migration plan based on analysis."""
        # Determine recommended installation mode
        has_conflicts = any(c["severity"] == "high" for c in self.conflicts)
        has_project_epics = any(
            not e["is_canonical"] for e in self.epic_mappings
        )
        
        if has_conflicts and has_project_epics:
            recommended_mode = "hybrid"
        elif has_project_epics:
            recommended_mode = "migration"
        else:
            recommended_mode = "fresh"
        
        self.migration_plan = {
            "recommended_mode": recommended_mode,
            "modes_available": ["fresh", "migration", "update", "hybrid"],
            "steps": [
                {
                    "step": 1,
                    "action": "backup_existing_structure",
                    "description": "Create backup of existing Kanban structure",
                    "required": True
                },
                {
                    "step": 2,
                    "action": "resolve_conflicts",
                    "description": "Resolve epic numbering conflicts",
                    "required": has_conflicts,
                    "conflicts_to_resolve": len([c for c in self.conflicts if c["severity"] == "high"])
                },
                {
                    "step": 3,
                    "action": "install_canonical_epics",
                    "description": "Install canonical core epics (1-8)",
                    "required": True,
                    "epics_to_install": sorted(self.CANONICAL_CORE_EPICS)
                },
                {
                    "step": 4,
                    "action": "migrate_project_epics",
                    "description": "Migrate project-specific epics to canonical format",
                    "required": has_project_epics,
                    "epics_to_migrate": len([e for e in self.epic_mappings if not e["is_canonical"]])
                },
                {
                    "step": 5,
                    "action": "migrate_stories",
                    "description": "Migrate stories to canonical format",
                    "required": True,
                    "stories_to_migrate": len(self.story_mappings)
                },
                {
                    "step": 6,
                    "action": "migrate_tasks",
                    "description": "Migrate tasks to canonical format",
                    "required": True,
                    "tasks_to_migrate": len(self.task_mappings)
                },
                {
                    "step": 7,
                    "action": "validate_migration",
                    "description": "Validate migrated structure",
                    "required": True
                }
            ],
            "estimated_complexity": self._assess_complexity(),
            "warnings": self._generate_warnings()
        }
    
    def _assess_complexity(self) -> str:
        """Assess migration complexity."""
        conflict_count = len([c for c in self.conflicts if c["severity"] == "high"])
        epic_count = len(self.epic_mappings)
        story_count = len(self.story_mappings)
        task_count = len(self.task_mappings)
        
        if conflict_count > 3 or epic_count > 10 or task_count > 100:
            return "high"
        elif conflict_count > 0 or epic_count > 5 or task_count > 50:
            return "medium"
        else:
            return "low"
    
    def _generate_warnings(self) -> List[str]:
        """Generate migration warnings."""
        warnings = []
        
        if any(c["severity"] == "high" for c in self.conflicts):
            warnings.append(
                "High-severity conflicts detected. Manual intervention required for epic renumbering."
            )
        
        if len(self.gaps) > 0:
            warnings.append(
                f"{len(self.gaps)} gaps identified. Review gaps section for details."
            )
        
        epic_count = len(self.epic_mappings)
        if epic_count > 10:
            warnings.append(
                f"Large number of epics ({epic_count}) detected. Migration may take significant time."
            )
        
        return warnings


def main():
    parser = argparse.ArgumentParser(
        description="Analyze detected Kanban structures and generate migration plan"
    )
    parser.add_argument(
        "--detection-report",
        type=str,
        default="detection_report.json",
        help="Path to detection report JSON (default: detection_report.json)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="analysis_report.json",
        help="Output file for analysis report (default: analysis_report.json)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Load detection report
    detection_path = Path(args.detection_report)
    if not detection_path.exists():
        print(f"Error: Detection report not found: {detection_path}")
        return 1
    
    with open(detection_path, 'r', encoding='utf-8') as f:
        detection_report = json.load(f)
    
    if args.verbose:
        print(f"Analyzing structure from detection report: {detection_path}")
    
    analyzer = KanbanStructureAnalyzer(detection_report, verbose=args.verbose)
    analysis_report = analyzer.analyze()
    
    # Write report to file
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_report, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print("Analysis Report Summary")
    print(f"{'='*60}")
    if analysis_report.get("status") == "analyzed":
        summary = analysis_report["summary"]
        plan = analysis_report["migration_plan"]
        
        print(f"Epics to migrate: {summary['epics_to_migrate']}")
        print(f"Stories to migrate: {summary['stories_to_migrate']}")
        print(f"Tasks to migrate: {summary['tasks_to_migrate']}")
        print(f"Conflicts: {summary['conflict_count']}")
        print(f"Gaps: {summary['gap_count']}")
        print(f"\nRecommended mode: {plan['recommended_mode']}")
        print(f"Complexity: {summary['migration_complexity']}")
        
        if plan.get("warnings"):
            print(f"\n⚠️  Warnings:")
            for warning in plan["warnings"]:
                print(f"  - {warning}")
    else:
        print(f"Status: {analysis_report.get('status')}")
        print(f"Message: {analysis_report.get('message')}")
    
    print(f"\nFull report written to: {output_path}")
    print(f"{'='*60}\n")
    
    return 0 if analysis_report.get("status") == "analyzed" else 1


if __name__ == "__main__":
    exit(main())

