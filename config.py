# config.py

# Import necessary packages
import os
from pathlib import Path

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent

# Define the directory for the project templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Define the default project parameters
DEFAULT_PROJECT_PARAMETERS = {
    'project_name': 'MyProject',
    'project_directory': BASE_DIR,
    'template_name': 'default',
    'version_control': 'git',
    'documentation': True,
}

# Define the AI optimization parameters
AI_OPTIMIZATION_PARAMETERS = {
    'algorithm': 'genetic',
    'population_size': 100,
    'mutation_rate': 0.01,
    'max_generations': 1000,
}

# Define the version control parameters
VERSION_CONTROL_PARAMETERS = {
    'git': {
        'repository_url': 'https://github.com/your-username/MyProject.git',
        'branch': 'main',
    },
}

# Define the documentation parameters
DOCUMENTATION_PARAMETERS = {
    'sphinx': {
        'conf_dir': os.path.join(BASE_DIR, 'docs'),
        'build_dir': os.path.join(BASE_DIR, 'docs', '_build'),
    },
}
