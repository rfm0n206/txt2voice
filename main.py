import glob
import gtts
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 380, 90, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 421, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Select file"))
        self.label_2.setText(_translate(
            "MainWindow", "txt2voice 2.0a \n\nby Tim Gore (KE6QBV / WRUK522)\n2023 CC BY-NC"))

    # This is where button action happens TG
    def pushButton_handler(self):
        print('button pressed')
        self.open_dialog_box()

    # This is where file dialog opens TG
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        print(filename)
        self.gen_from_file()

    def gen_from_file(self):
        print('generation happens here')

    # This takes selected txt file as source TG
    # def gen_from_file(self):
    #     list = []
    #     cwd = os.getcwd()
    #     list = open(filename).read().splitlines()
    #     for line in list:
    #         line = line.rstrip()
    #     for x in range(len(list)):
    #         tts = gtts.gTTS(list[x], lang="en")
    #         filename = list[x] + ".mp3"
    #         filename = filename.replace(" ", "_")
    #         filename = filename.lower()
    #         tts.save(filename)
    #         print("\nCreating file: " + filename)
    #         lst = glob.glob("*.mp3")
    #         print(lst)
    #         for file in lst:
    #             # convert wav to mp3
    #             os.system(
    #                 f"""ffmpeg -i {file} -acodec pcm_s16le -ar 8000 {file[:-4]}.wav""")
    #         # delete mp3 files after wav created
    #         currentdir = os.getcwd() + '/*.mp3'
    #         allmp3 = "rm *.mp3"
    #         os.system(allmp3)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
