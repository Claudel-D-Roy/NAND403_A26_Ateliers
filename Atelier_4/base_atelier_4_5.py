import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QGridLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        grid = QGridLayout()

        self.label_nbr = QLineEdit("0")
        label_object = QLabel("Number of objects")
        

        label_min = QLabel("Min")
        label_max = QLabel("Max")

        label_posX = QLabel("Position X")
        label_posY = QLabel("Position Y")
        label_posZ = QLabel("Position Z")
        label_scale = QLabel("Scale")

        self.min_posX = QLineEdit("0")
        self.max_posX = QLineEdit("0")
 

        self.min_posY = QLineEdit("0")
        self.max_posY = QLineEdit("0")

        self.min_posZ = QLineEdit("0")
        self.max_posZ = QLineEdit("0")

        self.min_scale = QLineEdit("0")
        self.max_scale = QLineEdit("0")

        grid.addWidget(label_object, 0, 0)
        grid.addWidget(self.label_nbr, 0, 1)

        grid.addWidget(label_min, 1, 1)
        grid.addWidget(label_max, 1, 2)

        grid.addWidget(label_posX, 2, 0)
        grid.addWidget(self.min_posX, 2, 1)
        grid.addWidget(self.max_posX, 2, 2)

        grid.addWidget(label_posY, 3, 0)
        grid.addWidget(self.min_posY, 3, 1)
        grid.addWidget(self.max_posY, 3, 2)

        grid.addWidget(label_posZ, 4, 0)
        grid.addWidget(self.min_posZ, 4, 1)
        grid.addWidget(self.max_posZ, 4, 2)

        grid.addWidget(label_scale, 5, 0)
        grid.addWidget(self.min_scale, 5, 1)
        grid.addWidget(self.max_scale, 5, 2)

        layout.addLayout(grid)
        

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
       
       nb_obj = int(self.label_nbr.text())
       pox_min = float(self.min_posX.text())
       pox_max = float(self.max_posX.text())
       poy_min = float(self.min_posY.text())
       poy_max = float(self.max_posY.text())
       poz_min = float(self.min_posZ.text())
       poz_max = float(self.max_posZ.text())
       scal_min = float(self.min_scale.text())
       scal_max = float(self.max_scale.text())
       

       for i in range(nb_obj):
            forme = random.choice(["cube", "cylindre", "sphere"])

            posX = random.uniform(pox_min, pox_max)
            posY = random.uniform(poy_min, poy_max)
            posZ = random.uniform(poz_min, poz_max)
            scale = random.uniform(scal_min, scal_max)

            print(f"{nb_obj}, {posX}, {posY}, {posZ}, {scale}, {forme}")
            if forme == "cube":
                objet = cmds.polyCube()[0]
                cmds.move(posX, posY, posZ, objet, absolute = True)
                cmds.scale(scale, scale, scale, objet, absolute = True)

            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
                cmds.move(posX, posY, posZ, objet, absolute = True)
                cmds.scale(scale, scale, scale, objet, absolute = True)
            else:
                objet = cmds.polySphere()[0]
                cmds.move(posX, posY, posZ, objet, absolute = True)
                cmds.scale(scale, scale, scale, objet, absolute = True)

            #random_value = random.uniform(-10, 10)
            #cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()