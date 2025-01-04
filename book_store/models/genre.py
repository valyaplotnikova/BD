from sqlalchemy import Column, Integer, String

from book_store.models.database import Base


class Genre(Base):
    __tablename__ = 'genre'

    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)
