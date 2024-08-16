from aiogram.types import BotCommand


private = [
	BotCommand(command='about',description='Инфа обо мне'),
	BotCommand(command='admin',description='Войти как админ'),
	BotCommand(command='my_id',description='Узнай своё id и отправь админу, если хочешь повысить привелегию'),
	BotCommand(command='user_private',description='Войти как авторизированный пользователь'),
	BotCommand(command='next',description='Продолжить без авторизации')
]