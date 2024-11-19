import sys
from PyQt5.QtWidgets import QApplication
from virtual_pet import VirtualPet

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mascota = VirtualPet()
    mascota.show()
    sys.exit(app.exec_())
