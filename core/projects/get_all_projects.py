from sonarqube import SonarQubeClient


def get_all_projects(sonar: SonarQubeClient):
    return list(sonar.projects.search_projects())
