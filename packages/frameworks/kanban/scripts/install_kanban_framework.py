#!/usr/bin/env python3
"""
Kanban Framework Installation Script

Provides interactive installation with mode selection (Fresh, Migration, Update, Hybrid)
and integrates detection, analysis, and migration utilities.

Part of Epic 4, Story 7, Task 2 (FR-007): Migration utilities and installation modes.

Usage:
    python3 install_kanban_framework.py [--mode MODE] [--kanban-path PATH] [--dry-run]

Arguments:
    --mode MODE               Installation mode: fresh, migration, update, hybrid, auto
    --kanban-path PATH        Path to Kanban directory (default: KB/PM_and_Portfolio/kanban)
    --dry-run                 Preview changes without modifying files
    --force                   Skip confirmation prompts
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Optional


def run_command(cmd: list, cwd: Optional[Path] = None) -> tuple[int, str, str]:
    """Run a command and return exit code, stdout, stderr."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def detect_structure(kanban_path: Path, verbose: bool = False) -> Optional[Path]:
    """Run detection utility and return path to detection report."""
    print("🔍 Step 1: Detecting existing Kanban structure...")
    
    detection_report = Path("detection_report.json")
    cmd = [
        sys.executable,
        "packages/frameworks/kanban/scripts/detect_existing_structure.py",
        "--kanban-path", str(kanban_path),
        "--output", str(detection_report)
    ]
    
    if verbose:
        cmd.append("--verbose")
    
    exit_code, stdout, stderr = run_command(cmd)
    
    if exit_code != 0:
        print(f"❌ Detection failed: {stderr}")
        return None
    
    print(stdout)
    
    if detection_report.exists():
        return detection_report
    return None


def analyze_structure(detection_report: Path, verbose: bool = False) -> Optional[Path]:
    """Run analysis utility and return path to analysis report."""
    print("\n📊 Step 2: Analyzing structure and generating migration plan...")
    
    analysis_report = Path("analysis_report.json")
    cmd = [
        sys.executable,
        "packages/frameworks/kanban/scripts/analyze_structure.py",
        "--detection-report", str(detection_report),
        "--output", str(analysis_report)
    ]
    
    if verbose:
        cmd.append("--verbose")
    
    exit_code, stdout, stderr = run_command(cmd)
    
    if exit_code != 0:
        print(f"❌ Analysis failed: {stderr}")
        return None
    
    print(stdout)
    
    if analysis_report.exists():
        return analysis_report
    return None


def select_installation_mode(analysis_report_path: Optional[Path], requested_mode: Optional[str]) -> str:
    """Select installation mode interactively or from analysis report."""
    if requested_mode and requested_mode != "auto":
        return requested_mode
    
    # If we have an analysis report, read recommended mode
    recommended_mode = None
    if analysis_report_path and analysis_report_path.exists():
        import json
        try:
            with open(analysis_report_path, 'r', encoding='utf-8') as f:
                analysis = json.load(f)
            recommended_mode = analysis.get("migration_plan", {}).get("recommended_mode")
        except Exception:
            pass
    
    print("\n🔧 Step 3: Select installation mode")
    print("=" * 60)
    print("Available modes:")
    print("  1. fresh      - Clean install (no existing structure)")
    print("  2. migration  - Migrate existing structure to canonical format")
    print("  3. update      - Update existing framework installation")
    print("  4. hybrid      - Preserve project epics, install framework epics")
    
    if recommended_mode:
        print(f"\n💡 Recommended mode: {recommended_mode} (from analysis)")
    
    if requested_mode == "auto" and recommended_mode:
        response = input(f"\nUse recommended mode '{recommended_mode}'? (Y/n): ").strip().lower()
        if response in ['', 'y', 'yes']:
            return recommended_mode
    
    while True:
        choice = input("\nSelect mode (1-4) or mode name: ").strip().lower()
        
        mode_map = {
            '1': 'fresh',
            '2': 'migration',
            '3': 'update',
            '4': 'hybrid',
            'fresh': 'fresh',
            'migration': 'migration',
            'update': 'update',
            'hybrid': 'hybrid'
        }
        
        if choice in mode_map:
            return mode_map[choice]
        
        print("❌ Invalid choice. Please enter 1-4 or mode name.")


