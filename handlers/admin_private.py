from aiogram import F, Router, types
from aiogram.filters import Command
from kbds import reply

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

@user_private_router.message(Command('admin'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как админ!',reply_markup = reply.start_kb_admin)