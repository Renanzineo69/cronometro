# content/main_window.py

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from styles.theme import get_dark_theme, get_light_theme
from components.navbar import Navbar
from components.clock import Clock
from components.stopwatch import Stopwatch
from components.alarm import Alarm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relógio com Cronômetro e Alarme")
        self.setMinimumSize(600, 500)

        # Layout principal
        main_layout = QVBoxLayout()

        # Navbar
        self.navbar = Navbar(self)
        main_layout.addWidget(self.navbar)

        # StackedWidget
        self.stacked_widget = QStackedWidget()
        self.tab_relogio = Clock(self)
        self.tab_stopwatch = Stopwatch(self)
        self.tab_alarm = Alarm(self)

        self.stacked_widget.addWidget(self.tab_relogio)
        self.stacked_widget.addWidget(self.tab_stopwatch)
        self.stacked_widget.addWidget(self.tab_alarm)

        main_layout.addWidget(self.stacked_widget)

        # Widget central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Timer do relógio em tempo real (Clock)
        # Se o 'Clock' já tiver um timer interno, não precisa duplicar

        # Definir tema inicial
        self.set_theme("dark")

    def set_theme(self, theme_type):
        if theme_type == "dark":
            self.setStyleSheet(get_dark_theme())
        else:
            self.setStyleSheet(get_light_theme())

    # Funções para trocar de tela
    def show_relogio(self):
        self.stacked_widget.setCurrentWidget(self.tab_relogio)

    def show_cronometro(self):
        self.stacked_widget.setCurrentWidget(self.tab_stopwatch)

    def show_alarm(self):
        self.stacked_widget.setCurrentWidget(self.tab_alarm)
