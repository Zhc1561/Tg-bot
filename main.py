import os
import asyncio

from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from middlewares.db import DataBaseSession

from database.engine import create_db, drop_db, session_maker

from handlers.admin_private import admin_router

from handlers.user_private import user_private_router

from handlers.privelegy_user import privat_router

from common.bot_cmds_list import private

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token = os.getenv('TOKEN'))
bot.my_admins_list = [856606995,]
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(admin_router)
dp.include_router(privat_router)
async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()

async def on_shutdown(bot):
    print('бот лёг')

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope = types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())