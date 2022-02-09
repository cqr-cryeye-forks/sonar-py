import uuid


def generate_random_name() -> str:
    return 'whitebox_' + uuid.uuid4().hex
