"""
Data Science Projects Portfolio - Main Entry Point
A comprehensive showcase of data science and programming projects with interactive project selection.
"""

import os
import sys
from pathlib import Path
import importlib.util
import argparse
from datetime import datetime

# Add the repository root to Python path
REPO_ROOT = Path(__file__).parent
sys.path.append(str(REPO_ROOT))

class ProjectPortfolio:
    """Main portfolio class to manage and run multiple data science projects."""

    def __init__(self):
        self.repo_root = REPO_ROOT
        self.projects_dir = self.repo_root / "projects"
        self.available_projects = self.discover_projects()

    def discover_projects(self):
        """Automatically discover available projects."""
        projects = {}

        if not self.projects_dir.exists():
            return projects

        for project_dir in self.projects_dir.iterdir():
            if project_dir.is_dir():
                # Look for main.py in src/ directory (new modular structure)
                main_file = project_dir / "src" / "main.py"
                if main_file.exists():
                    projects[project_dir.name] = {
                        'path': project_dir,
                        'main_file': main_file,
                        'description': self.get_project_description(project_dir),
                        'type': 'modular'
                    }
                # Also check for notebook-based projects
                elif (project_dir / "notebook.ipynb").exists():
                    projects[project_dir.name] = {
                        'path': project_dir,
                        'main_file': project_dir / "notebook.ipynb",
                        'description': self.get_project_description(project_dir),
                        'type': 'notebook'
                    }

        return projects

    def get_project_description(self, project_dir):
        """Extract project description from README or main.py docstring."""
        readme_file = project_dir / "README.md"
        if readme_file.exists():
            try:
                with open(readme_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # Look for the first substantial line after title
                    for line in lines[1:10]:  # Check first 10 lines
                        stripped = line.strip()
                        if stripped and not stripped.startswith('#') and len(stripped) > 20:
                            return stripped
            except Exception:
                pass

        # Fallback to project name processing
        project_name = project_dir.name.replace('-', ' ').replace('_', ' ').title()
        return f"{project_name} - Data Science Project"

    def list_projects(self):
        """Display all available projects."""
        print("="*80)
        print("DATA SCIENCE PROJECTS PORTFOLIO")
        print("="*80)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Repository: {self.repo_root}")
        print(f"Total Projects: {len(self.available_projects)}")

        if not self.available_projects:
            print("\nNo projects found in the projects/ directory.")
            print("Make sure your projects are in: projects/[project-name]/src/main.py")
            print("Or notebook projects in: projects/[project-name]/notebook.ipynb")
            return

        print(f"\nAVAILABLE PROJECTS:")
        print("-" * 80)

        for i, (project_name, project_info) in enumerate(self.available_projects.items(), 1):
            project_type = project_info.get('type', 'unknown')
            type_indicator = "📁" if project_type == 'modular' else "📓" if project_type == 'notebook' else "❓"

            print(f"\n{i}. {type_indicator} {project_name.replace('-', ' ').title()}")
            print(f"   Description: {project_info['description']}")
            print(f"   Type: {project_type.title()}")
            print(f"   Location: {project_info['path'].relative_to(self.repo_root)}")

        print("\n" + "="*80)
        print("Legend: 📁 Modular Project | 📓 Notebook Project")

    def run_project(self, project_name):
        """Run a specific project."""
        if project_name not in self.available_projects:
            print(f"Error: Project '{project_name}' not found.")
            print(f"Available projects: {list(self.available_projects.keys())}")
            return False

        project_info = self.available_projects[project_name]
        project_path = project_info['path']
        main_file = project_info['main_file']
        project_type = project_info.get('type', 'unknown')

        print(f"Starting project: {project_name}")
        print(f"Project type: {project_type}")
        print(f"Project directory: {project_path}")
        print(f"Main file: {main_file}")
        print("-" * 60)

        if project_type == 'notebook':
            print("This is a Jupyter notebook project.")
            print(f"To run: jupyter notebook {main_file}")
            print("Opening notebook instructions printed above.")
            return True

        # Handle modular Python projects
        # Change to project directory
        original_cwd = os.getcwd()
        os.chdir(project_path)

        try:
            # Add project src to Python path
            src_path = project_path / "src"
            if str(src_path) not in sys.path:
                sys.path.insert(0, str(src_path))

            # Import and run the project's main module
            spec = importlib.util.spec_from_file_location("project_main", main_file)
            project_module = importlib.util.module_from_spec(spec)

            # Execute the project
            print(f"Loading project module: {project_name}")
            spec.loader.exec_module(project_module)

            # If the project has a main() function, call it
            if hasattr(project_module, 'main'):
                print(f"Executing main() function from {project_name}")
                project_module.main()
            else:
                print(f"Project {project_name} loaded successfully (no main() function found)")

            print(f"\n✅ Project '{project_name}' completed successfully!")

        except FileNotFoundError as e:
            print(f"❌ File not found error in project '{project_name}': {e}")
            print("Make sure all required data files are in place.")
            return False
        except ImportError as e:
            print(f"❌ Import error in project '{project_name}': {e}")
            print("Make sure all required dependencies are installed.")
            return False
        except Exception as e:
            print(f"❌ Error running project '{project_name}': {e}")
            return False

        finally:
            # Restore original working directory
            os.chdir(original_cwd)
            # Clean up sys.path
            if str(src_path) in sys.path:
                sys.path.remove(str(src_path))

        return True

    def interactive_mode(self):
        """Run portfolio in interactive mode."""
        while True:
            self.list_projects()

            if not self.available_projects:
                break

            print("\nINTERACTIVE MODE:")
            print("Enter project number, project name, or command:")
            print("• 'list' or 'l' - Show projects again")
            print("• 'quit' or 'q' - Exit")
            print("• 'help' or 'h' - Show help")

            choice = input("\nYour choice: ").strip().lower()

            if choice in ['quit', 'q', 'exit']:
                print("Goodbye! Thanks for exploring the portfolio!")
                break
            elif choice in ['list', 'l']:
                continue
            elif choice in ['help', 'h']:
                self.show_help()
                continue
            elif choice.isdigit():
                # Handle numeric selection
                try:
                    project_index = int(choice) - 1
                    project_names = list(self.available_projects.keys())
                    if 0 <= project_index < len(project_names):
                        project_name = project_names[project_index]
                        self.run_project(project_name)
                    else:
                        print(f"Invalid number. Choose 1-{len(project_names)}")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                # Handle project name
                # Try exact match first
                if choice in self.available_projects:
                    self.run_project(choice)
                else:
                    # Try partial match
                    matches = [name for name in self.available_projects.keys()
                              if choice in name.lower()]
                    if len(matches) == 1:
                        self.run_project(matches[0])
                    elif len(matches) > 1:
                        print(f"Multiple matches found: {matches}")
                        print("Please be more specific.")
                    else:
                        print(f"No project found matching '{choice}'")

            input("\nPress Enter to continue...")

    def show_help(self):
        """Show help information."""
        print("\n" + "="*60)
        print("HELP - Data Science Portfolio")
        print("="*60)
        print("This portfolio contains multiple data science projects.")
        print("\nHow to use:")
        print("• Run specific project: python main.py --project [project-name]")
        print("• Interactive mode: python main.py --interactive")
        print("• List projects: python main.py --list")
        print("\nProject Types:")
        print("📁 Modular Projects - Complete Python packages with src/ structure")
        print("📓 Notebook Projects - Jupyter notebook-based analyses")
        print("\nProject Structure:")
        print("projects/")
        print("├── project-name/")
        print("│   ├── src/main.py    ← Entry point (modular)")
        print("│   ├── notebook.ipynb ← Entry point (notebook)")
        print("│   ├── README.md")
        print("│   └── ...")
        print("\nSupported Commands in Interactive Mode:")
        print("• Project number (1, 2, 3...)")
        print("• Project name or partial name")
        print("• 'list' - Show all projects")
        print("• 'quit' - Exit")
        print("="*60)


def setup_argument_parser():
    """Setup command line argument parser."""
    parser = argparse.ArgumentParser(
        description='Data Science Projects Portfolio - Run multiple projects',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --list                              # List all projects
  python main.py --interactive                       # Interactive mode
  python main.py --project bank-term-deposit-prediction  # Run bank project
  python main.py --project churn-risk-intelligence   # Run churn project
  python main.py --project churn                     # Partial name matching
        """
    )

    parser.add_argument('--list', '-l', action='store_true',
                       help='List all available projects')

    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode')

    parser.add_argument('--project', '-p', type=str,
                       help='Run a specific project by name')

    parser.add_argument('--version', '-v', action='version',
                       version='Data Science Portfolio v2.0.0')

    return parser


def main():
    """Main function to run the portfolio."""
    portfolio = ProjectPortfolio()
    parser = setup_argument_parser()
    args = parser.parse_args()

    # If no arguments provided, show list and enter interactive mode
    if not any(vars(args).values()):
        portfolio.list_projects()
        if portfolio.available_projects:
            print("\nTip: Use --interactive for interactive mode, or --help for more options")
            choice = input("\nWould you like to enter interactive mode? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                portfolio.interactive_mode()
        return

    # Handle specific arguments
    if args.list:
        portfolio.list_projects()

    elif args.interactive:
        portfolio.interactive_mode()

    elif args.project:
        # Try exact match first
        if args.project in portfolio.available_projects:
            portfolio.run_project(args.project)
        else:
            # Try partial matching
            matches = [name for name in portfolio.available_projects.keys()
                      if args.project.lower() in name.lower()]
            if len(matches) == 1:
                print(f"Found partial match: '{matches[0]}'")
                portfolio.run_project(matches[0])
            elif len(matches) > 1:
                print(f"Multiple matches found: {matches}")
                print("Please be more specific or use --list to see all projects.")
            else:
                print(f"No project found matching '{args.project}'")
                print("Use --list to see all available projects.")


if __name__ == "__main__":
    print("Applied Science Projects Portfolio - Starting...")
    print(f"Repository root: {REPO_ROOT}")
    print("-" * 60)

    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPortfolio execution interrupted. Goodbye!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Please check your project structure and try again.")

