#!/usr/bin/env python3
"""
Tool Management Script for dev-toolkit

Manages the collection of independent, self-contained tools while maintaining
separation of concerns. This script provides:
- Tool discovery and cataloging
- Validation of tool structure
- Registry maintenance
- Health checks

Each tool remains completely independent - this script only provides management
and discovery capabilities.
"""

import argparse
import json
import os
import subprocess
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class ToolManager:
    """Manages tools collection while maintaining tool independence."""
    
    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = repo_root or Path(__file__).parent.parent
        self.tools_dir = self.repo_root / "tools"
        self.registry_path = self.tools_dir / "tools-registry.yaml"
        
    def load_registry(self) -> Dict:
        """Load the tools registry."""
        if not self.registry_path.exists():
            return {"registry_version": "1.0.0", "tools": {}}
        
        with open(self.registry_path, 'r') as f:
            return yaml.safe_load(f) or {"registry_version": "1.0.0", "tools": {}}
    
    def save_registry(self, registry: Dict):
        """Save the tools registry."""
        registry["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        with open(self.registry_path, 'w') as f:
            yaml.dump(registry, f, default_flow_style=False, sort_keys=False)
    
    def discover_tools(self) -> List[str]:
        """Discover all tools in the tools directory."""
        tools = []
        if not self.tools_dir.exists():
            return tools
        
        for item in self.tools_dir.iterdir():
            if item.is_dir() and not item.name.startswith('_'):
                # Check if it looks like a tool (has README.md)
                if (item / "README.md").exists():
                    tools.append(item.name)
        
        return sorted(tools)
    
    def validate_tool(self, tool_name: str) -> Tuple[bool, List[str]]:
        """Validate a tool's structure and requirements."""
        errors = []
        tool_dir = self.tools_dir / tool_name
        
        if not tool_dir.exists():
            return False, [f"Tool directory does not exist: {tool_dir}"]
        
        # Check required files
        required_files = ["README.md"]
        for file in required_files:
            if not (tool_dir / file).exists():
                errors.append(f"Missing required file: {file}")
        
        # Check for entry point (Python script, shell script, etc.)
        entry_points = list(tool_dir.glob("*.py")) + list(tool_dir.glob("*.sh"))
        if not entry_points:
            errors.append("No entry point found (no .py or .sh files)")
        
        # Check requirements.txt if Python tool exists
        python_files = list(tool_dir.glob("*.py"))
        if python_files and not (tool_dir / "requirements.txt").exists():
            errors.append("Python tool missing requirements.txt")
        
        # Try to run --help if entry point exists
        if entry_points:
            entry_point = entry_points[0]
            try:
                if entry_point.suffix == ".py":
                    result = subprocess.run(
                        [sys.executable, str(entry_point), "--help"],
                        capture_output=True,
                        timeout=5,
                        cwd=tool_dir
                    )
                    if result.returncode != 0 and "--help" not in result.stderr.decode():
                        errors.append(f"Entry point {entry_point.name} may not support --help")
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass  # Not critical
        
        return len(errors) == 0, errors
    
    def check_tool_health(self, tool_name: str) -> Tuple[bool, List[str]]:
        """Perform health checks on a tool."""
        issues = []
        tool_dir = self.tools_dir / tool_name
        registry = self.load_registry()
        
        if tool_name not in registry.get("tools", {}):
            issues.append("Tool not registered in tools-registry.yaml")
        
        # Check if registry entry matches actual tool
        if tool_name in registry.get("tools", {}):
            tool_info = registry["tools"][tool_name]
            expected_dir = tool_info.get("directory", f"tools/{tool_name}")
            if expected_dir != f"tools/{tool_name}":
                issues.append(f"Registry directory mismatch: {expected_dir}")
        
        return len(issues) == 0, issues
    
    def list_tools(self, verbose: bool = False):
        """List all tools."""
        registry = self.load_registry()
        discovered = self.discover_tools()
        
        print(f"\n📦 Tools in dev-toolkit ({len(discovered)} found)\n")
        
        for tool_name in discovered:
            tool_info = registry.get("tools", {}).get(tool_name, {})
            status = tool_info.get("status", "unknown")
            description = tool_info.get("description", "No description")
            
            status_icon = "✅" if status == "active" else "📝" if status == "template" else "⚠️"
            
            print(f"{status_icon} {tool_name}")
            if verbose:
                print(f"   Description: {description}")
                print(f"   Status: {status}")
                if tool_info.get("tech_stack"):
                    print(f"   Tech Stack: {', '.join(tool_info['tech_stack'])}")
                print()
            else:
                print(f"   {description}\n")
    
    def validate_all(self):
        """Validate all tools."""
        tools = self.discover_tools()
        print(f"\n🔍 Validating {len(tools)} tools...\n")
        
        all_valid = True
        for tool_name in tools:
            is_valid, errors = self.validate_tool(tool_name)
            status_icon = "✅" if is_valid else "❌"
            print(f"{status_icon} {tool_name}")
            
            if errors:
                all_valid = False
                for error in errors:
                    print(f"   ⚠️  {error}")
            print()
        
        return all_valid
    
    def update_registry(self, force: bool = False):
        """Update registry with discovered tools."""
        registry = self.load_registry()
        discovered = self.discover_tools()
        
        if "tools" not in registry:
            registry["tools"] = {}
        
        updated = False
        for tool_name in discovered:
            tool_dir = self.tools_dir / tool_name
            
            if tool_name not in registry["tools"] or force:
                # Read basic info from README if available
                readme_path = tool_dir / "README.md"
                description = "No description"
                
                if readme_path.exists():
                    with open(readme_path, 'r') as f:
                        lines = f.readlines()
                        # Try to extract description from first few lines
                        for line in lines[:10]:
                            if line.strip() and not line.startswith('#'):
                                description = line.strip()[:100]
                                break
                
                # Detect tech stack
                tech_stack = []
                if list(tool_dir.glob("*.py")):
                    tech_stack.append("Python")
                if list(tool_dir.glob("*.sh")):
                    tech_stack.append("Shell")
                if list(tool_dir.glob("*.js")):
                    tech_stack.append("JavaScript")
                if list(tool_dir.glob("*.ts")):
                    tech_stack.append("TypeScript")
                
                # Find entry point
                entry_points = list(tool_dir.glob("*.py")) + list(tool_dir.glob("*.sh"))
                entry_point = entry_points[0].name if entry_points else None
                
                registry["tools"][tool_name] = {
                    "name": tool_name.replace("-", " ").title(),
                    "description": description,
                    "directory": f"tools/{tool_name}",
                    "tech_stack": tech_stack or ["Unknown"],
                    "entry_point": entry_point,
                    "dependencies_file": "requirements.txt" if list(tool_dir.glob("*.py")) else None,
                    "status": "active",
                    "maintainer": "earlution",
                    "added": datetime.now().strftime("%Y-%m-%d"),
                    "last_validated": datetime.now().strftime("%Y-%m-%d"),
                    "metadata": {
                        "tags": [],
                        "documentation": f"tools/{tool_name}/README.md"
                    }
                }
                updated = True
        
        if updated:
            self.save_registry(registry)
            print("✅ Registry updated successfully")
        else:
            print("ℹ️  Registry already up to date")
    
    def show_tool_info(self, tool_name: str):
        """Show detailed information about a tool."""
        registry = self.load_registry()
        tool_info = registry.get("tools", {}).get(tool_name)
        
        if not tool_info:
            print(f"❌ Tool '{tool_name}' not found in registry")
            return
        
        print(f"\n📦 {tool_info['name']} ({tool_name})\n")
        print(f"Description: {tool_info.get('description', 'N/A')}")
        print(f"Status: {tool_info.get('status', 'N/A')}")
        print(f"Directory: {tool_info.get('directory', 'N/A')}")
        print(f"Tech Stack: {', '.join(tool_info.get('tech_stack', []))}")
        print(f"Entry Point: {tool_info.get('entry_point', 'N/A')}")
        print(f"Maintainer: {tool_info.get('maintainer', 'N/A')}")
        print(f"Added: {tool_info.get('added', 'N/A')}")
        print(f"Last Validated: {tool_info.get('last_validated', 'N/A')}")
        
        if tool_info.get('metadata', {}).get('tags'):
            print(f"Tags: {', '.join(tool_info['metadata']['tags'])}")
        
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Manage dev-toolkit tools collection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s list                    # List all tools
  %(prog)s list --verbose          # List with details
  %(prog)s validate                # Validate all tools
  %(prog)s update-registry         # Update registry with discovered tools
  %(prog)s info github-badges      # Show tool information
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all tools')
    list_parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed information')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate all tools')
    
    # Update registry command
    update_parser = subparsers.add_parser('update-registry', help='Update tools registry')
    update_parser.add_argument('-f', '--force', action='store_true', help='Force update all entries')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show tool information')
    info_parser.add_argument('tool_name', help='Name of the tool')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    manager = ToolManager()
    
    try:
        if args.command == 'list':
            manager.list_tools(verbose=args.verbose)
        elif args.command == 'validate':
            is_valid = manager.validate_all()
            sys.exit(0 if is_valid else 1)
        elif args.command == 'update-registry':
            manager.update_registry(force=args.force)
        elif args.command == 'info':
            manager.show_tool_info(args.tool_name)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

