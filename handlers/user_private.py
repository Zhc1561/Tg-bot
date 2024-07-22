from aiogram.filters import CommandStart, Command
from aiogram import types, Router
from kbds import reply

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет я Бот! Авторизируйтесь как админ или как авторизированный пользователь,воспользовавшись моим меню. Вы можете продолжить сессию без авторизации, командой /next.', reply_markup = reply.start_kb_start)


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Обо мне:')


@user_private_router.message(Command('user_private'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как довереный пользователь!',reply_markup = reply.start_kb_private_user)

@user_private_router.message(Command('next'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как неавторезированый пользователь!',reply_markup = reply.start_kb_user)   

   

@user_private_router.message(Command('exit'))
async def start_cmd(message: types.Message):
    await message.answer('Привет я Бот! Авторизируйтесь как админ или как авторизированный пользователь,воспользовавшись моим меню. Вы можете продолжить сессию без авторизации, командой /next.', reply_markup = reply.start_kb_start)
 