from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Display do cronômetro
        self.stopwatch_display = QLabel("00:00:00.000")
        self.stopwatch_display.setAlignment(Qt.AlignCenter)
        self.stopwatch_display.setStyleSheet("font-size: 30px; font-family: 'Poppins'; color: white;")

        # Botões
        self.start_button = QPushButton("Iniciar Cronômetro")
        self.start_button.clicked.connect(self.toggle_stopwatch)

        self.reset_button = QPushButton("Voltar")
        self.reset_button.setVisible(False)
        self.reset_button.clicked.connect(self.record_lap)

        # Layout de botões
        self.layout.addWidget(self.stopwatch_display)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.reset_button)

        # Lista de voltas
        self.lap_list_display = QLabel("Voltas | Tempo das Voltas | Tempo Geral")
        self.lap_list_display.setVisible(False)  # Inicialmente invisível
        self.layout.addWidget(self.lap_list_display)

        # Lógica do cronômetro
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_str = "00:00:00.000"

        # Armazenar as voltas e tempos
        self.laps = []
        self.total_time = 0  # Tempo total das voltas

    def toggle_stopwatch(self):
        if not self.running:
            # Iniciar
            self.start_time = QTime.currentTime().msecsSinceStartOfDay() - self.elapsed_time
            self.timer.start(10)
            self.start_button.setText("Pausar Cronômetro")
            self.reset_button.setText("Voltar")
            self.reset_button.setVisible(True)
            self.lap_list_display.setVisible(True)  # Tornar visível a lista de voltas
            self.running = True
        else:
            # Pausar
            self.timer.stop()
            self.elapsed_time = QTime.currentTime().msecsSinceStartOfDay() - self.start_time
            self.start_button.setText("Retomar Cronômetro")
            self.reset_button.setText("Resetar Cronômetro")
            self.reset_button.setVisible(True)
            self.running = False

    def reset_stopwatch(self):
        self.timer.stop()
        self.running = False
        self.elapsed_time = 0
        self.total_time = 0
        self.time_str = "00:00:00.000"
        self.stopwatch_display.setText(self.time_str)
        self.start_button.setText("Iniciar Cronômetro")
        self.reset_button.setVisible(False)
        self.lap_list_display.setVisible(False)  # Esconder lista de voltas quando resetado
        self.laps = []
        self.lap_list_display.setText("Voltas | Tempo das Voltas | Tempo Geral")

    def record_lap(self):
        # Registra a volta e atualiza a lista de voltas
        lap_time = self.stopwatch_display.text()
        self.laps.append((lap_time, self.elapsed_time / 1000))  # Armazenar o tempo da volta e o tempo geral
        self.update_lap_list()
        print("Volta registrada:")
        print(f"Voltas: {len(self.laps)}")
        print(f"Tempo das Voltas: {lap_time}")
        print(f"Tempo Geral: {self.elapsed_time / 1000:.2f} s")

    def update_lap_list(self):
        # Atualiza a lista de voltas
        lap_info = "Voltas | Tempo das Voltas | Tempo Geral\n"
        total_time = self.elapsed_time / 1000  # Tempo total em segundos
        for i, (lap, lap_time) in enumerate(self.laps, 1):
            lap_info += f"{i} | {lap} | {total_time:.2f} s\n"
        self.lap_list_display.setText(lap_info)

    def update_time(self):
        # Atualiza o tempo do cronômetro
        current = QTime.currentTime().msecsSinceStartOfDay() - self.start_time
        minutes = current // 60000
        seconds = (current // 1000) % 60
        milliseconds = current % 1000
        self.time_str = f"{minutes:02}:{seconds:02}:{milliseconds:03}"
        self.stopwatch_display.setText(self.time_str)
