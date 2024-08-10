from aiogram import F, Router, types
from aiogram.filters import Command,StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from filters.chat_types import IsPrivate
from kbds import reply

privat_router = Router()
privat_router.message.filter(IsPrivate())


@privat_router.message(Command('user_private'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как довереный пользователь!',reply_markup = reply.start_kb_private_user)