from sonarqube import SonarQubeClient


def get_issues(sonar: SonarQubeClient, project: dict, issues_type: str) -> list[dict]:
    issues = list(sonar.issues.search_issues(
        componentKeys=project['key'],
        s="SEVERITY",
        types=issues_type
    ))
    print(f'Found {len(issues)} issues')
    return issues
