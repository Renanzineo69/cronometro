# components/clock.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt

class Clock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.clock_display = QLabel("00:00:00")
        self.clock_display.setAlignment(Qt.AlignCenter)
        self.clock_display.setStyleSheet("font-size: 30px; font-family: 'Poppins'; color: white;")

        self.layout.addWidget(self.clock_display)

        # Timer para atualizar o relógio
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)

    def update_clock(self):
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss")
        self.clock_display.setText(formatted_time)
