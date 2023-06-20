from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtWidgets import QWidget, QSlider, QTextBrowser, QHBoxLayout, QTextEdit, QPushButton, QApplication, \
    QGridLayout, QLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.text_edit = QTextBrowser(self)
        self.text_edit.setText("Started app")

        self.slider = QSlider(self)
        self.slider.setRange(50, 75)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.append_text)
        self.slider.setOrientation(Qt.Orientation.Horizontal)


        self.pushbutton = QPushButton(self)
        self.pushbutton.show()
        self.pushbutton.setText("Schließen")
        self.pushbutton.clicked.connect(QApplication.instance().quit)

        self.label1 = QLabel(self)
        self.label1.setText("Slider")

        self.label2 = QLabel(self)
        self.label2.setText("Textfeld")

        # A1: Umstellung auf QGridLayout mit vertikaler Orientierung
        #layout = QHBoxLayout(self)
        #layout.addWidget(self.pushbutton)
        #layout.addWidget(self.slider)
        #layout.addWidget(self.text_edit)

        layout = QGridLayout(self)
        layout.addWidget(self.pushbutton, 3, 2)
        layout.addWidget(self.slider, 1, 2)
        layout.addWidget(self.text_edit, 2, 2)
        layout.addWidget(self.label1, 1, 1)
        layout.addWidget(self.label2, 2, 1, Qt.AlignmentFlag.AlignTop)


        self.setLayout(layout)

    @pyqtSlot(int)
    def append_text(self, value_as_int):
        text = "Value Changed: " + str(value_as_int)
        self.text_edit.append(text)
