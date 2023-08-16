import sqlite3
import threading

def lock(func):
	def wrappper(*args, **kwargs):
		lock = threading.Lock()
		i = 0
		while True:
			i+=1
			try:
				print(i)
				lock.acquire(True)
				data = func(*args, **kwargs)
				lock.release()
				return data
			except:
				print(*args)

	return wrappper

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.connection.cursor()

	@lock
	def user_exists(self, table_name, user_id):
		with self.connection:
			result = self.cursor.execute(f"SELECT * FROM {table_name} WHERE user_id = {user_id}").fetchmany(1)
			return bool(len(result))

	@lock
	def add_team(self, table_name, user_id, team_name, team_color, score, answer):
		with self.connection:
			return self.cursor.execute(f"INSERT INTO {table_name} ('user_id', 'team_name', 'team_color', 'score', 'answer') VALUES (?, ?, ?, ?, ?)",\
				(user_id, team_name, team_color, score, answer))

	@lock
	def clear_table(self, table_name):
		with self.connection:
			self.cursor.execute(f"DELETE FROM {table_name}")

	@lock
	def get_team_name(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT team_name FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	@lock
	def get_team_color(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT team_color FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	@lock
	def get_score(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT score FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]
	@lock
	def get_answer(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT answer FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	@lock
	def set_team_name(self, table_name, user_id, team_name):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET team_name = (?) WHERE user_id = {user_id}", (team_name,))

	@lock
	def set_team_color(self, table_name, user_id, team_color):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET team_color = (?) WHERE user_id = {user_id}", (team_color,))

	@lock
	def set_score(self, table_name, user_id, score):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET score = (?) WHERE user_id = {user_id}", (score,))

	@lock
	def set_answer(self, table_name, user_id, answer):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET answer = (?) WHERE user_id = {user_id}", (answer,))


	@lock
	def set_all_answers(self, table_name, answer):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET answer = (?)", (answer,))

	@lock
	def delete_user(self, table_name, user_id):
		with self.connection:
			self.connection.execute(f"DELETE FROM {table_name} WHERE user_id = {user_id}")

	@lock
	def get_rating(self, table_name):
		with self.connection:
			return self.cursor.execute(f"SELECT user_id, team_name, team_color, score FROM {table_name} ORDER BY score").fetchall()

	@lock
	def get_ids(self, table_name):
		with self.connection:
			return self.cursor.execute(f"SELECT user_id FROM {table_name}").fetchall()


#	def add_statistics(self, table_name, user_id, nickname, attempts):
#		with self.connection:
#			return self.cursor.execute(f"INSERT INTO {table_name} ('user_id', 'nickname', 'attempts') VALUES (?, ?, ?)", (user_id, nickname, attempts))
#
#	def get_statistics(self, table_name, user_id):
#		with self.connection:
#			return self.cursor.execute(f"SELECT * FROM {table_name}").fetchall()
#
#	def get_user_statistics(self, table_name, user_id):
#		with self.connection:
#			return self.cursor.execute(f"SELECT attempts FROM {table_name} WHERE user_id = {user_id}").fetchmany(1)[0][0]
#
#	def user_exists_statistics(self, table_name, user_id):
#		with self.connection:
#			result = self.cursor.execute(f"SELECT * FROM {table_name} WHERE user_id = {user_id}").fetchmany(1)
#			return bool(len(result))
#
#	def set_statistics(self, table_name, user_id, attempts):
#		with self.connection:
#			return self.cursor.execute(f"UPDATE {table_name} SET attempts = (?) WHERE user_id = {user_id}", (attempts,))
#
#
#	def lox_rassilka(self, table_name):
#		with self.connection:
#			return self.cursor.execute(f"SELECT user_id, attempts FROM {table_name}").fetchall()