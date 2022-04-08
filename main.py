import telebot
import config
import random
import pg

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(sms):
	if sms.chat.type == "private":
		sti = open('image/sss.jpg','rb')
		bot.send_sticker(sms.chat.id,sti)
	
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Рандомное число")
		item2 = types.KeyboardButton("Как дела?")
		item3 = types.KeyboardButton("Узнать погоду")
		markup.add(item1,item2,item3)
		bot.send_message(sms.chat.id,"Привет хулиганы\nНу че народ погнали на хуй!!!\n ЕБАНЫЙ РООТ...",parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_sms(sms):
	#sms.text то что написали в чат
	#if sms.chat.type == "private":
	if True:
		if sms.text == "Рандомное число":
			bot.send_message(sms.chat.id,str(random.randint(0,100)))
		elif sms.text == "Как дела?":
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо",callback_data="good")
			item2 = types.InlineKeyboardButton("Плохо",callback_data="bad")
			markup.add(item1,item2)
			bot.send_message(sms.chat.id,"Ммм... у меня все четко, я в разработке! А ты как?",reply_markup=markup)
		elif sms.text == "Узнать погоду":
			data = pg.get_weather_forecast()
			markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton(f"{data[0].numbers_month} {data[0].name_month}",callback_data="0")
			item2 = types.InlineKeyboardButton(f"{data[1].numbers_month} {data[1].name_month}",callback_data="1")
			item3 = types.InlineKeyboardButton(f"{data[2].numbers_month} {data[2].name_month}",callback_data="2")
			item4 = types.InlineKeyboardButton(f"{data[3].numbers_month} {data[3].name_month}",callback_data="3")
			item5 = types.InlineKeyboardButton(f"{data[4].numbers_month} {data[4].name_month}",callback_data="4")
			item6 = types.InlineKeyboardButton(f"{data[5].numbers_month} {data[5].name_month}",callback_data="5")
			item7 = types.InlineKeyboardButton(f"{data[6].numbers_month} {data[6].name_month}",callback_data="6")
			markup.add(item1,item2,item3,item4,item5,item6,item7)
			bot.send_message(sms.chat.id,"На какой день вам сказать погоду?",reply_markup=markup)
		else:
			pass
			#bot.send_message(sms.chat.id,"<b>{}</b>:{}".format(sms.from_user.first_name,"Я пока что не понимаю этого"),parse_mode="html")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == "good":
				bot.send_message(call.message.chat.id,"Это просто прекрасно!")
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ОУ",reply_markup=None)
			elif call.data == "bad":
				bot.send_message(call.message.chat.id,"Просто работать надо и все у тебя получится")
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Мм..",reply_markup=None)
			elif call.data == "0":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[0].day_week} {data[0].numbers_month} {data[0].name_month}\nПогода:{data[0].cloud_cover}\n"
				str_2 = f"Днем: {data[0].day_temperature}\nНочью:{data[0].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "1":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[1].day_week} {data[1].numbers_month} {data[1].name_month}\nПогода:{data[1].cloud_cover}\n"
				str_2 = f"Днем: {data[1].day_temperature}\nНочью:{data[1].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "2":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[2].day_week} {data[2].numbers_month} {data[2].name_month}\nПогода:{data[2].cloud_cover}\n"
				str_2 = f"Днем: {data[2].day_temperature}\nНочью:{data[2].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "3":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[3].day_week} {data[3].numbers_month} {data[3].name_month}\nПогода:{data[3].cloud_cover}\n"
				str_2 = f"Днем: {data[3].day_temperature}\nНочью:{data[3].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "4":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[4].day_week} {data[4].numbers_month} {data[4].name_month}\nПогода:{data[4].cloud_cover}\n"
				str_2 = f"Днем: {data[4].day_temperature}\nНочью:{data[4].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "5":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[5].day_week} {data[5].numbers_month} {data[5].name_month}\nПогода:{data[0].cloud_cover}\n"
				str_2 = f"Днем: {data[5].day_temperature}\nНочью:{data[5].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			elif call.data == "6":
				data = pg.get_weather_forecast()
				str_1 = f"Дата: {data[6].day_week} {data[6].numbers_month} {data[6].name_month}\nПогода:{data[6].cloud_cover}\n"
				str_2 = f"Днем: {data[6].day_temperature}\nНочью:{data[6].night_temperature}"
				str = str_1+str_2
				bot.send_message(call.message.chat.id,str)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Прогноз",reply_markup=None)
			#bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Как дела?",reply_markup=None)
			#bot.answer_callback_query(chat_id=call.message.chat.id,show_alert=False,text="Это уведомление! =)")
	except Exception as e:
		print(repr(e))
bot.polling(none_stop=True)
