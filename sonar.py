from core import arguments
from core.authenticate import init_sonar
from core.export import export_issues
from core.projects import get_project
from core.projects.get_issues import get_issues


def main():
    print(f'Sonar link: {arguments.url}')
    sonar = init_sonar()
    target_project = get_project(sonar=sonar, project_name=arguments.project)
    issues = get_issues(sonar=sonar, project=target_project)
    export_issues(issues=issues)


if __name__ == '__main__':
    main()
