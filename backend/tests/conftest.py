"""
Session-scoped test configuration.

Replaces the global SQLAlchemy async engine with a NullPool engine so that
each DB operation gets a fresh connection. This prevents asyncpg
"another operation is in progress" errors that occur when TestClient (which
spawns its own event loop in a thread) and async test fixtures both draw from
the same connection pool.
"""
import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.config import settings


@pytest.fixture(scope="session", autouse=True)
def patch_db_engine():
    import app.db.database as db_module
    import app.services.tools.ticket_tools as tt_module

    engine = create_async_engine(settings.database_url, poolclass=NullPool, echo=False)
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    db_module.engine = engine
    db_module.async_session = session_factory
    tt_module.async_session = session_factory
    yield
