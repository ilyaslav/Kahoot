# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kahoot_finish.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from challengeApp import ChallengeApp

import settings


class RatingApp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet("background-color: #FFFFEA;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 160))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #0F1108;")
        self.label.setPixmap(QtGui.QPixmap("img/name.png"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.action_widget = QtWidgets.QPushButton(Form)
        self.action_widget.setMinimumSize(QtCore.QSize(700, 180))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.action_widget.setFont(font)
        self.action_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.action_widget.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-color:  #0000bb;\n"
"    background-color: #92BCEA;\n"
"    border-radius: 90px;\n"
"    color: #000000;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C0D5EC;\n"  
"}\n"
"QPushButton:pressed{\n"
"    background-color: #334195;\n"
"}")
        self.action_widget.setObjectName("action_widget")
        self.horizontalLayout.addWidget(self.action_widget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.connect_funcions()

    def connect_funcions(self):
        self.action_widget.pressed.connect(self.bt_pressed)

    def bt_pressed(self):
        settings.startEvent = True

    def open_challengeApp(self):
        import sys
        self.MainWindow = QtWidgets.QWidget()
        self.ui = ChallengeApp()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.setWindowState(Qt.WindowMaximized)
        self.MainWindow.showFullScreen()

    def add_rating(self):
        self.label.setPixmap(QtGui.QPixmap())
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(0, 0))
        self.horizontalLayout.removeWidget(self.action_widget)
        self.action_widget = QtWidgets.QFrame()
        self.action_widget.setMinimumSize(QtCore.QSize(800, 800))
        self.action_widget.setMaximumSize(QtCore.QSize(1000, 8000))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.action_widget.setFont(font)
        self.action_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.action_widget.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-color: #0F1108;\n"
"    border-width: 10px;\n"
"}\n"
"QLabel{\n"
"    background-color: red;\n"
"    border-style: solid;\n"
"    border-color: #92BCEA;\n"
"    border-width: 0px;\n"
"    border-bottom-width: 4px;\n"
"}")
        self.action_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.action_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.action_widget.setObjectName("action_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.action_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.insertWidget(1, self.action_widget)
        self.fill_rating()

    def fill_rating(self):
        self.clear_rating()
        settings.rating.sort(key = lambda x: x[3])
        for team in reversed(settings.rating):
            index = len(settings.rating) - settings.rating.index(team)
            self.add_team(index, team[1], team[2], team[3])
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

    def clear_rating(self):
        tmpItem = self.verticalLayout_4.itemAt(0)
        while(tmpItem):
            self.verticalLayout_4.removeItem(tmpItem)
            self.verticalLayout_4.removeWidget(tmpItem.widget())
            del tmpItem
            tmpItem = self.verticalLayout_4.itemAt(0)
        self.verticalLayout_4.update()

    def add_team(self, position, team_name, team_color, score):
        label = QtWidgets.QLabel(self.action_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        label.setFont(font)
        label.setMinimumSize(QtCore.QSize(0, 20))
        label.setMaximumSize(QtCore.QSize(16777215, 40))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(f"{position}. {team_name}\t {score}")
        label.setStyleSheet("QLabel{\n"
f"    background-color: {team_color};\n"
"    border-style: solid;\n"
"    border-color: #FFFFEA;\n"
"    border-width: 0px;\n"
"    border-bottom-width: 4px;\n"
"    color: white;\n"
"}")
        self.verticalLayout_4.addWidget(label)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.action_widget.setText(_translate("Form", "Начать игру"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RatingApp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
