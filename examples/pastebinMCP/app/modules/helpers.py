import os


def getEnv(key: str, default: str | None = None) -> str:
    """
    Get the environment variable value.
    """
    value = os.getenv(key, default)
    
    if value is None:
        raise ValueError(f"Environment variable {key} not found")
    
    return value