# отсюда alembic берет данные о моделях
# import Base from db.base прописать в env.py alembic
from db.session import Base

__all__ = [
    Base,
]
