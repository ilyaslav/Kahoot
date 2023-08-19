from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from challengeApp import ChallengeApp
from ratingApp import RatingApp
from threadClass import ThreadClass
import game
import settings

class MyApp(RatingApp):
	def setupUi(self, Form):
		super(MyApp, self).setupUi(Form)
		self.start_worker()

	def start_worker(self):
		self.thread = ThreadClass(parent=None)
		self.thread.start()
		self.thread.any_signal.connect(self.main_loop)

	def main_loop(self):
		self.start_event()
		self.fill_event()

	def start_event(self):
		if settings.startEvent:
			settings.startEvent = False
			data = game.fill_rating()
			if data:
				self.add_rating()
				self.fill_rating()
				self.open_challengeApp()

	def fill_event(self):
		if settings.fillEvent:
			settings.fillEvent = False
			self.fill_rating()

if __name__ == "__main__":
	import sys
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QWidget()
	ui = MyApp()
	ui.setupUi(MainWindow)
	MainWindow.setWindowState(Qt.WindowMaximized)
	try:
		MainWindow.windowHandle().setScreen(app.screens()[1])
	except:
		pass
	MainWindow.showFullScreen()
	sys.exit(app.exec_())