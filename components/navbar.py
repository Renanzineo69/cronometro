# components/navbar.py

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Navbar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent_window = parent  # Guardar referência à janela principal

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Botão Relógio
        self.relogio_button = QPushButton("Relógio")
        self.relogio_button.clicked.connect(self.show_relogio)
        self.layout.addWidget(self.relogio_button)

        # Botão Cronômetro
        self.cronometro_button = QPushButton("Cronômetro")
        self.cronometro_button.clicked.connect(self.show_cronometro)
        self.layout.addWidget(self.cronometro_button)

        # Botão Alarme
        self.alarm_button = QPushButton("Alarme")
        self.alarm_button.clicked.connect(self.show_alarm)
        self.layout.addWidget(self.alarm_button)

        # Centralizar a navbar
        self.layout.setAlignment(Qt.AlignCenter)

    def show_relogio(self):
        self.parent_window.show_relogio()

    def show_cronometro(self):
        self.parent_window.show_cronometro()

    def show_alarm(self):
        self.parent_window.show_alarm()
