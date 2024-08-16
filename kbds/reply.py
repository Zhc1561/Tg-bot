from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_kb_start = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='/about'),
		KeyboardButton(text='/my_id'),
		KeyboardButton(text='/admin'),
		KeyboardButton(text='/user_private'),
		KeyboardButton(text='/next')
		],
	],
	resize_keyboard=True,
	input_field_placeholder='Что Вас инетересует?'


)

start_kb_admin = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='/add_private_user'),
		KeyboardButton(text='/remove_private_user'),
		KeyboardButton(text='/all_users'),
		KeyboardButton(text='/help_a'),
		KeyboardButton(text='/exit')
		],
	],
	resize_keyboard=True,
	input_field_placeholder='Что Вас инетересует?'


)

start_kb_private_user = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='/wiki'),
		KeyboardButton(text='/stack_over_flow'),
		KeyboardButton(text='/help_p'),
		KeyboardButton(text='/exit')
		],
	],
	resize_keyboard=True,
	input_field_placeholder='Что Вас инетересует?'


)

start_kb_user = ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='/schedule'),
		KeyboardButton(text='/help_u'),
		KeyboardButton(text='/exit')
		],
	],
	resize_keyboard=True,
	input_field_placeholder='Что Вас инетересует?'


)

del_kbd = ReplyKeyboardRemove()