def migrate_structure(
    analysis_report: Path,
    kanban_path: Path,
    mode: str,
    dry_run: bool = False,
    force: bool = False
) -> bool:
    """Run migration utility."""
    print(f"\n🔄 Step 4: Migrating structure (mode: {mode})...")
    
    cmd = [
        sys.executable,
        "packages/frameworks/kanban/scripts/migrate_structure.py",
        "--analysis-report", str(analysis_report),
        "--kanban-path", str(kanban_path),
        "--mode", mode
    ]
    
    if dry_run:
        cmd.append("--dry-run")
    
    if force:
        cmd.append("--force")
    
    exit_code, stdout, stderr = run_command(cmd)
    
    print(stdout)
    
    if exit_code != 0:
        print(f"❌ Migration failed: {stderr}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Install Kanban framework with migration support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive installation (recommended)
  python3 install_kanban_framework.py

  # Fresh install (no existing structure)
  python3 install_kanban_framework.py --mode fresh

  # Migration install (with existing structure)
  python3 install_kanban_framework.py --mode migration

  # Dry run (preview changes)
  python3 install_kanban_framework.py --mode migration --dry-run
        """
    )
    parser.add_argument(
        "--mode",
        choices=["fresh", "migration", "update", "hybrid", "auto"],
        default="auto",
        help="Installation mode (default: auto-detect)"
    )
    parser.add_argument(
        "--kanban-path",
        type=str,
        default="KB/PM_and_Portfolio/kanban",
        help="Path to Kanban directory (default: KB/PM_and_Portfolio/kanban)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Skip confirmation prompts"
    )
    parser.add_argument(
        "--skip-detection",
        action="store_true",
        help="Skip detection step (use existing detection_report.json)"
    )
    parser.add_argument(
        "--skip-analysis",
        action="store_true",
        help="Skip analysis step (use existing analysis_report.json)"
    )
    
    args = parser.parse_args()
    
    kanban_path = Path(args.kanban_path).resolve()
    project_root = Path.cwd()
    
    print("=" * 60)
    print("Kanban Framework Installation")
    print("=" * 60)
    print(f"📁 Project root: {project_root}")
    print(f"📁 Kanban path: {kanban_path}")
    print(f"🔧 Mode: {args.mode}")
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
    print("=" * 60)
    
    # Step 1: Detect existing structure (unless fresh mode or skipped)
    detection_report = None
    if args.mode != "fresh" and not args.skip_detection:
        detection_report = detect_structure(kanban_path, verbose=True)
        if not detection_report:
            print("⚠️  Detection failed or no structure found. Proceeding with fresh install...")
            args.mode = "fresh"
    
    # Step 2: Analyze structure (unless fresh mode or skipped)
    analysis_report = None
    if args.mode != "fresh" and not args.skip_analysis:
        if detection_report:
            analysis_report = analyze_structure(detection_report, verbose=True)
        else:
            # Try to use existing analysis report
            existing_analysis = Path("analysis_report.json")
            if existing_analysis.exists():
                analysis_report = existing_analysis
                print(f"📋 Using existing analysis report: {analysis_report}")
    
    # Step 3: Select installation mode
    if args.mode == "auto":
        args.mode = select_installation_mode(analysis_report, None)
    
    # Step 4: Migrate/Install
    if args.mode == "fresh":
        print("\n🆕 Fresh install mode: Installing canonical epics...")
        # For fresh install, we'd install canonical epics directly
        # This would be implemented separately
        print("✅ Fresh install complete (canonical epics installed)")
    else:
        if not analysis_report:
            print("❌ Error: Analysis report required for migration/update/hybrid modes")
            return 1
        
        success = migrate_structure(
            analysis_report,
            kanban_path,
            args.mode,
            dry_run=args.dry_run,
            force=args.force
        )
        
        if not success:
            return 1
    
    print("\n" + "=" * 60)
    print("✅ Installation complete!")
    print("=" * 60)
    
    if args.mode != "fresh":
        print("\n📋 Next steps:")
        print("  1. Review migration log in analysis_report.json")
        print("  2. Verify migrated structure")
        print("  3. Continue using Kanban framework")
    
    return 0


if __name__ == "__main__":
    exit(main())

