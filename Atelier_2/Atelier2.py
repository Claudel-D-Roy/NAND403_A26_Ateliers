import sys
import json
from PySide6 import QApplication, QMainWindow

file_path = sys.argv[1]

print(file_path)

try: 
    file = open(file_path)
    data = json.load(file)
    print(type(data))

except: 
    print(f"Could not load data from {file_path}")


app = QApplication([])

table = QTableWidget()
table.setRowCount(len(data))
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["name", "price", "type"])

for i in range(len(data)):
    table.setItem(i, 0, QTableWidgetItem(data[i]["name"]))
    table.setItem(i, 1, QTableWidgetItem(str(data[i]["price"])))
    table.setItem(i, 2, QTableWidgetItem(data[i]["type"]))


for i in data:
    for k in i.items():
        print(f"{k}") 

window = QMainWindow();
window.show()
sys.exit(app.exit())

