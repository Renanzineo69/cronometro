from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget
from styles.theme import get_dark_theme, get_light_theme  # Certifique-se de que estas funções retornam strings de cor

class Clock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_time = QTime.currentTime()

        # Timer to update the time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Updates every second

        # Set the widget size to fit the circles
        self.setMinimumSize(400, 400)

    def update_time(self):
        self.current_time = QTime.currentTime()
        self.update()  # This triggers a repaint of the widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable anti-aliasing for smooth circles

        center_x = int(self.width() / 2)
        center_y = int(self.height() / 2)

        # Get the background color from the current theme (returns color string)
        background_color = QColor(get_dark_theme())  # If using light theme, use get_light_theme()

        # Draw the background circle
        painter.setPen(QColor(255, 255, 255, 100))  # Light white with some transparency
        painter.setBrush(background_color)  # Set the background color
        painter.drawEllipse(center_x - 150, center_y - 150, 300, 300)  # Outer circle for hours

        # Draw the hour circle
        self.draw_time_circle(painter, center_x, center_y, 150, 10, self.current_time.hour(), 24)  # Hours circle

        # Draw the minute circle
        self.draw_time_circle(painter, center_x, center_y, 120, 8, self.current_time.minute(), 60)  # Minute circle

        # Draw the second circle
        self.draw_time_circle(painter, center_x, center_y, 90, 6, self.current_time.second(), 60)  # Second circle

        # Draw the time label in the center (centralized text)
        painter.setPen(QColor(255, 255, 255))
        
        # Set a larger font size
        font = QFont()
        font.setPointSize(30)  # Increase the font size
        painter.setFont(font)
        
        # Centralize the text by adjusting its position
        text = self.current_time.toString("hh:mm:ss")
        text_rect = painter.fontMetrics().boundingRect(text)
        text_rect.moveCenter(self.rect().center())  # Center the text in the widget
        painter.drawText(text_rect, Qt.AlignCenter, text)

    def draw_time_circle(self, painter, center_x, center_y, radius, width, time_value, max_value):
        angle = (time_value / max_value) * 360
        start_angle = -90  # Starting at the top (12 o'clock)

        # Draw the arc (circle)
        painter.setPen(QColor(0, 255, 0))  # Green color for the current time arc
        painter.setBrush(Qt.transparent)  # No fill for the arc

        # Convert angle to int to avoid TypeError
        painter.drawArc(center_x - radius, center_y - radius, radius * 2, radius * 2, start_angle * 16, int(-angle * 16))  # Arc angle * 16
