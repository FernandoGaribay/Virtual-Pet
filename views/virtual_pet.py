import sys
import math

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPixmap

from config.window_settings import *
from config.pet_settings import *

class VirtualPet(QWidget):
    def __init__(self):
        super().__init__()

        self.velocity = 3
        self.threshold = 5

        self.setWindowFlags(WINDOW_FLAGS)
        self.setAttribute(WINDOW_ATTRIBUTES)
        self.setFixedSize(HEIGHT, WIDTH)
        self.setAttribute(Qt.WA_NoChildEventsForParent, True)
        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

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

        dx = cursor_pos.x() - (current_x + HEIGHT / 2)
        dy = cursor_pos.y() - (current_y + WIDTH / 2)
        distancia = math.hypot(dx, dy)

        if distancia >= self.threshold:
            self.threshold = MIN_TRESHOLD

            dx /= distancia
            dy /= distancia

            new_x = current_x + dx * self.velocity
            new_y = current_y + dy * self.velocity
            print(distancia)
            self.move(int(new_x), int(new_y))
        else:
            self.threshold = MAX_TRESHOLD
