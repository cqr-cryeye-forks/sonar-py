from time import sleep

from core import arguments
from core.account.tokens import generate_new_token, delete_token
from core.authenticate import init_sonar
from core.export import export_issues
from core.projects import get_project
from core.projects.delete_project import delete_project, clean_whitebox_projects
from core.projects.get_issues import get_issues
from core.projects.get_results import get_results
from core.sonar_scanner import run_scanner


def main():
    print(f'Sonar link: {arguments.url}')
    sonar = init_sonar()
    if arguments.remove_old:
        clean_whitebox_projects(sonar=sonar, delete_age=arguments.delete_time)
    else:
        print('Cleaning old projects skipped.')
    token = arguments.token
    target_path = arguments.scan
    target_project = get_project(sonar=sonar, project_name=arguments.project)
    need_to_delete_token = False
    if not token:
        token = generate_new_token(sonar=sonar, token_name=target_project['key'])['token']
        need_to_delete_token = True
    print(f'Path for scanning: {target_path}')
    errors = run_scanner(target_project=target_project['name'], token=token, target_path=target_path)
    print('Wait a bit for results')
    sleep(30)
    issues = get_issues(sonar=sonar, project=target_project, issues_type=arguments.issues_type)
    scan_data, errors_ = get_results(project=target_project, token=token, sonar_url=arguments.url.removesuffix('/'))
    errors.extend(errors_)
    export_issues(issues=issues, errors=errors, scan_data=scan_data)
    if need_to_delete_token:
        delete_token(sonar=sonar, token_name=target_project['key'])
    if arguments.delete:
        delete_project(sonar=sonar, project=target_project)


if __name__ == '__main__':
    main()
