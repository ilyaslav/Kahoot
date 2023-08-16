from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from questionWidget import QuestionWidget
from ratingWidget import RatingWidget
from mainMenuWidget import MainMenuWidget
from finishPageWidget import FinishPageWidget
from threadClass import ThreadClass
import game
import settings

class MyApp(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1920, 1280)
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		MainWindow.setFont(font)
		MainWindow.setStyleSheet("background-color: #61b0ff;")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.eventWidget = MainMenuWidget(self.centralwidget)
		self.eventWidget.setObjectName("eventWidget")
		self.gridLayout.addWidget(self.eventWidget, 1,0,1,1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.timer = QTimer()
		self.start_worker()

	def start_worker(self):
		self.thread = ThreadClass(parent=None)
		self.thread.start()
		self.thread.any_signal.connect(self.main_loop)

	def main_loop(self):
		self.change_stage()
		self.change_question()
		self.start_timer()
		self.register_team()
		self.pop_team()
		self.print_team()
		self.finish_event()

	def change_question(self):
		if settings.changeQuestionEvent:
			self.stop_timer()
			self.gridLayout.removeWidget(self.eventWidget)
			self.eventWidget = QuestionWidget(self.centralwidget)
			self.gridLayout.addWidget(self.eventWidget)
			self.show_question()
			settings.changeQuestionEvent = False

	def show_question(self):
		img = f'img/question{settings.questionNumber}.png'
		self.eventWidget.show_question('img/33.png')

	def show_answer(self):
		img = f'img/answer{settings.questionNumber}.png'
		self.eventWidget.show_answer('img/111.png')

	def change_stage(self):
		if settings.changeStageEvent:
			self.stop_timer()
			self.gridLayout.removeWidget(self.eventWidget)
			settings.stageType = settings.stages[settings.stage]
			if settings.stageType == 'main':
				self.eventWidget = MainMenuWidget(self.centralwidget)
			elif settings.stageType == 'question':
				self.eventWidget = QuestionWidget(self.centralwidget)
				self.show_question()
			elif settings.stageType == 'new_stage':
				game.save_team_list()
				self.eventWidget = QuestionWidget(self.centralwidget)
				self.eventWidget.add_logo()
			elif settings.stageType == 'rating':
				self.eventWidget = RatingWidget(self.centralwidget)
				game.get_rating()
				settings.printRatingEvent = True
			elif settings.stageType == 'finish':
				game.get_rating()
				self.eventWidget = FinishPageWidget(self.centralwidget)
			self.gridLayout.addWidget(self.eventWidget)
			settings.changeStageEvent = False

	def register_team(self):
		if settings.addTeamEvent:
			try:
				self.eventWidget.add_team(settings.teamName, settings.teamColor)
				settings.addTeamEvent = False
			except:
				pass

	def pop_team(self):
		if settings.popTeamEvent:
			self.pop_team_rating(settings.teams)
			settings.popTeamEvent = False

	def print_team(self):
		if settings.printRatingEvent:
			for team in settings.teams:
				self.print_team_rating(len(settings.teams)-settings.teams.index(team), team[1], team[2], team[3])
			settings.printRatingEvent = False

	def pop_team_rating(self, team_list):
		if settings.teamNumber:
			team = team_list[settings.teamNumber-1]
			self.print_team_rating(settings.teamNumber, team[1], team[2], team[3])
			settings.teamNumber-=1

	def print_team_rating(self, position, team_name, team_color, team_score):	
		self.eventWidget.add_team(position, team_name, team_color, team_score)

	def finish_event(self):
		if settings.finishEvent:
			settings.finishEvent = False
			data = game.load_team_list()
			if data:
				print(data)
				game.calculate_rating(data)
				self.eventWidget.change_central_widget()

	def start_timer(self):
		if settings.startTimerEvent:
			self.start_timer_event()
			settings.startTimerEvent = False

	def timer_event(self):
		if settings.timer:
			settings.timer-=1
			self.eventWidget.set_time()
		else:
			self.stop_timer()
			self.show_answer()
			game.set_all_answers(False)
	def start_timer_event(self):
		self.timer = QTimer()
		settings.timer = 30
		settings.questionTime = True
		game.set_all_answers(True)
		game.send_question()
		self.timer.timeout.connect(self.timer_event)
		self.timer.start(1000)
	def stop_timer(self):
		settings.questionTime = False
		self.timer.stop()

if __name__ == "__main__":
	import sys
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	MainWindow = QtWidgets.QMainWindow()
	ui = MyApp()
	ui.setupUi(MainWindow)
	MainWindow.setWindowState(Qt.WindowMaximized)
	try:
		MainWindow.windowHandle().setScreen(app.screens()[1])
	except:
		pass
	MainWindow.showFullScreen()
	sys.exit(app.exec_())