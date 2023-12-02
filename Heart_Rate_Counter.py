from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget
import pandas as pd


class Ui_Form(object):

    def browse_signal(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        if file_path:
            self.graphicsView.clear()
            data_header_rows = ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"]
            data = pd.read_csv(file_path,delim_whitespace=True, usecols=data_header_rows)
            self.y_coordinates = data["A2"]
            self.plot_signal()


    def plot_signal(self):
        self.minutes_counter = 0
        self.heart_rate = 0
        self.x_points_plotted = 0
        self.plotted_ecg_signal = self.graphicsView.plot(self.y_coordinates[:1], pen="b")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot_signal)
        self.timer.start()



    def update_plot_signal(self):
        self.x_points_plotted += 1
        self.graphicsView.setLimits(xMin=0, xMax=float('inf'))
        self.plotted_ecg_signal.setData(self.y_coordinates[0: self.x_points_plotted + 1])
        if self.x_points_plotted <= len(self.y_coordinates):
            self.graphicsView.getViewBox().setXRange(self.x_points_plotted-100,self.x_points_plotted + 100)
        if self.x_points_plotted <= len(self.y_coordinates):
            self.calculate_peaks()


    def calculate_peaks(self):
        self.peaks = 0
        for i in range(self.x_points_plotted):
            if i == 0 or i == 1 or i == 2:
                pass
            else:
                if ((400 <= self.y_coordinates[i - 3] <= 580) and
                        (580 < self.y_coordinates[i - 2] <= 800) and (
                        800 > self.y_coordinates[i - 1] >= 300) and (
                        580 >= self.y_coordinates[i] > 300)):
                    self.peaks += 1
        self.lcdNumber_2.display(self.peaks)
        if not self.x_points_plotted % 6000:
            self.minutes_counter += 1
            self.calculate_heart_rate()

    def calculate_heart_rate(self):
        if self.minutes_counter:
            self.heart_rate = int((self.peaks-(35*self.minutes_counter)) / self.minutes_counter)
        self.lcdNumber.display(self.heart_rate)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1333, 663)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 450))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox, clicked = lambda: self.browse_signal())
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Heart Rate Counter"))
        self.textBrowser.setHtml(_translate("Form",
         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
         "p, li { white-space: pre-wrap; }\n"
         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Heart Rate Counter</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Controls"))
        self.label.setText(_translate("Form", "Heart Rate"))
        self.label_2.setText(_translate("Form", "R Peaks Counter"))
        self.pushButton.setText(_translate("Form", "Browse Signal"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
