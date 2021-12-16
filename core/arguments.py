import argparse

from config.constants import sonarqube_url


def create_parser():
    parser = argparse.ArgumentParser(description='Broken Minecraft seeds finder')
    parser.add_argument('-u', '--url', type=str, nargs=1, default=sonarqube_url,
                        help=f'SonarQube link. Default is {sonarqube_url}')
    parser.add_argument('-l', '--login', type=str,
                        help='SonarQube login')
    parser.add_argument('-p', '--password', type=str,
                        help='SonarQube password')
    parser.add_argument('-t', '--token', type=str,
                        help='SonarQube token')
    parser.add_argument('-n', '--project', type=str, default='',
                        help='Target SonarQube project')
    parser.add_argument('-j', '--json', default=False, action='store_true',
                        help='Data as json')
    return parser.parse_args()


arguments = create_parser()
