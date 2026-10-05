#Afficher une string dans Maya 
#Fenetre de dialogue ou on peux ecrire du texte et un bouton écrit Show et ca fait apparaitre le message. 
#PySide6 dans Maya

#Setup maya - l'extention -> Maya Python, permet de coder dans vs code et l'executer dans Maya, aller chercher l'interpreter de mayapy.exe
#from maya import cmds;cmds.commandPort(name='127.0.0.1:7002', sourceType='python', echoOutput=True) dans le window script editor de maya
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget): #Parent QWidget donc hérite de QWidget
    def __init__(self): #Constructeur
        super().__init__() #Super = constructeur du parent
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        global text_edit
        text_edit = QLineEdit()
        button = QPushButton("Ok")
        

        
        layout.addWidget(label)
        layout.addWidget(text_edit)
        layout.addWidget(button)

        button.clicked.connect(lambda : self.on_click())


    def on_click(self):
         QMessageBox.information(
            self,
            'Information',
            f'{text_edit.text()}'
            )
       


def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()
