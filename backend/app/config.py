from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_BACKEND_DIR = Path(__file__).resolve().parent.parent  # always backend/


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # OpenAI
    openai_api_key: str

    # Database
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/devsupport"

    # ChromaDB
    chroma_persist_dir: str = str(_BACKEND_DIR / "chroma_db")
    chroma_collection_name: str = "stripe_docs"

    # LLM settings
    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    # App settings
    log_level: str = "INFO"
    environment: str = "development"


settings = Settings()
