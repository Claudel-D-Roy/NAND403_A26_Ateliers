import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QSpinBox,
    QDoubleSpinBox
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
        label_spaces = QLabel("Spaces")  

        label_pos = QLabel("Position")
        label_posX = QLabel("X")
        label_posY = QLabel("Y")
        label_posZ = QLabel("Z")

        label_scale = QLabel("Scale")
        label_scalX = QLabel("X")
        label_scalY = QLabel("Y")
        label_scalZ = QLabel("Z")

        self.nbr_fences = QSpinBox()
        self.espace = QSpinBox()
        self.edit_posX = QDoubleSpinBox()
        self.edit_posY = QDoubleSpinBox()
        self.edit_posZ = QDoubleSpinBox()

        self.edit_scalx = QDoubleSpinBox()
        self.edit_scaly = QDoubleSpinBox()
        self.edit_scalz = QDoubleSpinBox()

        grid.addWidget(label_object, 0, 0)
        grid.addWidget(self.nbr_fences, 0, 2)

        grid.addWidget(label_spaces, 1, 0)
        grid.addWidget(self.espace, 1, 2)


        grid.addWidget(label_pos, 2, 0)
        grid.addWidget(label_posX, 2, 1)
        grid.addWidget(self.edit_posX, 2, 2)

        grid.addWidget(label_posY, 3, 1)
        grid.addWidget(self.edit_posY, 3, 2)

        grid.addWidget(label_posZ, 4, 1)
        grid.addWidget(self.edit_posZ , 4, 2)

        grid.addWidget(label_scale, 5, 0)
        grid.addWidget(label_scalX, 5, 1)
        grid.addWidget(self.edit_scalx, 5, 2)

        grid.addWidget(label_scalY, 6, 1)
        grid.addWidget(self.edit_scaly, 6, 2)

        grid.addWidget(label_scalZ, 7, 1)
        grid.addWidget(self.edit_scalz, 7, 2)

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
       espace = self.espace.value()

       post_h = 4.0                    
       hauteur = post_h * scal_y         
       bas = poy - hauteur / 2  

       init = cmds.polyCube(w = 0.4, h = post_h, d = 0.2 )[0]
       cmds.move(pox, poy, poz, init, absolute = True)
       cmds.scale(scal_x, scal_y, scal_z, init, absolute = True)

       for i in range(1, nb_obj):
            new_init = cmds.duplicate()[0]
            position_x = (pox + i) * espace
            cmds.move(position_x, poy, poz, new_init)
            print(f"post :  {position_x}")

            for s in range(nb_obj - 1):
                position_hor = pox + (s + 0.5) * espace
                print(f"bar :  {position_hor}")
                for ratio in (0.3, 0.7):
                    new_init_horizontal = cmds.duplicate(init)[0]
                    cmds.move(position_hor, bas + hauteur * ratio , poz, new_init_horizontal)
                    cmds.rotate(90, 90, 0,new_init_horizontal)
            
    

               

            



def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()