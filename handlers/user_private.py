from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_private_router = Router()
password_user_private = ['123','321']

ADMIN = False
USER = False

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет я Бот! Давайте определим кто вы, выберите команду /admin, если вы админ или /user_private если вы авторизированный пользователь. Если у вас ещё нет прав, вы можете продолжить как неавтаризированный пользователь, написав команду /user')

@user_private_router.message(Command('user_private'))
async def user_private(message: types.Message):
    await message.answer('Введите пароль!')
    async def user_privated(message: types.Message):
        if message.text in password_user_private:
            USER = True
            await message.answer('Вы авторизировались как user_private. Введите команду /menu, чтобы использовать мой функционал или /exit для того чтобы завершить сессию user_private')
        else:
            await message.answer('Вы ввели неверный пароль!')

@user_private_router.message(Command('menu'))
async def menu_user_private(message: types.Message):
    await message.answer('Вот меню: ')

    
#@user_private_router.message(Command('user'))
#async def echo(message: types.Message):
#    if message.text == admin:
#        ADMIN = True
#        await message.answer('Вы авторизировались как админ')
   