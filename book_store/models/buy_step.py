from sqlalchemy import Column, Integer, ForeignKey, Date
from book_store.models.database import Base


class BuyStep(Base):
    __tablename__ = 'buy_step'

    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.buy_id'))
    step_id = Column(Integer, ForeignKey('step.step_id'))
    date_step_beg = Column(Date)
    date_step_end = Column(Date)
