# pyepfa.py

# Import necessary packages
import os
import shutil
from config import *
from GitPython import Repo
from sphinx.quickstart import generate

# Function to create project structure
def create_project_structure(project_parameters):
    # Create the project directory
    os.makedirs(project_parameters['project_directory'], exist_ok=True)

    # Copy the template directory to the project directory
    template_dir = os.path.join(TEMPLATES_DIR, project_parameters['template_name'])
    shutil.copytree(template_dir, project_parameters['project_directory'])

# Function to initialize version control
def initialize_version_control(version_control_parameters):
    # Initialize a new Git repository
    repo = Repo.init(version_control_parameters['git']['repository_url'])

    # Create a new branch
    repo.create_head(version_control_parameters['git']['branch'])

# Function to generate documentation
def generate_documentation(documentation_parameters):
    # Generate Sphinx documentation
    generate(documentation_parameters['sphinx']['conf_dir'], documentation_parameters['sphinx']['build_dir'])

# Main function
def main():
    # Create the project structure
    create_project_structure(DEFAULT_PROJECT_PARAMETERS)

    # Initialize version control
    initialize_version_control(VERSION_CONTROL_PARAMETERS)

    # Generate documentation
    if DEFAULT_PROJECT_PARAMETERS['documentation']:
        generate_documentation(DOCUMENTATION_PARAMETERS)

# Run the main function
if __name__ == "__main__":
    main()
