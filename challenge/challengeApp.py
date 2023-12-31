# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import game
import settings

class ChallengeApp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1924, 1080)
        MainWindow.setStyleSheet("background-color: #FFFFEA;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 160))
        self.label.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #0F1108;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QPushButton{\n"
"    background-color: #92BCEA;\n"
"    color: #000000;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C0D5EC;\n"  
"}\n"
"QPushButton:pressed{\n"
"    background-color: #334195;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.teams = QtWidgets.QComboBox(self.frame)
        self.teams.setMinimumSize(QtCore.QSize(800, 160))
        self.teams.setMaximumSize(QtCore.QSize(800, 160))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.teams.setFont(font)
        self.teams.setStyleSheet("QComboBox\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 3px;\n"
"    border-color:  #0F1108;\n"
"    background-color: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #C0D5EC, stop: 1 #FFFFEA);\n"
"    border-radius: 8px;\n"
"    padding-left: 20px;\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(85, 170, 255);    \n"
"  background-color: #373e4e;\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}\n")
        self.teams.setMaxVisibleItems(6)
        self.teams.setObjectName("teams")
        self.gridLayout.addWidget(self.teams, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.minus1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus1.sizePolicy().hasHeightForWidth())
        self.minus1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minus1.setFont(font)
        self.minus1.setObjectName("minus1")
        self.verticalLayout_2.addWidget(self.minus1)
        self.minus2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus2.sizePolicy().hasHeightForWidth())
        self.minus2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minus2.setFont(font)
        self.minus2.setObjectName("minus2")
        self.verticalLayout_2.addWidget(self.minus2)
        self.minus3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus3.sizePolicy().hasHeightForWidth())
        self.minus3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minus3.setFont(font)
        self.minus3.setObjectName("minus3")
        self.verticalLayout_2.addWidget(self.minus3)
        self.minus4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus4.sizePolicy().hasHeightForWidth())
        self.minus4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minus4.setFont(font)
        self.minus4.setObjectName("minus4")
        self.verticalLayout_2.addWidget(self.minus4)
        self.minus5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus5.sizePolicy().hasHeightForWidth())
        self.minus5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minus5.setFont(font)
        self.minus5.setObjectName("minus5")
        self.verticalLayout_2.addWidget(self.minus5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plus1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus1.sizePolicy().hasHeightForWidth())
        self.plus1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.plus1.setFont(font)
        self.plus1.setObjectName("plus1")
        self.verticalLayout_4.addWidget(self.plus1)
        self.plus2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus2.sizePolicy().hasHeightForWidth())
        self.plus2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.plus2.setFont(font)
        self.plus2.setObjectName("plus2")
        self.verticalLayout_4.addWidget(self.plus2)
        self.plus3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus3.sizePolicy().hasHeightForWidth())
        self.plus3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.plus3.setFont(font)
        self.plus3.setObjectName("plus3")
        self.verticalLayout_4.addWidget(self.plus3)
        self.plus4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus4.sizePolicy().hasHeightForWidth())
        self.plus4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.plus4.setFont(font)
        self.plus4.setObjectName("plus4")
        self.verticalLayout_4.addWidget(self.plus4)
        self.plus5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus5.sizePolicy().hasHeightForWidth())
        self.plus5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.plus5.setFont(font)
        self.plus5.setObjectName("plus5")
        self.verticalLayout_4.addWidget(self.plus5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connect_funcions()
        self.fill_teams()

    def connect_funcions(self):
        self.plus1.pressed.connect(self.add_1)
        self.plus2.pressed.connect(self.add_2)
        self.plus3.pressed.connect(self.add_3)
        self.plus4.pressed.connect(self.add_4)
        self.plus5.pressed.connect(self.add_5)
        self.minus1.pressed.connect(self.remove_1)
        self.minus2.pressed.connect(self.remove_2)
        self.minus3.pressed.connect(self.remove_3)
        self.minus4.pressed.connect(self.remove_4)
        self.minus5.pressed.connect(self.remove_5)

    def add_1(self):
        team_name = self.teams.currentText()
        game.change_score(1, team_name)
        settings.fillEvent = True
    def add_2(self):
        team_name = self.teams.currentText()
        game.change_score(2, team_name)
        settings.fillEvent = True
    def add_3(self):
        team_name = self.teams.currentText()
        game.change_score(3, team_name)
        settings.fillEvent = True
    def add_4(self):
        team_name = self.teams.currentText()
        game.change_score(4, team_name)
        settings.fillEvent = True
    def add_5(self):
        team_name = self.teams.currentText()
        game.change_score(5, team_name)
        settings.fillEvent = True

    def remove_1(self):
        team_name = self.teams.currentText()
        game.change_score(-1, team_name)
        settings.fillEvent = True
    def remove_2(self):
        team_name = self.teams.currentText()
        game.change_score(-2, team_name)
        settings.fillEvent = True
    def remove_3(self):
        team_name = self.teams.currentText()
        game.change_score(-3, team_name)
        settings.fillEvent = True
    def remove_4(self):
        team_name = self.teams.currentText()
        game.change_score(-4, team_name)
        settings.fillEvent = True
    def remove_5(self):
        team_name = self.teams.currentText()
        game.change_score(-5, team_name)
        settings.fillEvent = True

    def fill_teams(self):
        for team in settings.rating:
            self.teams.addItem(team[1])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Интеллектуальная игра"))
        self.minus1.setText(_translate("MainWindow", "-1"))
        self.minus2.setText(_translate("MainWindow", "-2"))
        self.minus3.setText(_translate("MainWindow", "-3"))
        self.minus4.setText(_translate("MainWindow", "-4"))
        self.minus5.setText(_translate("MainWindow", "-5"))
        self.plus1.setText(_translate("MainWindow", "+1"))
        self.plus2.setText(_translate("MainWindow", "+2"))
        self.plus3.setText(_translate("MainWindow", "+3"))
        self.plus4.setText(_translate("MainWindow", "+4"))
        self.plus5.setText(_translate("MainWindow", "+5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ChallengeApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
