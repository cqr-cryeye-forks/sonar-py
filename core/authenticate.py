from sonarqube import SonarQubeClient

from config.constants import sonarqube_url


def init_sonar(username: str = None, password: str = None, token: str = None) -> SonarQubeClient:
    if token:
        return SonarQubeClient(sonarqube_url=sonarqube_url, token=token)
    return SonarQubeClient(sonarqube_url=sonarqube_url, username=username, password=password)
