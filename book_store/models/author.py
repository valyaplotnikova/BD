from sqlalchemy import Column, Integer, String

from book_store.models.database import Base


class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)
