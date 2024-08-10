from aiogram.filters import Filter
from aiogram import Bot, types

from database.models import Base

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from database.models import IdUser

from database.engine import engine
from database.orm import orm_id


class IsAdmin(Filter):
	def __init__(self):
		pass
	async def __call__(self,message: types.Message, bot:Bot):
		return message.from_user.id in bot.my_admins_list

class IsPrivate(Filter):
	
	def __init__(self):
		pass

	async def __call__(self,message: types.Message, bot:Bot,session: AsyncSession):
		listt = []
		f = str(message.from_user.id)
		for idd in await orm_id(session):
			listt.append(idd.iduser)
			print(listt)
		return f in listt

		
		
		
        