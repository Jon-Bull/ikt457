# config.py
# Define the root directory of the project
import os

# Define paths for various directories based on the root directory
def get_paths(IN_COLAB=False):
    # Root 
	PATH_PROJECT_ROOT = '/content/drive/MyDrive/ikt457' if IN_COLAB else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	# Assignments
	PATH_ASSIGNMENTS = os.path.join(PATH_PROJECT_ROOT, "assignments")
 
	# Common
	PATH_COMMON = os.path.join(PATH_PROJECT_ROOT, "common")
	PATH_COMMON_DATASETS = os.path.join(PATH_COMMON, "datasets")
	PATH_COMMON_NOTEBOOKS = os.path.join(PATH_COMMON, "notebooks")
	PATH_COMMON_RESOURCES = os.path.join(PATH_COMMON, "resources")
	PATH_COMMON_SCRIPTS = os.path.join(PATH_COMMON, "scripts")
 
	# Reports
	PATH_REPORTS = os.path.join(PATH_PROJECT_ROOT, "reports")

	# Src
	PATH_SRC = os.path.join(PATH_PROJECT_ROOT, "src")
 
	# Return all paths in a dictionary
	return {
        'PATH_PROJECT_ROOT': PATH_PROJECT_ROOT,
        'PATH_ASSIGNMENTS': PATH_ASSIGNMENTS,
        'PATH_COMMON': PATH_COMMON,
        'PATH_COMMON_DATASETS': PATH_COMMON_DATASETS,
        'PATH_COMMON_NOTEBOOKS': PATH_COMMON_NOTEBOOKS,
        'PATH_COMMON_RESOURCES': PATH_COMMON_RESOURCES,
        'PATH_COMMON_SCRIPTS': PATH_COMMON_SCRIPTS,
        'PATH_REPORTS': PATH_REPORTS,
        'PATH_SRC': PATH_SRC,
        'PATH_1_LEARNING_AUTOMATA_GAME': os.path.join(PATH_ASSIGNMENTS, '1_learning_automata_game'),
    }