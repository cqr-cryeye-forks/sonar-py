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
# sonar-scanner
# -Dsonar.projectKey=test-target
# -Dsonar.sources=.
# -Dsonar.host.url=https://7de1-195-138-83-98.ngrok.io
# -Dsonar.login=2521e30c25052df055485af0f086bbc4012fb4bd
