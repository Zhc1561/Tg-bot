from aiogram.filters import CommandStart, Command
from aiogram import types, Router
from kbds import reply
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import datetime
user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет я Бот! Авторизируйтесь как админ или как авторизированный пользователь,воспользовавшись моим меню. Вы можете продолжить сессию без авторизации, командой /next. Если возникли вопросы, то вот мой админ @TrueVISIon22', reply_markup = reply.start_kb_start)


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('''Обо мне:
        Я бот, которым могут пользоваться три группы пользователей. У каждой группы, есть свои команды, которые я выполняю. Если вы хотите повысить привелегию, воспользуйтесь командой /my_id и отправьте своё id моему админу @dreamyy66. Для того, чтобы узнать что делает та или иная команда в разных режимах пользователя, я добавил кнопки help_...

        ''')

@user_private_router.message(Command('my_id'))
async def my_id(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id} ")




@user_private_router.message(Command('next'))
async def user_next(message: types.Message):
    await message.answer('Вы вошли как неавторизированый пользователь!',reply_markup = reply.start_kb_user)   

@user_private_router.message(Command('help_u'))
async def user_u(message: types.Message):
    await message.answer('''Вам доступны 2 команды:
        1. /schedule - посмотреть расписание группы на текущий день.
        2. /exit - выйти.
        ''')

@user_private_router.message(Command('exit'))
async def exit(message: types.Message):
    await message.answer('Вы вышли из сессии(((.', reply_markup = reply.start_kb_start)


@user_private_router.message(Command('schedule'))
async def shedule(message: types.Message):
    
    date = datetime.datetime.now()

    date = str(date)
    date = date.replace('-','')
    date = date[0:8]
    
    
    url = "https://www.asu.ru/timetable/students/14/2129441043/?date="+date+"&mode=print"
    print(url)
    service = Service(executable_path='C:/Users/user/Desktop/drive/msedgedriver.exe')
    driver = webdriver.Edge(service=service)

    driver.get(url)


    x = 0
    i = ''
    i1 = ''
    th = ['№','Время','Предмет','Преподаватель','Аудитория','Дата изменения']
    td = []
    result =driver.find_elements(By.CLASS_NAME, "schedule_table-body-row")

    for item in result:
        i = item.text
        if x == 1:
            i1 = i.replace('\n',' ')
            i1 = i1.replace(' ','  ')
            await message.answer('Формат вывода: |№| |Время| |Предмет| |Преподаватель| |Аудитория| |Дата изменения|\n'+str(i1))
        x = 1