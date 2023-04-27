import glob
import gtts
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(40, 330, 90, 28))
        self.open_button.setObjectName("pushButton")
        self.open_button.clicked.connect(self.open_button_handler)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(80, 10, 171, 161))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        # text1 is the app title under logo
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 180, 311, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text1.setFont(font)
        self.text1.setScaledContents(True)
        self.text1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.text1.setObjectName("text1")
        # text2 is the label with creator credit
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(10, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text2.setFont(font)
        self.text2.setScaledContents(True)
        self.text2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.text2.setObjectName('text2')
        # text3 is the written directions in the main window
        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(10, 250, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text3.setFont(font)
        self.text3.setScaledContents(True)
        self.text3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.text3.setObjectName('text3')
        self.text3.setWordWrap(True)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(190, 330, 90, 28))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.exit_button_handler)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "txt2voice 2.0a", "txt2voice 2.0a"))
        self.open_button.setText(_translate("MainWindow", "Select file"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.text1.setText(_translate(
            "MainWindow", "txt2voice 2.0a"))
        self.text2.setText(_translate(
            'MainWindow', 'Tim Gore KE6QBV / WRUK522'))
        self.text3.setText(_translate(
            'MainWindow', 'Select a txt file that contains a listing of what you want generated. Software will create the voice files and save them to the same directory as this script. '))

    # This is where button action happens
    def open_button_handler(self):
        print('button pressed')
        self.open_dialog_box()

    # This button simply quits the program
    def exit_button_handler(self):
        MainWindow.close()

    # Creates dialog box to inform of task completion
    def show_dialog(self):
        dialog = QMessageBox(MainWindow)
        dialog.setText('Your files have been generated successfully.')
        dialog.setWindowTitle('Information')
        dialog.setIcon(QMessageBox.Information)
        dialog.exec_()

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
        self.show_dialog()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
