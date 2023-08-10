import sqlite3

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.connection.cursor()

	def user_exists(self, table_name, user_id):
		with self.connection:
			result = self.cursor.execute(f"SELECT * FROM {table_name} WHERE user_id = {user_id}").fetchmany(1)
			return bool(len(result))

	def add_team(self, table_name, user_id, team_name, team_color, score):
		with self.connection:
			return self.cursor.execute(f"INSERT INTO {table_name} ('user_id', 'team_name', 'team_color', 'score') VALUES (?, ?, ?, ?)",\
				(user_id, team_name, team_color, score,))

	def clear_table(self, table_name):
		with self.connection:
			self.cursor.execute(f"DELETE FROM {table_name}")
			print('delete')


	def get_team_name(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT team_name FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	def get_team_color(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT team_color FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	def get_score(self, table_name, user_id):
		with self.connection:
			return self.cursor.execute(f"SELECT score FROM {table_name} WHERE user_id = ?", (user_id,)).fetchmany(1)[0][0]

	def set_team_name(self, table_name, user_id, team_name):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET team_name = (?) WHERE user_id = {user_id}", (team_name,))

	def set_team_color(self, table_name, user_id, team_color):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET team_color = (?) WHERE user_id = {user_id}", (team_color,))

	def set_score(self, table_name, user_id, score):
		with self.connection:
			return self.cursor.execute(f"UPDATE {table_name} SET score = (?) WHERE user_id = {user_id}", (score,))

	def delete_user(self, table_name, user_id):
		with self.connection:
			self.connection.execute(f"DELETE FROM {table_name} WHERE user_id = {user_id}")

	def get_rating(self, table_name, count):
		with self.connection:
			return self.cursor.execute(f"SELECT team_name, team_color, score FROM {table_name} ORDER BY score").fetchmany(count)


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