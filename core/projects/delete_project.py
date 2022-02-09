from sonarqube import SonarQubeClient

from core.projects.get_all_projects import get_all_projects


def delete_project(sonar: SonarQubeClient, project: dict) -> None:
    idle = sonar.projects.delete_project(project=project['key'])
    print(f'Project {project["name"]} removed.')


def remove_all_projects(sonar: SonarQubeClient):
    projects = get_all_projects(sonar=sonar)
    for project in projects:
        if project['visibility'] == 'private':
            delete_project(sonar=sonar, project=project)


def clean_whitebox_projects(sonar: SonarQubeClient):
    projects = get_all_projects(sonar=sonar)
    print('Cleaning old junk projects...')
    for project in projects:
        if 'whitebox_' in project['key']:
            delete_project(sonar=sonar, project=project)
    print('Cleaning old junk projects finished')
