from core import arguments
from core.authenticate import init_sonar


def main():
    sonar_host = arguments.url
    login = arguments.login
    password = arguments.password
    token = arguments.token
    print(f'Sonar link: {sonar_host}')
    if not arguments.login and not password and not token:
        print('Please specify Account details. Use login/password or token arguments')
        exit(0)
    elif token and login and password:
        print('Too many Account details. Do not use login/password and token arguments.')
        exit(0)
    if token:
        print(f"Using token '{token}'")
        sonar = init_sonar(token=token)
    else:
        if not password:
            password = input('Please specify user password: ')
        print(f'{login=}\n{password=}')
        sonar = init_sonar(username=login, password=password)
    print(list(sonar.issues.search_issues(componentKeys=arguments.project, branch="develop")))

if __name__ == '__main__':
    main()
