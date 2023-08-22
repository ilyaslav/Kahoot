import telebot
from telebot import types
import threading
import random

import settings
import jsonWriter
from database import Database
bot = telebot.TeleBot('5415524055:AAGHGAKYir7R-O1His9uLyTDksB_OXQ917k')
db = Database('Kahoot.db')

def send_message(chat_id, text, parse_mode = None, reply_markup = None):
	try:
		bot.send_message(chat_id, text, parse_mode = parse_mode, reply_markup = reply_markup)
	except:
		pass

@bot.message_handler(commands=['start'])
def start(message):
	table_name = 'Teams'
	if add_team(message.from_user.id):
		send_message(message.chat.id, f"Команда успешно зарегистрирована!\nВаша команда: {settings.teamName}!", parse_mode="html")
	else:
		send_message(message.chat.id, f"Ваша команда: {db.get_team_name(table_name ,message.from_user.id)}!", parse_mode="html")

@bot.message_handler(content_types="text")
def message_answer(message):
	table_name = "Teams"
	if db.user_exists(table_name, message.from_user.id):
		if settings.questionTime:
			if db.get_answer(table_name, message.from_user.id):
				check_answer(message)
				db.set_answer(table_name, message.from_user.id, False)
				send_message(message.chat.id, f"Ответ принят!", parse_mode="html")
			else:
				send_message(message.chat.id, f"Вы уже отправили ответ на этот вопрос!", parse_mode="html")

def init_game():
	db.clear_table('Teams')
	jsonWriter.write()
	settings.questions = jsonWriter.read()
	settings.registration = True
	bot.polling(non_stop="True")

def set_color(user_id):
	color = f'{user_id%1000000}'.rjust(6, '0')
	return '#'+color

def add_team(user_id):
	table_name = 'Teams'
	if not db.user_exists(table_name, user_id) and settings.registration:
		settings.teamName = random_team()
		settings.teamColor = set_color(user_id)
		settings.teamScore = 0
		settings.teamNumber+=1
		db.add_team(table_name, user_id, settings.teamName, settings.teamColor, settings.teamScore, settings.questionTime)
		settings.addTeamEvent = True
		return True
	return False

def random_team():
	number = random.randint(0, len(settings.teamNames)-1)
	return settings.teamNames.pop(number)

def send_question():
	table_name = 'Teams'
	user_ids = db.get_ids(table_name)
	for user_id in user_ids:
		for ID in user_id:
			message = settings.questions['questions'][settings.questionNumber-1]['question']
			if settings.questions['questions'][settings.questionNumber-1]['type'] == 'close':
				marcup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2, one_time_keyboard = True)
				item_a = types.KeyboardButton('А')
				item_b = types.KeyboardButton('Б')
				item_c = types.KeyboardButton('В')
				item_d = types.KeyboardButton('Г')
				marcup_reply.add(item_a, item_b, item_c, item_d)
				send_message(ID, message, reply_markup = marcup_reply)
			else:
				send_message(ID, message)

def set_all_answers(answer):
	table_name = 'Teams'
	db.set_all_answers(table_name, answer)

def check_answer(message):
	table_name = 'Teams'
	if find_answer(message.text):
		score = db.get_score(table_name, message.from_user.id)+1
		db.set_score(table_name, message.from_user.id, score)

def find_answer(answer):
	return answer.lower() in settings.questions['questions'][settings.questionNumber-1]['answer']

def get_rating():
	table_name = 'Teams'
	settings.teams = db.get_rating(table_name)

def save_team_list():
	get_rating()
	jsonWriter.save_team_list(settings.teams)

def load_team_list():
	return jsonWriter.load_team_list()

def calculate_rating(data):
	table_name = 'Teams'
	for team in data:
		score = db.get_score(table_name, team[0])
		score+= team[3]
		db.set_score(table_name, team[0], score)
	get_rating()


threading.Thread(target= init_game, daemon = True).start()
