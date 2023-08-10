# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kahoot_finish.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import settings


class FinishPageWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(FinishPageWidget, self).__init__(*args, **kwargs)
        self.main_frame = QtWidgets.QFrame(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName("mainLayout")
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 160))
        self.label.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setMinimumSize(QtCore.QSize(700, 180))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-width: 10px;\n"
"    border-color:  #0000bb;\n"
"    background-color: #fea125;\n"
"    border-radius: 90px;\n"
"    color: #000000;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-color: #0000ff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addWidget(self.main_frame)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connect_funcions()
        self.teams = 25

    def connect_funcions(self):
        self.pushButton.pressed.connect(self.change_central_widget)

    def change_central_widget(self):
        self.mainLayout.removeWidget(self.main_frame)
        self.main_frame = QtWidgets.QFrame()
        self.add_rating()
        self.mainLayout.addWidget(self.main_frame)

    def add_rating(self):
        self.HL = QtWidgets.QHBoxLayout(self.main_frame)
        self.battery_frame = QtWidgets.QFrame(self)
        self.battery_frame.setMinimumSize(QtCore.QSize(800, 800))
        self.battery_frame.setMaximumSize(QtCore.QSize(1000, 8000))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.battery_frame.setFont(font)
        self.battery_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.battery_frame.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-color: #ffffff;\n"
"    border-width: 10px;\n"
"}\n"
"QLabel{\n"
"    background-color: red;\n"
"    border-style: solid;\n"
"    border-color: #ffffff;\n"
"    border-width: 0px;\n"
"    border-bottom-width: 4px;\n"
"}")
        self.battery_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.battery_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_frame.setObjectName("battery_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.battery_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QPushButton()#QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spacerItem.sizePolicy().hasHeightForWidth())
        spacerItem.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    background-color: #61b0ff;\n"
"    color: #000000;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-color: #0000ff;\n"
"}")
        spacerItem.pressed.connect(self.add_team_event)
        spacerItem.setSizePolicy(sizePolicy)
        self.verticalLayout_4.addWidget(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HL.addItem(spacerItem1)
        self.HL.addWidget(self.battery_frame)
        self.HL.addItem(spacerItem1)

    def add_team_event(self):
        settings.popTeamEvent = True

    def add_team(self, position, team_name, team_color, score):
        label = QtWidgets.QLabel(self.battery_frame)
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
        label.setText(f"{position}. {team_name}\t {team_score}")
        label.setStyleSheet("QLabel{\n"
f"    background-color: {team_color};\n"
"    border-style: solid;\n"
"    border-color: #ffffff;\n"
"    border-width: 0px;\n"
"    border-bottom-width: 4px;\n"
"    color: white;\n"
"}")
        self.verticalLayout_4.insertWidget(0, label)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Итоговый рейтинг команд"))
        self.pushButton.setText(_translate("Form", "Показать рейтинг команд"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
