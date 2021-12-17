from sonarqube import SonarQubeClient


def delete_project(sonar: SonarQubeClient, project: dict) -> None:
    idle = sonar.projects.delete_project(project=project['key'])
    print(f'Project {project["name"]} removed.')
