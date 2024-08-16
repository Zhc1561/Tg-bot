from aiogram import F, Router, types
from aiogram.filters import Command,StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from database.orm import orm_add_id, orm_delete_id, orm_id


from filters.chat_types import IsAdmin
from kbds import reply

admin_router = Router()
admin_router.message.filter(IsAdmin())





@admin_router.message(Command('admin'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как админ!',reply_markup = reply.start_kb_admin)

class AddUser(StatesGroup):
    user_add_id = State()

class RemoveUser(StatesGroup):
    user_delet_id = State()



@admin_router.message(StateFilter(None),Command('add_private_user'))
async def add_private_user(message: types.Message, state: FSMContext):
    await message.answer('Введите id пользователя, которому хотите дать привелегию авторизированного пользователя.')

    await state.set_state(AddUser.user_add_id)

@admin_router.message(AddUser.user_add_id)
async def user_private(message: types.Message, state: FSMContext,session = AsyncSession):
    await message.answer('Вы добавили пользователя')
    await state.update_data(user_add_id=message.text)
    data = await state.get_data()

    await orm_add_id(session, data)

    await state.clear()
    

@admin_router.message(StateFilter(None),Command('remove_private_user'))
async def remove_private_user(message: types.Message, state: FSMContext):
    await message.answer('Введите БД-id пользователя, которого хотите удалить')

    await state.set_state(RemoveUser.user_delet_id)

@admin_router.message(RemoveUser.user_delet_id)
async def user_private(message: types.Message, state: FSMContext, session = AsyncSession):
    await message.answer('Вы удалили пользователя!')
    await state.update_data(user_delet_id=message.text)
    data = await state.get_data()
    iduser = int(data["user_delet_id"])

    await orm_delete_id(session, iduser)

    

    await state.clear()
    
@admin_router.message(Command('all_users'))
async def users(message: types.Message,session = AsyncSession):
    for idd in await orm_id(session):
        await message.answer('БД-id: '+str(idd.id)+' Telegram-id: '+str(idd.iduser))
    
    await message.answer('Вот список всех доверенных пользователей.')

@admin_router.message(Command('help_a'))
async def user_a(message: types.Message):
    await message.answer('''Вам доступны 4 команды:
        1. /add_private_user - добавить доверенного пользователя.
        2. /remove_private_user - удалить доверенного пользователя.
        3. /all_users - просмотреть список всех доверенных пользователей.
        4. /exit - выйти.
        ''')