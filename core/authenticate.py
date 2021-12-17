import json

import requests
from sonarqube import SonarQubeClient

from core import arguments


def init_sonar(username: str = arguments.login,
               password: str = arguments.password,
               token: str = arguments.token) -> SonarQubeClient:
    if not username and not password and not token:
        print('Please specify Account details. Use login/password or token arguments')
        exit(0)
    elif token and username and password:
        print('Too many Account details. Do not use login/password and token arguments.')
        exit(0)
    if username and not password:
        password = input('Please specify user password: ')
    try:
        sonar = SonarQubeClient(sonarqube_url=arguments.url, username=username, password=password, token=token)
        if 'true' in sonar.auth.check_credentials():
            print('Authentication success')
            return sonar
        print('Authentication error. Check your input data')
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError) as e:
        print(f'Connection with SonarQube error. Check link or connection. \nError: {e}')
    exit(0)
