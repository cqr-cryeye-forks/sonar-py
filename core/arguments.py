import argparse

from config.constants import sonarqube_url


def create_parser():
    parser = argparse.ArgumentParser(description='Broken Minecraft seeds finder')
    parser.add_argument('-u', '--url', type=str, default=sonarqube_url,
                        help=f'SonarQube link. Default is {sonarqube_url}')
    parser.add_argument('-l', '--login', type=str, default=None,
                        help='SonarQube login')
    parser.add_argument('-p', '--password', type=str, default=None,
                        help='SonarQube password')
    parser.add_argument('-t', '--token', type=str, default=None,
                        help='SonarQube token')
    parser.add_argument('-n', '--project', type=str,  default=None,
                        help='Target SonarQube project')
    parser.add_argument('-o', '--output', type=str,  default=None,
                        help='Output file for data')
    parser.add_argument('-j', '--json', default=False, action='store_true',
                        help='Data as json')
    parser.add_argument('-d', '--delete', default=False, action='store_true',
                        help='Remove project in the end')
    return parser.parse_args()


arguments = create_parser()
