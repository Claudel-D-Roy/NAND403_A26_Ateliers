import math

from maya import cmds
from maya import OpenMayaUI as omui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QSlider,
    QLabel,
    QPushButton,
)
from shiboken6 import wrapInstance


def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class RockMaker(QDialog):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowTitle("Rock Maker")
        self.setMinimumWidth(260)

        self.current_rock = None
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)
        form = QFormLayout()
        main_layout.addLayout(form)

        self.subdivisions_slider = self.add_slider(form, "Subdivisions", 4, 64, 20)
        self.amplitude_slider = self.add_slider(form, "Amplitude", 0, 100, 30, divisor=100)
        self.frequency_slider = self.add_slider(form, "Frequency", 5, 80, 30, divisor=10)
        self.seed_slider = self.add_slider(form, "Seed", 0, 100, 0)

        self.subdivisions_slider.valueChanged.connect(self.update_rock)
        self.amplitude_slider.valueChanged.connect(self.update_rock)
        self.frequency_slider.valueChanged.connect(self.update_rock)
        self.seed_slider.valueChanged.connect(self.update_rock)

        create_button = QPushButton("Create rock")
        create_button.clicked.connect(self.make_rock)
        main_layout.addWidget(create_button)

    def add_slider(self, form, name, minimum, maximum, value, divisor=1):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(minimum, maximum)
        slider.setValue(value)

        value_label = QLabel(f"{value / divisor:g}")
        value_label.setMinimumWidth(30)
        slider.valueChanged.connect(lambda v: value_label.setText(f"{v / divisor:g}"))

        row = QHBoxLayout()
        row.addWidget(slider)
        row.addWidget(value_label)
        form.addRow(name, row)
        return slider

    def make_rock(self):
        self.current_rock = self.create_rock(
            self.subdivisions_slider.value(),
            self.amplitude_slider.value() / 100,
            self.frequency_slider.value() /10,
            self.seed_slider.value(),
        )


    def update_rock(self):
        if self.current_rock and cmds.objExists(self.current_rock):
            cmds.delete(self.current_rock)
        self.make_rock()

    def create_rock(self, subdivisions, amplitude, frequency, seed):

        self.sphere= cmds.polySphere(sx=subdivisions, sy=subdivisions)[0]
        vertices = cmds.ls(f'{self.sphere}.vtx[*]', flatten=True)

        for vertex in vertices:
            pos_vertex = cmds.pointPosition(vertex, world=True)
            bump = self.get_bump(pos_vertex[0], pos_vertex[1], pos_vertex[2], frequency, seed)
            random_vertex = bump * amplitude
          
            cmds.move(pos_vertex[0] * random_vertex, pos_vertex[1] * random_vertex, pos_vertex[2] * random_vertex, vertex, r = True ) 

        return self.sphere
                               
    def get_bump(self, x, y, z, frequency, seed):
        return (math.sin(x * frequency + seed)
                + math.sin(y * frequency + seed * 2)
                + math.sin(z * frequency + seed * 3)) / 3


def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RockMaker()
    tool_window.show()


show_tool()
