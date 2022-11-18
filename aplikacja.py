from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
)
from PyQt6.QtCore import Qt

import konwertery

app = QApplication([])


# Na końcu ta funckja w tutorialu
def convertCilck():
    num = numLineEdit.text()

    numType = numTypeCombo.currentText()

    if (numType == "BIN"):
        convertedToBinLineEdit.setText(num)
        convertedToOctLineEdit.setText(konwertery.binToOct(num))
        convertedToDecLineEdit.setText(konwertery.binToDec(num))
        convertedToHexLineEdit.setText(konwertery.binToHex(num))

    elif (numType == "OCT"):
        convertedToBinLineEdit.setText(konwertery.octToBin(num))
        convertedToOctLineEdit.setText(num)
        convertedToDecLineEdit.setText(konwertery.octToDec(num))
        convertedToHexLineEdit.setText(konwertery.octToHex(num))

    elif (numType == "DEC"):
        convertedToBinLineEdit.setText(konwertery.decToBin(num))
        convertedToOctLineEdit.setText(konwertery.decToOct(num))
        convertedToDecLineEdit.setText(num)
        convertedToHexLineEdit.setText(konwertery.decToHex(num))

    elif (numType == "HEX"):
        convertedToBinLineEdit.setText(konwertery.hexToBin(num))
        convertedToOctLineEdit.setText(konwertery.hexToOct(num))
        convertedToDecLineEdit.setText(konwertery.hexToDec(num))
        convertedToHexLineEdit.setText(num)


window = QWidget()
window.setWindowTitle("Konwerter Systemów Liczbowych")

mainLayout = QVBoxLayout()

# Wiersz pierwszy
rowNumToConvert = QHBoxLayout()
rowNumToConvert.addWidget(QLabel("Podaj liczbę i jej typ: "))
numLineEdit = QLineEdit()
rowNumToConvert.addWidget(numLineEdit)

numTypeCombo = QComboBox()
numTypeCombo.addItems(["BIN", "OCT", "DEC", "HEX"])
rowNumToConvert.addWidget(numTypeCombo)

convertButton = QPushButton("Konwertuj")
convertButton.clicked.connect(convertCilck)

rowNumToConvert.addWidget(convertButton)

# Wiersze z wynikami konwersji

rowBinResult = QHBoxLayout()
rowBinResult.addWidget(QLabel("BIN: "), 0, Qt.AlignmentFlag.AlignCenter)
convertedToBinLineEdit = QLineEdit("0")
convertedToBinLineEdit.setReadOnly(True)
rowBinResult.addWidget(convertedToBinLineEdit, 0, Qt.AlignmentFlag.AlignCenter)


rowOctResult = QHBoxLayout()
rowOctResult.addWidget(QLabel("OCT: "), 0, Qt.AlignmentFlag.AlignCenter)
convertedToOctLineEdit = QLineEdit("0")
convertedToOctLineEdit.setReadOnly(True)
rowOctResult.addWidget(convertedToOctLineEdit, 0, Qt.AlignmentFlag.AlignCenter)

rowDecResult = QHBoxLayout()
rowDecResult.addWidget(QLabel("DEC: "), 0, Qt.AlignmentFlag.AlignCenter)
convertedToDecLineEdit = QLineEdit("0")
convertedToDecLineEdit.setReadOnly(True)
rowDecResult.addWidget(convertedToDecLineEdit, 0, Qt.AlignmentFlag.AlignCenter)

rowHexResult = QHBoxLayout()
rowHexResult.addWidget(QLabel("HEX: "), 0, Qt.AlignmentFlag.AlignCenter)
convertedToHexLineEdit = QLineEdit("0")
convertedToHexLineEdit.setReadOnly(True)
rowHexResult.addWidget(convertedToHexLineEdit, 0, Qt.AlignmentFlag.AlignCenter)

mainLayout.addLayout(rowNumToConvert)
mainLayout.addLayout(rowBinResult)
mainLayout.addLayout(rowOctResult)
mainLayout.addLayout(rowDecResult)
mainLayout.addLayout(rowHexResult)

window.setLayout(mainLayout)
window.show()
app.exec()
