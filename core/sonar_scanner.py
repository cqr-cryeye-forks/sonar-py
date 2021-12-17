import subprocess

from core import arguments


def run_scanner(target_project: str, token: str, target_path: str):
    try:
        output = subprocess.run(
            ['sonar-scanner',
             f'-Dsonar.projectKey={target_project}',
             '-Dsonar.sources=.',
             f'-Dsonar.host.url={arguments.url}',
             f'-Dsonar.login={token}',
             ],
            cwd=target_path,
        )
    except FileNotFoundError:
        print('sonar-scanner not found')
