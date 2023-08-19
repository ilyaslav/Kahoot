# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kahoot.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import settings


class QuestionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(QuestionWidget, self).__init__(*args, **kwargs)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QtGui.QPixmap("img/4.png"))
        self.label.setScaledContents(True)
        self.label.setStyleSheet("QLabel{\n"
"    background-color: #ffffff;\n"
"    border-style: solid;\n"
"    border-color: #ffffff;\n"
"    border-width: 10px;\n"
"    border-radius: 90px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)   
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("QPushButton{\n"
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
"}"
"QFrame{background-color: rgba(255,255,255,0);}\n")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_back = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_back.sizePolicy().hasHeightForWidth())
        self.bt_back.setSizePolicy(sizePolicy)
        self.bt_back.setMinimumSize(QtCore.QSize(360, 180))
        self.bt_back.setMaximumSize(QtCore.QSize(360, 180))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bt_back.setFont(font)
        self.bt_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_back.setStyleSheet("")
        pixmap = QtGui.QPixmap("img/back.png")
        ButtonIcon = QtGui.QIcon(pixmap)
        self.bt_back.setIcon(ButtonIcon)
        self.bt_back.setIconSize(pixmap.rect().size()/4)
        self.bt_back.setObjectName("bt_back")
        self.horizontalLayout.addWidget(self.bt_back)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.central_widget = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.central_widget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bt_forward = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_forward.sizePolicy().hasHeightForWidth())
        self.bt_forward.setSizePolicy(sizePolicy)
        self.bt_forward.setMinimumSize(QtCore.QSize(360, 180))
        self.bt_forward.setMaximumSize(QtCore.QSize(360, 180))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bt_forward.setFont(font)
        self.bt_forward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pixmap = QtGui.QPixmap("img/forward.png")
        ButtonIcon = QtGui.QIcon(pixmap)
        self.bt_forward.setIcon(ButtonIcon)
        self.bt_forward.setIconSize(pixmap.rect().size()/4)
        self.bt_forward.setObjectName("bt_forward")
        self.horizontalLayout.addWidget(self.bt_forward)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.connect_funcions()
        self.add_start_bt()
        #self.add_logo()
        #self.add_timer()

    def connect_funcions(self):
        self.bt_back.pressed.connect(self.page_down)
        self.bt_forward.pressed.connect(self.page_up)

    def show_question(self, img):
        self.label.setPixmap(QtGui.QPixmap(img))
        self.label.setScaledContents(True)

    def show_answer(self, img):
        self.label.setPixmap(QtGui.QPixmap(img))
        self.label.setScaledContents(True)
        self.add_logo()

    def show_theme(self, img):
        self.label.setPixmap(QtGui.QPixmap(img))
        self.label.setScaledContents(True)
        self.add_logo()

    def page_up(self):
        if settings.stageType == 'new_stage':
            settings.stage+=1
            settings.question=1
            settings.questionNumber+=1
            settings.changeStageEvent = True
        elif settings.question == 10:
            settings.stage+=1
            settings.question=1
            settings.changeStageEvent = True
        else:
            settings.question+=1
            settings.questionNumber+=1
            settings.changeQuestionEvent = True

    def page_down(self):
        if settings.stageType == 'new_stage':
            settings.stage-=1
            settings.question=10
            settings.questionNumber-=1
            settings.changeStageEvent = True
        elif settings.question == 0:
            settings.stage-=1
            settings.question=10
            settings.questionNumber-=1
            settings.changeStageEvent = True
        else:
            settings.question-=1
            settings.questionNumber-=1
            settings.changeQuestionEvent = True

    def add_start_bt(self):
        self.horizontalLayout.removeWidget(self.central_widget)
        self.central_widget = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QtCore.QSize(180, 180))
        self.central_widget.setMaximumSize(QtCore.QSize(180, 180))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.central_widget.setFont(font)
        self.central_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.central_widget.setStyleSheet("QPushButton{\n"
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
        pixmap = QtGui.QPixmap("img/timer.png")
        ButtonIcon = QtGui.QIcon(pixmap)
        self.central_widget.setIcon(ButtonIcon)
        self.central_widget.setIconSize(pixmap.rect().size()/8)
        self.horizontalLayout.insertWidget(3,self.central_widget)
        self.central_widget.pressed.connect(self.start_timer_press)

    def add_timer(self):
        self.horizontalLayout.removeWidget(self.central_widget)
        self.central_widget = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QtCore.QSize(180, 180))
        self.central_widget.setMaximumSize(QtCore.QSize(180, 180))
        self.central_widget.setText("30")
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.central_widget.setFont(font)
        self.central_widget.setStyleSheet("QLabel\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 10px;\n"
"    border-color:  #92BCEA;\n"
"    background-color: #ffffff;\n"
"    border-radius: 90px;\n"
"    color: #000000;\n"
"}")
        self.central_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.insertWidget(3,self.central_widget)

    def add_logo(self):
        self.horizontalLayout.removeWidget(self.central_widget)
        self.central_widget = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QtCore.QSize(180, 180))
        self.central_widget.setMaximumSize(QtCore.QSize(180, 180))
        self.central_widget.setText("")
        self.central_widget.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.central_widget.setScaledContents(True)
        self.central_widget.setStyleSheet("QLabel\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 10px;\n"
"    border-color:  #92BCEA;\n"
"    background-color: #ffffff;\n"
"    border-radius: 90px;\n"
"    color: #000000;\n"
"}")
        self.horizontalLayout.insertWidget(3,self.central_widget)

    def start_timer_press(self):
        self.add_timer()
        settings.startTimerEvent = True

    def set_time(self):
        self.central_widget.setText(f'{settings.timer}')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = QuestionWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
