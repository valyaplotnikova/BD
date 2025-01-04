from sqlalchemy import Column, Integer, String, ForeignKey

from book_store.models.database import Base


class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    city_id = Column(Integer, ForeignKey('city.city_id'))
    email = Column(String)
