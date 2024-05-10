import random, socket, Server, json
from PyQt5 import QtCore, QtGui
class Maestro:
    def __init__(self, UI):
        self.ui = UI
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.generate_random_vitals)
        self.timer.start(2000)
        self.selected_patient = 1
        self.server = Server.Server(self)
        self.readings = [34]

    def generate_random_vitals(self):
        readings = dict()
        for i in range(1, 6):
            reading = random.randint(34, 42)
            readings[i] = reading
        self.send_to_server(readings)

    def send_to_server(self, readings : dict):
        try:
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_connection.connect(("192.168.1.4", 5050))
            socket_connection.sendall(json.dumps(readings).encode())
        except Exception as e:
            print("Error:", e)
            return None
        self.server.receive_data()

    def update_readings(self):
        temperature = self.retrieve_patient_data()
        if temperature is None:
            return
        self.ui.current_temp_LCD.display(temperature)
        if temperature > 38:
            self.ui.status_ok_label.setPixmap(QtGui.QPixmap(":/images/Assets/warning.png"))
        else:
            self.ui.status_ok_label.setPixmap(QtGui.QPixmap(":/images/Assets/checked.png"))
        self.readings.append(temperature)
        self.ui.temperature_graph.plot(self.server.steps, self.readings, pen = 'g')


    def close(self):
        if self.connection:
            self.connection.close()

    def search_button_clicked(self):
        patient_id = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        if int(patient_id) < 1 or int(patient_id) > 5 or patient_id == "":
            return None
        self.selected_patient = int(patient_id)

        self.update_readings()


    def retrieve_patient_data(self) -> int:
        return self.server.return_data(self.selected_patient)