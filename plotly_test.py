from PySide6.QtWidgets import QWidget, QApplication, QGridLayout
import sys

import pyqtgraph as pg
import numpy as np

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #00AAAA;')
        self.resize(650, 650)

        self.box = QGridLayout()
        self.box.setSpacing(5)
        self.box.setContentsMargins(5,5,5,5)

        self.setLayout(self.box)
        self.graph_one()
    
    def graph_one(self):
        plt = pg.PlotWidget(title='grafica lineal')
        x = np.linspace(0,100,50)
        plt.plot(x,2*np.cos(x),Symbol = 'star',symblBrush="00AAAA",color="00AAAA",pen="#00AAAA",width=2, SymbolPen="00AAAA")
        self.box.addWidget(plt,0,1)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    my_app=GUI()
    my_app.show()
    sys.exit(app.exec_())