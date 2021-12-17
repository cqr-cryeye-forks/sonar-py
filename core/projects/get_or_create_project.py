from sonarqube import SonarQubeClient

from core.projects.create_project import create_project
from core.utils.randomizer import generate_random_name


def get_project(sonar: SonarQubeClient, project_name: str = ''):
    if not project_name:
        project_name = generate_random_name()
    print(f'Search for project: {project_name}')

    projects = list(sonar.projects.search_projects(projects=project_name))
    if not projects:
        print(f'Project "{project_name}" not found. Creating new project with this name...')
        projects = create_project(sonar=sonar, project=project_name, name=project_name)
    target_project = projects[0]['project']
    print(f'Target project: {target_project["name"]}')
    return target_project
