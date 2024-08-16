from aiogram import F, Router, types
from aiogram.filters import Command,StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bs4 import BeautifulSoup
import requests
import json


from filters.chat_types import IsPrivate
from kbds import reply

privat_router = Router()
privat_router.message.filter(IsPrivate())


@privat_router.message(Command('user_private'))
async def user_private(message: types.Message):
    await message.answer('Вы вошли как довереный пользователь!',reply_markup = reply.start_kb_private_user)


class Wiki(StatesGroup):
    zapros = State()

@privat_router.message(Command('help_p'))
async def user_p(message: types.Message):
    await message.answer('''Вам доступны 3 команды:
        1. /wiki - запросить ссылку на какую-либо статью с Wikipedia.
        2. /stack_over_flow - запросить 3 ссылки на тему по javascript с сайта stackoverflow.
        3. /exit - выйти.
        ''')

@privat_router.message(StateFilter(None),Command('wiki'))
async def wiki(message: types.Message, state: FSMContext):
    await message.answer('Введите запрос и я дам ссылку на статью в Wikipedia.')

    await state.set_state(Wiki.zapros)

@privat_router.message(Wiki.zapros)
async def wiki2(message: types.Message, state: FSMContext,session = AsyncSession):
    await state.update_data(zapros=message.text)
    data = await state.get_data()

    x = data['zapros']
    x = x.replace(' ','+')
    url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + x
    request = requests.get(url)
    soup = BeautifulSoup(request.text,"html.parser")

    links = soup.find_all("div", class_="nw-search-result-heading")

    if len(links) > 0 :
        url = "https://ru.wikipedia.org" + links[0].find("a")["href"]

    await message.answer(f'Ссылка на статью: {url}')



    await state.clear()



class Flow(StatesGroup):
    flow = State()


@privat_router.message(StateFilter(None),Command('stack_over_flow'))
async def flow(message: types.Message, state: FSMContext):
    await message.answer('Введите запрос и я дам ссылки на пару статей с Stakoverflow.')

    await state.set_state(Flow.flow)

@privat_router.message(Flow.flow)
async def flow2(message: types.Message, state: FSMContext,session = AsyncSession):
    await state.update_data(flow=message.text)
    data = await state.get_data()

    x = str(data['flow'])
    x = x.replace(' ','%20')
    url = "https://api.stackexchange.com/2.3/search/advanced?order=desc&tagged=javascript&sort=relevance&q=%20"+x+"&site=stackoverflow"
    
    response = requests.get(url)

    data = json.loads(response.text)

    questions = data["items"]
    i = -1
    if len(questions) < 1:
        await message.answer('Введите корректную тему по javascript')    
    for question in questions:
        i += 1
        
        if i == 0:
            title1 = question["title"]
            link1 = question["link"]
            print(title1,link1)
            
        if i == 1:
            title2 = question["title"]
            link2 = question["link"]
            print(title2,link2)
            
        if i == 2:
            title3 = question["title"]
            link3 = question["link"]
            print(title3,link3)
            
    
    await message.answer('Вот пару статей по вашей теме и ссылки на них:\n'+'1.'+str(title1)+'\n'+ str(link1)+'\n'+'2.'+str(title2)+'\n' + str(link2)+'\n'+'3.'+str(title3)+'\n' + str(link3))       
    
 
        
    



    await state.clear()





    