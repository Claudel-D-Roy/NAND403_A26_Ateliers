import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QGridLayout,
    QSpinBox 
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 6")
        self.setMinimumWidth(300)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)
        grid = QGridLayout()

        label_object = QLabel("Number of fences")

        label_pos = QLabel("Position")
        label_posX = QLabel("X")
        label_posY = QLabel("Y")
        label_posZ = QLabel("Z")

        label_scale = QLabel("Scale")
        label_scalX = QLabel("X")
        label_scalY = QLabel("Y")
        label_scalZ = QLabel("Z")

        self.nbr_fences = QSpinBox()
        self.edit_posX = QSpinBox()
        self.edit_posY = QSpinBox()
        self.edit_posZ = QSpinBox()

        self.edit_scalx = QSpinBox()
        self.edit_scaly = QSpinBox()
        self.edit_scalz = QSpinBox()

        grid.addWidget(label_object, 0, 0)
        grid.addWidget(self.nbr_fences, 0, 2)

        grid.addWidget(label_pos, 1, 0)
        grid.addWidget(label_posX, 1, 1)
        grid.addWidget(self.edit_posX, 1, 2)

        grid.addWidget(label_posY, 2, 1)
        grid.addWidget(self.edit_posY, 2, 2)

        grid.addWidget(label_posZ, 3, 1)
        grid.addWidget(self.edit_posZ , 3, 2)

        grid.addWidget(label_scale, 4, 0)
        grid.addWidget(label_scalX, 4, 1)
        grid.addWidget(self.edit_scalx, 4, 2)

        grid.addWidget(label_scalY, 5, 1)
        grid.addWidget(self.edit_scaly, 5, 2)

        grid.addWidget(label_scalZ, 6, 1)
        grid.addWidget(self.edit_scalz, 6, 2)

        layout.addLayout(grid)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
       nb_obj = self.nbr_fences.value()
       
       pox = self.edit_posX.value()
       poy = self.edit_posY.value()
       poz = self.edit_posZ.value()

       scal_x = self.edit_scalx.value()
       scal_y = self.edit_scaly.value()
       scal_z = self.edit_scalz.value()      

       for i in range(nb_obj):
            fence1 = cmds.polyCube()[0]
            cmds.move(pox, poy, poz, fence1, absolute = True)
            cmds.scale(scal_x, scal_y + 5, scal_z, fence1, absolute = True)

            fence2 = cmds.polyCube()[0]
            cmds.move(pox, poy + poy/2, poz, fence2, absolute = True)
            cmds.scale(scal_x + 5, scal_y , scal_z, fence2, absolute = True)

            fence3 = cmds.polyCube()[0]
            cmds.move(pox, poy - poy/2, poz, fence3, absolute = True)
            cmds.scale(scal_x + 5, scal_y , scal_z, fence3, absolute = True)




def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()