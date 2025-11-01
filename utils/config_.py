from pydantic_settings import BaseSettings

class LibConfig(BaseSettings):
    EMBEDDING_MODEL: str = "voyage-3.5-lite"
    EMBEDDING_OUT_DIMS: int = 1024
    DISTANCE_MATCH_THRESHOLD: int = -1

lib_config = LibConfig()