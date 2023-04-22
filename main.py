import glob
import gtts
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(10, 380, 90, 28))
        self.open_button.setObjectName("pushButton")
        self.open_button.clicked.connect(self.open_button_handler)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(130, 10, 181, 161))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 180, 421, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setScaledContents(True)
        self.text.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.text.setObjectName("text")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(340, 380, 90, 28))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.exit_button_handler)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "txt2voice 2.0a", "txt2voice 2.0a"))
        self.open_button.setText(_translate("MainWindow", "Select file"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.text.setText(_translate(
            "MainWindow", "txt2voice 2.0a \n\nTim Gore (KE6QBV / WRUK522)\n2023 CC BY-NC"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    # This is where button action happens
    def open_button_handler(self):
        print('button pressed')
        self.open_dialog_box()

    # This button simply quits the program
    def exit_button_handler(self):
        MainWindow.close()

    # File dialog opens, lets you choose file and then process it
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        list = []
        cwd = os.getcwd()
        list = open(path).read().splitlines()
        for line in list:
            line = line.rstrip()
        for x in range(len(list)):
            tts = gtts.gTTS(list[x], lang="en")
            filename = list[x] + ".mp3"
            filename = filename.replace(" ", "_")
            filename = filename.lower()
            tts.save(filename)
            print("\nCreating file: " + filename)
            lst = glob.glob("*.mp3")
            print(lst)
            for file in lst:
                # convert wav to mp3
                os.system(
                    f"""ffmpeg -i {file} -acodec pcm_s16le -ar 8000 {file[:-4]}.wav""")
            # delete mp3 files after wav created
            currentdir = os.getcwd() + '/*.mp3'
            allmp3 = "rm *.mp3"
            os.system(allmp3)
        print('done yup')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
