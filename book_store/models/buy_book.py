from sqlalchemy import Column, Integer, ForeignKey
from book_store.models.database import Base


class BuyBook(Base):
    __tablename__ = 'buy_book'

    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.buy_id'))
    book_id = Column(Integer, ForeignKey('book.book_id'))
    amount = Column(Integer)
