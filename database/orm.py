
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from database.models import IdUser


async def orm_add_id(session: AsyncSession, data : dict):
        obj = IdUser(
                iduser = data["user_add_id"]
        )
        session.add(obj)
        await session.commit()

async def orm_delete_id(session: AsyncSession, iduser: int):
        query = delete(IdUser).where(IdUser.id == iduser)
        await session.execute(query)
        await session.commit()
        
async def orm_id(session: AsyncSession):
        query = select(IdUser)
        r = await session.execute(query)
        return r.scalars().all()

