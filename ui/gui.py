from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys

def start_gui():
    """Starts the graphical user interface."""
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Network Multi-Tool")
    label = QLabel("GUI is under construction!", parent=window)
    label.move(50, 50)
    window.setGeometry(100, 100, 400, 200)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_gui()
