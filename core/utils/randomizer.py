import uuid


def generate_random_name() -> str:
    return uuid.uuid4().hex
