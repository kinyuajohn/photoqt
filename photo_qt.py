# import modules
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
    QComboBox,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt

# Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotQt")
main_window.resize(900, 600)

# WIdgets/Objects
btn_folder = QPushButton("Folder")

file_list = QListWidget()

# Dropdown
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpen")
filter_box.addItem("B/W")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpen")
gray = QPushButton("B/W")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

picture_box = QLabel("Picture will appear here")

# Design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

col2.addWidget(picture_box)

master_layout.addLayout(col1)
master_layout.addLayout(col2)

main_window.setLayout(master_layout)

# RUn/Show
main_window.show()
app.exec_()
