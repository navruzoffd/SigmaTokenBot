from sqlalchemy import Column, Integer, String, BigInteger, Boolean
from database import Base

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, nullable=False)
    id_tg = Column(BigInteger, nullable=False)
    username_tg = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    invited = Column(String)
    referrals = Column(Integer, default=0)
    complite_tasks = Column(Boolean, default=False)
    task_msg = Column(BigInteger)