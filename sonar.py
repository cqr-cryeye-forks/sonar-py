from core import arguments
from core.account.tokens import generate_new_token, delete_token
from core.authenticate import init_sonar
from core.export import export_issues
from core.projects import get_project
from core.projects.delete_project import delete_project
from core.projects.get_issues import get_issues


def main():
    print(f'Sonar link: {arguments.url}')
    sonar = init_sonar()
    token = arguments.token
    target_path = arguments.scan
    need_to_delete_token = False
    if not token:
        token = generate_new_token(sonar=sonar, token_name=target_project['key'])['token']
        need_to_delete_token = True
    print(f'Path for scanning: {target_path}')
    target_project = get_project(sonar=sonar, project_name=arguments.project)

    run_scanner(target_project=target_project['name'], token=token, target_path=target_path)
    issues = get_issues(sonar=sonar, project=target_project)
    export_issues(issues=issues)
    if need_to_delete_token:
        delete_token(sonar=sonar, token_name=target_project['key'])
    if arguments.delete:
        delete_project(sonar=sonar, project=target_project)


if __name__ == '__main__':
    main()
