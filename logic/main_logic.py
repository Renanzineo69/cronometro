# logic/main_logic.py

class MainLogic:
    def __init__(self, stopwatch_display, alarm_time_display):
        self.stopwatch_display = stopwatch_display
        self.alarm_time_display = alarm_time_display

    def start_stopwatch(self):
        print("Iniciar cronômetro pela lógica principal")

    def reset_stopwatch(self):
        print("Resetar cronômetro pela lógica principal")

    def set_alarm(self, alarm_time):
        print(f"Alarme definido pela lógica principal: {alarm_time}")
