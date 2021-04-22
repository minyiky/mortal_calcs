# %%

import json
import math
from collections import namedtuple

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import bow_calc_ui
import bow_calc_single_ui

BowMatEq = namedtuple('BowMatEq', ['str_m', 'str_c', 'rng_m', 'rng_c', 'dura'])

with open('bow_data.json', 'r') as fp:
    bowData = json.load(fp)

bowMechanics = ('decurve',)
bowTypes = ('short', 'long')
bowMats = (
    'denseCrepite',
    'crepite',
    'spongewood',
)

char_strength = 109

bowList = []
bowListSorted = []


def addTableRow(table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)
        col = 0
        for col, item in enumerate(row_data):
            cell = QTableWidgetItem(item)
            table.setItem(row, col, cell)


#handler for the signal aka slot
def calculate(checked):
    bowMechanics = []
    bowTypes = []
    bowMats = []
    if form.denseCrepite.isChecked(): bowMats.append('Dense Crepite')
    if form.crepite.isChecked(): bowMats.append('Crepite')
    if form.molarium.isChecked(): bowMats.append('Molarium')
    if form.emalj.isChecked(): bowMats.append('Emalj')
    if form.greatHorn.isChecked(): bowMats.append('GreatHorn')
    if form.compactHorn.isChecked(): bowMats.append('Compact Horn')
    if form.horn.isChecked(): bowMats.append('Horn')
    if form.ironBone.isChecked(): bowMats.append('Iron Bone')
    if form.boneTissue.isChecked(): bowMats.append('Bone Tissue')
    if form.spongeWood.isChecked(): bowMats.append('Spongewood')
    if form.whiteWood.isChecked(): bowMats.append('Whitewood')
    if form.firmWood.isChecked(): bowMats.append('Firmwood')
    if form.greyWood.isChecked(): bowMats.append('Greywood')
    if form.dappleWood.isChecked(): bowMats.append('Dapplewood')
    if form.brownWood.isChecked(): bowMats.append('Brownwood')
    if form.blackWood.isChecked(): bowMats.append('Blackwood')
    if form.ironWood.isChecked(): bowMats.append('Ironwood')
    if form.stoneWood.isChecked(): bowMats.append('Stonewood')
    if len(bowMats) == 0:
        print('You must select at least one bow material')
        return
    if form.short_2.isChecked(): bowTypes.append('Short')
    if form.long_2.isChecked(): bowTypes.append('Long')
    if form.asym_2.isChecked(): bowTypes.append('Asymmetrical')
    if len(bowTypes) == 0:
        print('You must select at least one bow type')
        return
    if form.decurve.isChecked(): bowMechanics.append('Decurve')
    if form.recurve.isChecked(): bowMechanics.append('Recurve')
    if form.flat.isChecked(): bowMechanics.append('Flat')
    if len(bowMechanics) == 0:
        print('You must select at least one bow mechanic')
        return

    char_strength = form.spinStrength.value()
    print(f'|{"Bow Type":^10}|{"Bow Mechanic":^14}|{"Left Material":^15}|{"Right Material":16}|{"Perctentage":^13}|{"Strength":^10}|{"Range":^9}|{"Durability":^12}|')
    print(f'|{"-"*10}|{"-"*14}|{"-"*15}|{"-"*16}|{"-"*13}|{"-"*10}|{"-"*9}|{"-"*12}|')    
    for Mechanic in bowMechanics:
        for Type in bowTypes:
            for leftMat in bowMats:
                for rightMat in bowMats:
                    params = BowMatEq(*bowData[f"{Mechanic}_{Type}_{leftMat}_{rightMat}"])
                    if params.str_m > 0 and params.rng_m > 0:
                        print((char_strength - params.str_c) / params.str_m)
                        x = math.floor((char_strength - params.str_c) / params.str_m)
                    if params.str_m < 0 and params.rng_m < 0:
                        x = math.ceil((char_strength - params.str_c) / params.str_m)
                    if params.str_m < 0 and params.rng_m > 0:
                        x = 95
                    if params.str_m > 0 and params.rng_m < 0:
                        x = 5
                    if x > 95: x=95
                    if x < 5: x=5
                    strength = params.str_m*x + params.str_c
                    rng = params.rng_m*x + params.rng_c
                    if strength <= char_strength:
                        str_strength = f'   {strength:.2F}'[-7:]
                        str_rng = f'   {rng:.2F}'[-7:]
                        str_dura = f'   {params.dura:.2F}'[-7:]
                        print(f'|{Type:^10}|{Mechanic:^14}|{leftMat:^15}|{rightMat:^16}|{x:^13}|{str_strength:^10}|{str_rng:^9}|{str_dura:^12}|')
                        addTableRow(form.tableWidget, [Type, Mechanic, leftMat, rightMat, str(x), str_strength, str_rng, str_dura])

def clear(checked):
    form.tableWidget.setRowCount(0)

def show_single(checked):
    popup = Popup()
    popup.show()
    popup.exec()

class ExampleApp(QtWidgets.QMainWindow, bow_calc_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


class Popup(QtWidgets.QDialog, bow_calc_single_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(Popup, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.pushButton.clicked.connect(calculate)
    form.pushButton_2.clicked.connect(clear)
    form.pushButton_3.clicked.connect(show_single)
    form.show()
    app.exec_()
