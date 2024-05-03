from models import Users
from dao.base import BaseDAO
from database import async_session_maker
from sqlalchemy import update

class UserDAO(BaseDAO):
    model = Users

    @classmethod
    async def update_by_id_tg(cls, id_tg, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id_tg == id_tg).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def task_reward(cls, id_tg, value):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id_tg == id_tg).values(complite_tasks = True, balance = cls.model.balance + value)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def referral_reward(cls, referrer_id):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id_tg == referrer_id).values(
                balance = cls.model.balance + 100,
                referrals = cls.model.referrals + 1
                )
            await session.execute(query)
            await session.commit()