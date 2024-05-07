from PyQt5 import QtCore, QtGui, QtWidgets
import sys, GUI.resources as resources
from AppManager import Maestro
from pyqtgraph import PlotWidget
import socket
import json

class   (object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 680)
        MainWindow.setMinimumSize(QtCore.QSize(1126, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1126, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#3A3B3C;\n"
"background-image: url(:/images/Assets/bg2.jpg);\n"
"color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 751, 301))
        self.groupBox.setObjectName("groupBox")
        self.ECG_Graph = PlotWidget(self.groupBox)
        self.ECG_Graph.setGeometry(QtCore.QRect(10, 20, 731, 271))
        self.ECG_Graph.setObjectName("ECG_Graph")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(790, 40, 311, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.current_temp_LCD = QtWidgets.QLCDNumber(self.groupBox_2)
        self.current_temp_LCD.setGeometry(QtCore.QRect(10, 30, 181, 161))
        self.current_temp_LCD.setObjectName("current_temp_LCD")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.status_ok_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.status_ok_label_2.setGeometry(QtCore.QRect(210, 60, 91, 91))
        self.status_ok_label_2.setText("")
        self.status_ok_label_2.setPixmap(QtGui.QPixmap(":/images/Assets/thermometer.png"))
        self.status_ok_label_2.setScaledContents(True)
        self.status_ok_label_2.setObjectName("status_ok_label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 0, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(660, 0, 141, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.status_ok_label = QtWidgets.QLabel(self.centralwidget)
        self.status_ok_label.setGeometry(QtCore.QRect(790, 390, 91, 91))
        self.status_ok_label.setText("")
        self.status_ok_label.setPixmap(QtGui.QPixmap(":/images/Assets/checked.png"))
        self.status_ok_label.setScaledContents(True)
        self.status_ok_label.setObjectName("status_ok_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RealTime Monitoring System"))
        self.groupBox.setTitle(_translate("MainWindow", "Chart"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Temperature"))
        self.label.setText(_translate("MainWindow", "Current Temperature"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Patient ID"))
        self.commandLinkButton.setText(_translate("MainWindow", "Search"))
from pyqtgraph import PlotWidget


# Mansy Code
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.search_button_clicked)

    def search_button_clicked(self):
        # Retrieve patient ID entered in the search bar
        patient_id = self.ui.lineEdit.text()

        # Send patient ID to server for data retrieval
        data = self.retrieve_patient_data(patient_id)

        # Display retrieved data (replace this with your actual visualization code)
        print("Retrieved Data:", data)

    def retrieve_patient_data(self, patient_id):
        # Establish connection to the server and send request for patient data
        server_address = ('localhost', 8000)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect(server_address)
                # Send patient ID to server
                client_socket.sendall(json.dumps({'patient_id': patient_id}).encode())
                # Receive response from server
                data = client_socket.recv(1024)
                return json.loads(data.decode())
        except Exception as e:
            print("Error:", e)
            return None


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     Maestro = Maestro(ui)
#     MainWindow.show()
#     sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())