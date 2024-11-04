from dotenv import load_dotenv
import os

load_dotenv()


def get_env_variable(key: str, default: str = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value
