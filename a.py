from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
import datetime

from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.get("https://www.asu.ru/timetable/students/14/2129441043/?date=20240905&mode=print")



x = 0
i = ''
i1 = ''
th = ['№','Время','Предмет','Преподаватель','Аудитория','Дата изменения']
td = []
result =driver.find_elements(By.CLASS_NAME, "schedule_table-body-row")

for item in result:
    i = item.text
    if x == 1:
    	i1 = i
        await message.answer('№ Время Предмет Преподаватель Аудитория Дата изменения\n'+str(i))
    x = 1





