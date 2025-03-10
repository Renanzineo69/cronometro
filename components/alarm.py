# components/alarm.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Alarm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.alarm_time_display = QLabel("Defina o alarme (HH:MM):")
        self.alarm_time_display.setAlignment(Qt.AlignCenter)
        self.alarm_time_display.setStyleSheet("font-size: 20px; font-family: 'Poppins'; color: white;")

        self.alarm_input = QLineEdit()
        self.alarm_input.setPlaceholderText("Ex: 14:30")
        self.alarm_input.setStyleSheet("background-color: #4a4a4a; color: white; border-radius: 8px; padding: 10px;")

        self.alarm_button = QPushButton("Definir Alarme")
        self.alarm_button.clicked.connect(self.set_alarm)

        self.layout.addWidget(self.alarm_time_display)
        self.layout.addWidget(self.alarm_input)
        self.layout.addWidget(self.alarm_button)

    def set_alarm(self):
        alarm_time = self.alarm_input.text()
        print(f"Alarme definido para: {alarm_time}")
