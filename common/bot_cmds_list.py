from aiogram.types import BotCommand


private = [
	BotCommand(command='about',description='Инфа обо мне'),
	BotCommand(command='admin',description='Войти как админ'),
	BotCommand(command='user_private',description='Войти как доверенный пользователь'),
	BotCommand(command='next',description='Продолжить без авторизации'),
	BotCommand(command='exit',description='Выйти из сессии')
]