from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QTextCodec
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
		self.start_worker()

	def start_worker(self):
		self.thread = ThreadClass(parent=None)
		self.thread.start()
		self.thread.any_signal.connect(self.main_loop)

	def main_loop(self):
		self.change_stage()
		self.change_question()
		self.register_team()
		self.pop_team()
		self.print_team()

	def change_question(self):
		if settings.changeQuestionEvent:
			print(settings.question)
			settings.changeQuestionEvent = False

	def change_stage(self):
		if settings.changeStageEvent:
			self.gridLayout.removeWidget(self.eventWidget)
			settings.stageType = settings.stages[settings.stage]
			if settings.stageType == 'main':
				self.eventWidget = MainMenuWidget(self.centralwidget)
			elif settings.stageType == 'question':
				self.eventWidget = QuestionWidget(self.centralwidget)
				settings.question = 1
			elif settings.stageType == 'new_stage':
				self.eventWidget = QuestionWidget(self.centralwidget)
				self.eventWidget.add_logo()
			elif settings.stageType == 'rating':
				self.eventWidget = RatingWidget(self.centralwidget)
			elif settings.stageType == 'finish':
				self.eventWidget = FinishPageWidget(self.centralwidget)
			self.gridLayout.addWidget(self.eventWidget)
			settings.changeStageEvent = False

	def register_team(self):
		if settings.addTeamEvent:
			self.eventWidget.add_team(settings.teamName, settings.teamColor)
			settings.addTeamEvent = False

	def pop_team(self):
		if settings.popTeamEvent:
			self.pop_team_rating(settings.teams)
			settings.popTeamEvent = False

	def print_team(self):
		if settings.printRatingEvent:
			for team in settings.teams:
				self.print_team(team_list.index(team)+1, team[0], team[1], team[2])
			settings.printRatingEvent = False

	def pop_team_rating(self, team_list):
		if settings.teamNumber:
			team = team_list[settings.teamNumber-1]
			print_team(settings.teamNumber, team[0], team[1], team[2])
			settings.teamNumber-=1

	def print_team_rating(self, position, team_name, team_color, team_score):
		if settings.printTeamEvent:		
			self.eventWidget.add_team(position, team_name, team_color, team_score)

if __name__ == "__main__":
	import sys
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	MainWindow = QtWidgets.QMainWindow()
	ui = MyApp()
	ui.setupUi(MainWindow)
	MainWindow.setWindowState(Qt.WindowMaximized);
	MainWindow.showFullScreen()
	sys.exit(app.exec_())