import telebot
import threading
import random

import settings
from database import Database
bot = telebot.TeleBot('5415524055:AAGHGAKYir7R-O1His9uLyTDksB_OXQ917k')
db = Database('Kahoot.db')

@bot.message_handler(commands=['start'])
def start(message):
	table_name = 'Teams'
	if add_team(message.from_user.id):
		bot.send_message(message.chat.id, f"Команда успешно зарегистрирована!\nВаша команда: {settings.teamName}!", parse_mode="html")
	else:
		bot.send_message(message.chat.id, f"Ваша команда: {db.get_team_name(table_name ,message.from_user.id)}!", parse_mode="html")

@bot.message_handler(content_types="text")
def message_answer(message):
	table_name = "Kahoot"
	if db.user_exists(table_name, message.from_user.id):
		pass

def init_game():
	db.clear_table('Teams')
	settings.registration = True
	bot.polling(non_stop="True")

def add_team(user_id):
	table_name = 'Teams'
	if not db.user_exists(table_name, user_id) and settings.registration:
		settings.teamName = random_team()
		settings.teamColor = f'#{user_id%1000000}'
		settings.teamScore = 0
		settings.teamNumber+=1
		db.add_team(table_name, user_id, settings.teamName, settings.teamColor, settings.teamScore)
		settings.addTeamEvent = True
		return True
	return False

def random_team():
	number = random.randint(0, len(settings.teamNames)-1)
	return settings.teamNames.pop(number)



threading.Thread(target= init_game, daemon = True).start()
