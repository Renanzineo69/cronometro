# styles/theme.py

def get_dark_theme():
    return """
    QMainWindow {
        background-color: #333333;
    }
    QPushButton {
        background-color: #555555;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    QLabel {
        color: white;
    }
    """

def get_light_theme():
    return """
    QMainWindow {
        background-color: #f0f0f0;
    }
    QPushButton {
        background-color: #e0e0e0;
        color: black;
        border-radius: 8px;
        padding: 10px;
    }
    QLabel {
        color: black;
    }
    """
