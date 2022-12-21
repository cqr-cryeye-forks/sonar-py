import json
import subprocess

import requests

from core import arguments


def run_scanner(target_project: str, token: str, target_path: str) -> list[str]:
    # java_jdk = os.getenv('JAVA_HOME')
    # if not java_jdk:
    #     java_jdk = os.getenv('JDK_HOME')
    # java_binaries = subprocess.run(['which', 'java'])
    try:
        result = subprocess.run(
            ['sonar-scanner',
             f'-Dsonar.projectKey={target_project}',
             '-Dsonar.sources=.',
             f'-Dsonar.host.url={arguments.url}',
             f'-Dsonar.login={token}',
             '-Dsonar.exclusions=**/*.java',
             '-Dsonar.c.file.suffixes=-',
             '-Dsonar.cpp.file.suffixes=-',
             '-Dsonar.objc.file.suffixes=-',
             # f'-Dsonar.java.jdkHome={java_jdk}',
             # f'-Dsonar.java.binaries={java_binaries}',
             ],
            cwd=target_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        run_data = result.stdout.decode()
        errors = result.stderr.decode()
        print(run_data)
        errors_list = errors.splitlines()
        if "More about the report processing at" in run_data:
            data_link = run_data.split('More about the report processing at ', 1)[-1].split('\n', 1)[0]
            session = requests.Session()
            session.auth = (token, '')
            link_data = session.get(url=data_link)
            if link_data.status_code == 200:
                content = json.loads(link_data.content.decode())
                if error_message := content.get('task', {}).get('errorMessage'):
                    errors_list.append(error_message)
            else:
                errors_list.append(f"Can't check results. Error code: {link_data.status_code}")

        print("Errors:")
        for err in errors_list:
            print(err)
        return errors_list
    except FileNotFoundError:
        print('sonar-scanner not found')
        return ['sonar-scanner not found']
