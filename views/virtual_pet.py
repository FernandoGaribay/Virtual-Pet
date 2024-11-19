import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap


class VirtualPet(QWidget):
    def __init__(self):
        super().__init__()

        self._HEIGHT = 50
        self._WIDTH = 50
        self._MIN_TRESHOLD = 5
        self._MAX_TRESHOLD = 50
        self.velocity = 3
        self.threshold = 5

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(self._HEIGHT, self._WIDTH)

        self.image_path = 'resources/cat.png'
        self.pixmap = QPixmap(self.image_path)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(15)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        img_rect = self.rect()
        painter.drawPixmap(img_rect, self.pixmap)

    def update_position(self):
        cursor_pos = QApplication.instance().desktop().cursor().pos()

        current_x = self.x()
        current_y = self.y()

        dx = cursor_pos.x() - (current_x + self._HEIGHT / 2)
        dy = cursor_pos.y() - (current_y + self._WIDTH / 2)
        distancia = math.hypot(dx, dy)

        if distancia >= self.threshold:
            self.threshold = self._MIN_TRESHOLD

            dx /= distancia
            dy /= distancia

            new_x = current_x + dx * self.velocity
            new_y = current_y + dy * self.velocity

            self.move(int(new_x), int(new_y))
        else:
            self.threshold = self._MAX_TRESHOLD
