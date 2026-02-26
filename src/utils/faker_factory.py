from faker import Faker

fake = Faker()


def random_email(prefix: str = "qa") -> str:
    return f"{prefix}_{fake.uuid4()}@example.com"


def random_name() -> str:
    return fake.name()
