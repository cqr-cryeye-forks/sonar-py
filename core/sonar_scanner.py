import os
import subprocess

from core import arguments


def run_scanner(target_project: str, token: str, target_path: str):
    # java_jdk = os.getenv('JAVA_HOME')
    # if not java_jdk:
    #     java_jdk = os.getenv('JDK_HOME')
    # java_binaries = subprocess.run(['which', 'java'])
    try:
        output = subprocess.run(
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
        )
    except FileNotFoundError:
        print('sonar-scanner not found')
