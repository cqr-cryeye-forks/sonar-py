import datetime
import uuid


def generate_random_name() -> str:
    return f'whitebox_{datetime.date.today()}_{uuid.uuid4().hex}'
