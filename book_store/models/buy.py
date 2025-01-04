from sqlalchemy import Column, Integer, ForeignKey, Text

from book_store.models.database import Base


class Buy(Base):
    __tablename__ = 'buy'

    buy_id = Column(Integer, primary_key=True)
    buy_description = Column(Text)
    client_id = Column(Integer, ForeignKey('client.client_id'))
