from aiogram import F, Router, types
from aiogram.filters import Command,StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from filters.chat_types import IsAdmin
from kbds import reply

admin_router = Router()
admin_router.message.filter(IsAdmin())

user_private_list = []

@admin_router.message(Command('admin'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как админ!',reply_markup = reply.start_kb_admin)

class AddUser(StatesGroup):
    user_add_id = State()

class RemoveUser(StatesGroup):
    user_delet_id = State()

class InfoUser(StatesGroup):
    user_info_id = State()

@admin_router.message(StateFilter(None),Command('add_private_user'))
async def add_private_user(message: types.Message, state: FSMContext):
    await message.answer('Введите id пользователя, которому хотите дать привелегию авторизированного пользователя.')

    await state.set_state(AddUser.user_add_id)

@admin_router.message(AddUser.user_add_id)
async def user_private(message: types.Message, state: FSMContext):
    await message.answer('Вы добавили пользователя')
    await state.update_data(user_add_id=message.text)
    data = await state.get_data()
    
    user_private_list.append(data.get('user_add_id'))
    
    await state.clear()
    print(user_private_list)

@admin_router.message(StateFilter(None),Command('remove_private_user'))
async def remove_private_user(message: types.Message, state: FSMContext):
    await message.answer('Введите id пользователя, которого хотите удалить')

    await state.set_state(RemoveUser.user_delet_id)

@admin_router.message(RemoveUser.user_delet_id)
async def user_private(message: types.Message, state: FSMContext):
    await message.answer('Вы удалили пользователя!')
    await state.update_data(user_delet_id=message.text)
    data = await state.get_data()
    
    user_private_list.remove(data.get('user_delet_id'))
    await state.clear()
    print(user_private_list)

@admin_router.message(StateFilter(None),Command('info_user'))
async def info_user(message: types.Message, state: FSMContext):
    await message.answer('Введите id пользователя и я дам ссылку на него)')

    await state.set_state(InfoUser.user_info_id)

@admin_router.message(InfoUser.user_info_id)
async def user_private(message: types.Message, state: FSMContext):
    await state.update_data(user_info_id=message.text)   
    data = await state.get_data()
    d = data.get('user_info_id')
    await message.answer(f'tg://user?id={str(d)} вот ссылка на пользователя!')
    await state.clear()
    print(user_private_list)



 

