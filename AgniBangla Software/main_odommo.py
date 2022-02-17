#Team 3rr0r
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1199, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    border-radius: 5px;\n"
"    border :1px rgb(0,0,0);\n"
"    background-color: rgb(0, 170, 127,100);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,20);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,50);\n"
"    \n"
"\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1211, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/bg/gui.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 490, 211, 41))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    border :1px rgb(0,0,0);\n"
"    background-color: rgb(0, 170, 127,100);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,20);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,50);\n"
"    \n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 540, 211, 41))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    border :1px rgb(0,0,0);\n"
"    background-color: rgb(0, 170, 127,100);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,20);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:#fff;\n"
"     background-color: rgb(0, 170, 127,50);\n"
"    \n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.battery_frame = QtWidgets.QFrame(self.centralwidget)
        self.battery_frame.setGeometry(QtCore.QRect(970, 260, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_frame.sizePolicy().hasHeightForWidth())
        self.battery_frame.setSizePolicy(sizePolicy)
        self.battery_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.battery_frame.setMaximumSize(QtCore.QSize(100, 100))
        self.battery_frame.setStyleSheet("QFrame{\n"
"    border: 3px solid rgb(56, 185, 35);\n"
"    border-radius: 50px;\n"
"}\n"
"")
        self.battery_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.battery_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_frame.setObjectName("battery_frame")
        self.battery_percentage_output_label = QtWidgets.QLabel(self.battery_frame)
        self.battery_percentage_output_label.setGeometry(QtCore.QRect(0, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.battery_percentage_output_label.setFont(font)
        self.battery_percentage_output_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none; \n"
"background-color: none;")
        self.battery_percentage_output_label.setLineWidth(0)
        self.battery_percentage_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_percentage_output_label.setObjectName("battery_percentage_output_label")
        self.battery_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.battery_frame_2.setGeometry(QtCore.QRect(1090, 260, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_frame_2.sizePolicy().hasHeightForWidth())
        self.battery_frame_2.setSizePolicy(sizePolicy)
        self.battery_frame_2.setMinimumSize(QtCore.QSize(100, 100))
        self.battery_frame_2.setMaximumSize(QtCore.QSize(100, 100))
        self.battery_frame_2.setStyleSheet("QFrame{\n"
"    border: 3px solid rgb(56, 185, 35);\n"
"    border-radius: 50px;\n"
"}\n"
"")
        self.battery_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.battery_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_frame_2.setObjectName("battery_frame_2")
        self.battery_percentage_output_label_2 = QtWidgets.QLabel(self.battery_frame_2)
        self.battery_percentage_output_label_2.setGeometry(QtCore.QRect(30, 40, 48, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.battery_percentage_output_label_2.setFont(font)
        self.battery_percentage_output_label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none; \n"
"background-color: none;")
        self.battery_percentage_output_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_percentage_output_label_2.setObjectName("battery_percentage_output_label_2")
        self.camView = QtWidgets.QWidget(self.centralwidget)
        self.camView.setGeometry(QtCore.QRect(280, 10, 661, 551))
        self.camView.setStyleSheet("\n"
"QWidget{\n"
"border-radius: 10px;\n"
"background-color: rgb(85, 85, 127,100);\n"
"}")
        self.camView.setObjectName("camView")
        self.progressBar_1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_1.setGeometry(QtCore.QRect(970, 120, 211, 21))
        self.progressBar_1.setStyleSheet("QProgressBar{\n"
"    background-color : rgb(141, 144, 147);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.54, stop:0 rgba(255, 200, 68, 255), stop:1 rgba(180, 252, 124, 255));\n"
"}")
        self.progressBar_1.setProperty("value", 80)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_1.setInvertedAppearance(False)
        self.progressBar_1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(970, 590, 211, 41))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(970, 230, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.temperature_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label_2.setGeometry(QtCore.QRect(970, 90, 211, 27))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setUnderline(False)
        self.temperature_label_2.setFont(font)
        self.temperature_label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.temperature_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label_2.setObjectName("temperature_label_2")
        self.battery_frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.battery_frame_4.setGeometry(QtCore.QRect(970, 370, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_frame_4.sizePolicy().hasHeightForWidth())
        self.battery_frame_4.setSizePolicy(sizePolicy)
        self.battery_frame_4.setMinimumSize(QtCore.QSize(100, 100))
        self.battery_frame_4.setMaximumSize(QtCore.QSize(100, 100))
        self.battery_frame_4.setStyleSheet("QFrame{\n"
"    border: 3px solid rgb(56, 185, 35);\n"
"    border-radius: 50px;\n"
"}\n"
"")
        self.battery_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.battery_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_frame_4.setObjectName("battery_frame_4")
        self.battery_percentage_output_label_7 = QtWidgets.QLabel(self.battery_frame_4)
        self.battery_percentage_output_label_7.setGeometry(QtCore.QRect(0, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.battery_percentage_output_label_7.setFont(font)
        self.battery_percentage_output_label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none; \n"
"background-color: none;")
        self.battery_percentage_output_label_7.setLineWidth(0)
        self.battery_percentage_output_label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_percentage_output_label_7.setObjectName("battery_percentage_output_label_7")
        self.battery_frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.battery_frame_5.setGeometry(QtCore.QRect(1090, 370, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_frame_5.sizePolicy().hasHeightForWidth())
        self.battery_frame_5.setSizePolicy(sizePolicy)
        self.battery_frame_5.setMinimumSize(QtCore.QSize(100, 100))
        self.battery_frame_5.setMaximumSize(QtCore.QSize(100, 100))
        self.battery_frame_5.setStyleSheet("QFrame{\n"
"    border: 3px solid rgb(56, 185, 35);\n"
"    border-radius: 50px;\n"
"}\n"
"")
        self.battery_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.battery_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.battery_frame_5.setObjectName("battery_frame_5")
        self.battery_percentage_output_label_8 = QtWidgets.QLabel(self.battery_frame_5)
        self.battery_percentage_output_label_8.setGeometry(QtCore.QRect(0, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.battery_percentage_output_label_8.setFont(font)
        self.battery_percentage_output_label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none; \n"
"background-color: none;")
        self.battery_percentage_output_label_8.setLineWidth(0)
        self.battery_percentage_output_label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_percentage_output_label_8.setObjectName("battery_percentage_output_label_8")
        self.temp_frame = QtWidgets.QFrame(self.centralwidget)
        self.temp_frame.setGeometry(QtCore.QRect(10, 20, 241, 201))
        self.temp_frame.setStyleSheet("QFrame{\n"
"background-color: rgb(138, 138, 138,100);\n"
"border-radius:10px;\n"
"}")
        self.temp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp_frame.setObjectName("temp_frame")
        self.temp_frame_line = QtWidgets.QFrame(self.temp_frame)
        self.temp_frame_line.setGeometry(QtCore.QRect(19, 35, 211, 2))
        self.temp_frame_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temp_frame_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.temp_frame_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.temp_frame_line.setObjectName("temp_frame_line")
        self.temperature_label = QtWidgets.QLabel(self.temp_frame)
        self.temperature_label.setGeometry(QtCore.QRect(20, 5, 211, 27))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setUnderline(False)
        self.temperature_label.setFont(font)
        self.temperature_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label.setObjectName("temperature_label")
        self.array1_label_2 = QtWidgets.QLabel(self.temp_frame)
        self.array1_label_2.setGeometry(QtCore.QRect(20, 60, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.array1_label_2.setFont(font)
        self.array1_label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.array1_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.array1_label_2.setObjectName("array1_label_2")
        self.array1_label_3 = QtWidgets.QLabel(self.temp_frame)
        self.array1_label_3.setGeometry(QtCore.QRect(20, 100, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.array1_label_3.setFont(font)
        self.array1_label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.array1_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.array1_label_3.setObjectName("array1_label_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.temp_frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 160, 91, 31))
        self.pushButton_6.setStyleSheet("QPushButton{ \n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 0);\n"
"    border: 1px solid rgb(46, 52, 54);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"    border: 1px solid rgb(46, 52, 54);\n"
"} \n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.temp_frame)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 160, 101, 31))
        self.pushButton_7.setStyleSheet("QPushButton{ \n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    \n"
"    \n"
"    background-color: rgb(255, 57, 116);\n"
"    border: 1px solid rgb(46, 52, 54);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    background-color: rgb(255, 106, 128);\n"
"    border: 1px solid rgb(46, 52, 54);\n"
"} \n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.array1_label_4 = QtWidgets.QLabel(self.temp_frame)
        self.array1_label_4.setGeometry(QtCore.QRect(80, 60, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.array1_label_4.setFont(font)
        self.array1_label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.array1_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.array1_label_4.setObjectName("array1_label_4")
        self.array1_label_5 = QtWidgets.QLabel(self.temp_frame)
        self.array1_label_5.setGeometry(QtCore.QRect(90, 100, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        self.array1_label_5.setFont(font)
        self.array1_label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.array1_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.array1_label_5.setObjectName("array1_label_5")
        self.temperature_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label_3.setGeometry(QtCore.QRect(970, 210, 211, 27))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setUnderline(False)
        self.temperature_label_3.setFont(font)
        self.temperature_label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.temperature_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label_3.setObjectName("temperature_label_3")
        self.btn_minimize_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimize_5.setGeometry(QtCore.QRect(730, 570, 211, 51))
        self.btn_minimize_5.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_minimize_5.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgb(200, 5, 17);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(200, 5, 17);\n"
"}")
        self.btn_minimize_5.setObjectName("btn_minimize_5")
        self.btn_minimize_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimize_2.setGeometry(QtCore.QRect(280, 570, 201, 51))
        self.btn_minimize_2.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_minimize_2.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.btn_minimize_2.setObjectName("btn_minimize_2")
        self.btn_minimize_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimize_4.setGeometry(QtCore.QRect(490, 570, 231, 51))
        self.btn_minimize_4.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_minimize_4.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(60, 198, 123);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(60, 198, 123, 150);\n"
"}")
        self.btn_minimize_4.setObjectName("btn_minimize_4")
        self.camView_2 = QtWidgets.QWidget(self.centralwidget)
        self.camView_2.setGeometry(QtCore.QRect(10, 230, 241, 171))
        self.camView_2.setStyleSheet("\n"
"QWidget{\n"
"border-radius: 10px;\n"
"background-color: rgb(85, 85, 127,100);\n"
"}")
        self.camView_2.setObjectName("camView_2")
        self.temperature_label_4 = QtWidgets.QLabel(self.camView_2)
        self.temperature_label_4.setGeometry(QtCore.QRect(20, 0, 211, 27))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setUnderline(False)
        self.temperature_label_4.setFont(font)
        self.temperature_label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.temperature_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label_4.setObjectName("temperature_label_4")
        self.temp_frame_line_2 = QtWidgets.QFrame(self.camView_2)
        self.temp_frame_line_2.setGeometry(QtCore.QRect(20, 30, 211, 2))
        self.temp_frame_line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temp_frame_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.temp_frame_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.temp_frame_line_2.setObjectName("temp_frame_line_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_4 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 40, 51, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 40, 71, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_14 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 80, 81, 31))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 80, 51, 31))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_13.setGeometry(QtCore.QRect(160, 80, 71, 31))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_9 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 120, 81, 31))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_10.setGeometry(QtCore.QRect(100, 120, 51, 31))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.camView_2)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 120, 71, 31))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(198, 192, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(198, 192, 60, 150);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.map = QtWidgets.QWidget(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(10, 410, 231, 191))
        self.map.setObjectName("map")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agni Bangla Drone GUI"))
        self.pushButton_2.setText(_translate("MainWindow", "Weather Monitor"))
        self.pushButton_3.setText(_translate("MainWindow", "Data Analysis"))
        self.battery_percentage_output_label.setText(_translate("MainWindow", "85%"))
        self.battery_percentage_output_label_2.setText(_translate("MainWindow", "90%"))
        self.pushButton_8.setText(_translate("MainWindow", "Predict Weather"))
        self.temperature_label_2.setText(_translate("MainWindow", "DRONE CHARGE"))
        self.battery_percentage_output_label_7.setText(_translate("MainWindow", "90%"))
        self.battery_percentage_output_label_8.setText(_translate("MainWindow", "90%"))
        self.temperature_label.setText(_translate("MainWindow", "DRONE INFO"))
        self.array1_label_2.setText(_translate("MainWindow", "IP     :"))
        self.array1_label_3.setText(_translate("MainWindow", "PORT :"))
        self.pushButton_6.setText(_translate("MainWindow", "CONNECT"))
        self.pushButton_7.setText(_translate("MainWindow", "DISCONNECT"))
        self.array1_label_4.setText(_translate("MainWindow", "https://192.168.1.1"))
        self.array1_label_5.setText(_translate("MainWindow", "8080"))
        self.temperature_label_3.setText(_translate("MainWindow", "DRONE THRUST"))
        self.btn_minimize_5.setText(_translate("MainWindow", "Emergency Stop"))
        self.btn_minimize_2.setText(_translate("MainWindow", "Release Water"))
        self.btn_minimize_4.setText(_translate("MainWindow", "Release Fire Ball"))
        self.temperature_label_4.setText(_translate("MainWindow", "DRONE CONTROL PANEL"))
        self.pushButton_15.setText(_translate("MainWindow", "L.Forward"))
        self.pushButton_4.setText(_translate("MainWindow", "Front"))
        self.pushButton_5.setText(_translate("MainWindow", "R.Forward"))
        self.pushButton_14.setText(_translate("MainWindow", "Left"))
        self.pushButton_12.setText(_translate("MainWindow", "Stop"))
        self.pushButton_13.setText(_translate("MainWindow", "Right"))
        self.pushButton_9.setText(_translate("MainWindow", "L.Backward"))
        self.pushButton_10.setText(_translate("MainWindow", "Back"))
        self.pushButton_11.setText(_translate("MainWindow", "R.Backward"))

import rc_odommo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

