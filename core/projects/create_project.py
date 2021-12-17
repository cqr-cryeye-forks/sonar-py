from sonarqube import SonarQubeClient


def create_project(sonar: SonarQubeClient, project: str, name: str, visibility: str = "private") -> list[dict]:
    project = project.replace(' ', '_')
    print(f'New project info:\nProject: {project}\nName: {name}\nVisibility: {visibility}')
    return [sonar.projects.create_project(project=project, name=name, visibility=visibility)]
