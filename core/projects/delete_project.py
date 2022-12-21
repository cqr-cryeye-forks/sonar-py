import datetime

from sonarqube import SonarQubeClient

from core.projects.get_all_projects import get_all_projects


def delete_project(sonar: SonarQubeClient, project: dict) -> None:
    idle = sonar.projects.delete_project(project=project['key'])
    print(f'Project {project["name"]} removed.')


def remove_all_private_projects(sonar: SonarQubeClient):
    projects = get_all_projects(sonar=sonar)
    for project in projects:
        if project['visibility'] == 'private':
            delete_project(sonar=sonar, project=project)


def clean_whitebox_projects(sonar: SonarQubeClient, delete_age: int = 30):
    """
    :param delete_age: how mane days can old project exist before deleting
    :param sonar: SonarQube client
    """
    projects = get_all_projects(sonar=sonar)
    print('Cleaning old junk projects...')
    for project in projects:
        name = project['key']
        if 'whitebox_' in name:
            creating_date: str = name.split('_', 2)[-2]
            if creating_date == 'whitebox':
                delete_project(sonar=sonar, project=project)  # old projects without info creation date
                continue
            else:
                try:
                    project_age = datetime.date.today() - datetime.datetime.strptime(creating_date, '%Y-%m-%d').date()
                    if project_age.days > delete_age:
                        delete_project(sonar=sonar, project=project)
                        continue
                except Exception as e:
                    print(f'Parse error: {e}')
        print(f"Project {name} skipped")
    print('Cleaning old junk projects finished')
