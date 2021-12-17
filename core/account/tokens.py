from sonarqube import SonarQubeClient


def generate_new_token(sonar: SonarQubeClient, token_name: str) -> dict:
    user_token = sonar.user_tokens.generate_user_token(token_name)
    print(f'New token generated: {user_token}')
    return user_token


def delete_token(sonar: SonarQubeClient, token_name: str):
    sonar.user_tokens.revoke_user_token(token_name)
    print(f'Token removed: {token_name}')
