from sonarqube import SonarQubeClient


def get_issues(sonar: SonarQubeClient, project: dict) -> list[dict]:
    issues = list(sonar.issues.search_issues(
        componentKeys=project['key'],
        additionalFields='_all',
        s="SEVERITY",
        resolved=False))
    print(f'Found {len(issues)} issues')
    return issues
