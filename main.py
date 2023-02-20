import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MapViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Yandex Maps Viewer')
        self.line = QLineEdit(self)
        self.line.resize(100, 30)
        self.line.move(215, 562)
        self.line2 = QLineEdit(self)
        self.line2.resize(200, 30)
        self.line2.move(10, 562)
        self.webEngineView = QWebEngineView(self)
        self.webEngineView.setGeometry(0, 0, 800, 560)
        self.btn = QPushButton('>', self)
        self.btn.clicked.connect(self.zoomed)
        self.btn.resize(30, 30)
        self.btn.move(320, 562)

    def zoomed(self):
        self.coords = self.line2.text()
        self.zoom = self.line.text()
        self.webEngineView.load(QUrl(f"https://yandex.ru/maps/?ll={self.coords}&z={self.zoom}"))
        self.webEngineView.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapViewer()
    ex.show()
    sys.exit(app.exec_())