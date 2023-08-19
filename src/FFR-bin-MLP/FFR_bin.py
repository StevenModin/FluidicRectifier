# encoding == utf-8
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem
from Ui_toolkit import Ui_Form
from MLP_model import Predictor
import re
import csv
import util


class MyWindow(Ui_Form, QWidget):
    # static variables
    ckptPattern = re.compile(r".+\.ckpt$")
    csvPattern = re.compile(r".+\.csv$")
    floatPattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+$')
    
    # constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ckptPath = "./resource/RFR-binary.ckpt"    # ckpt file path
        self.csvPath = "./data/data.csv"                # csv file path
        self.singleData = [0, 0, 0, 0, 0, 0, 0]         # single data 
        self.batchData = None                           # batch process data
        self.batchResult = None                         # batch result data
        self.predModel = Predictor(self.ckptPath, self.noticeLabel_1)   # Predictor Object
        self.bind()


    # bind the functions to Buttons
    def bind(self):
        self.pathButton_1.clicked.connect(lambda: self.getFilePath(self.loadModelWeights))
        self.pathButton_2.clicked.connect(lambda: self.getFilePath(self.loadBatchData))
        self.classButton.clicked.connect(lambda: self.singleClassification())
        self.batchButton.clicked.connect(lambda: self.batchClassification())
        self.clearButton_1.clicked.connect(lambda: self.clear)

    # define patterns
    # get model file path
    def loadModelWeights(self):
        # match the regex pattern
        if self.ckptPattern.match(self.ckptPath):
            self.pathEdit_1.setText(self.ckptPath)
            # input path to predModel
            self.predModel.loadCkptFile(self.ckptPath, util.setQTextMsg, self.noticeLabel_1)
            print("model loaded")
            self.pathEdit_1.setReadOnly(True)
            
        else: 
            self.pathEdit_1.setStyleSheet("color: red; font-weight: bold;")
            self.pathEdit_1.setText("FILE PATH ERROR")
            self.pathEdit_1.setStyleSheet("")
            
            self.noticeLabel_1.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: You must choose a ckpt file!")
    
    # get csv file path
    def loadBatchData(self):
        # match the regex pattern
        if self.csvPattern.match(self.ckptPath):
            self.pathEdit_2.setText(self.ckptPath)
            self.noticeLabel_2.setText("csv file loaded successfully!")
            self.loadTable(self.ckptPath)
            print("csv loaded")
            self.pathEdit_2.setReadOnly(True)
        else:
            # show error info.
            self.pathEdit_2.setStyleSheet("color: red; font-weight: bold;")
            self.pathEdit_2.setText("FILE PATH ERROR")
            self.pathEdit_2.setStyleSheet("")

            self.noticeLabel_2.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: You must choose a csv file!")

    # import the file path
    def getFilePath(self, func):  
        # select a ckpt file by QFilDialog
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Choose a file")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        # if file selected
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0]
            self.ckptPath = str(file_path)
            func()
        
        # if cancelled
        else:
            self.noticeLabel_1.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: Choose a file OR Load from default path")
    
    # load the csv file to QTable widget
    def loadTable(self, filename):
        self.batchData = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                self.batchData.append([float(item) for item in row])
            # print(data)
        # tableWidget = QTableWidgetItem
        
        for row_index, row_data in enumerate(self.batchData):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.tableWidget.setItem(row_index, col_index, item)


    def getText(self, textEdit, idx):
        num_str = textEdit.text()
        if self.floatPattern.match(num_str):
            self.singleData[idx] = float(num_str)
            return True
        else:
            return False

    # run the model and get the result
    def singleClassification(self):
        if (self.predModel.ckptWeights == None):
            self.noticeLabel_1.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: No ckpt file loaded!")
            return
        # get values from QText Widget
        ret1 = self.getText(self.lineEdit_1, 0)
        ret2 = self.getText(self.lineEdit_2, 1)
        ret3 = self.getText(self.lineEdit_3, 2)
        ret4 = self.getText(self.lineEdit_4, 3)
        ret5 = self.getText(self.lineEdit_5, 4)
        ret6 = self.getText(self.lineEdit_6, 5)
        ret7 = self.getText(self.lineEdit_7, 6)

        # ensure all the data are set to a valid number
        if (ret1 and ret2 and ret3 and ret4 and ret5 and ret6 and ret7):
            # do predict
            predClass = self.predModel.predict([self.singleData])
            print(f"predClass = {predClass}")
            number = predClass[0]
            print(f"number = {number}")
            if predClass:
                status = "Water-permeable"
            else:
                status = "Completely water-blocking"
            # display result
            self.resultLabel.setText("<span style='color: red; font-weight: bold;'>" + status + "</span>")
        else:
            self.noticeLabel_1.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: Input Error!")

    def batchClassification(self):
        if (self.predModel.ckptWeights == None):
            self.noticeLabel_1.setText("<span style='color: red; font-weight: bold;'>[NOTICE]</span>: No ckpt file loaded!")
            return
        print(f"csvData= {self.batchData}")
        predClass = self.predModel.predict(self.batchData)
        print(predClass)
        if (predClass != )


    def clear(self):
        self.resultLabel.setText("TBD.")
        self.textLabel_1.setText()
        self.textLabel_2.setText()
        self.textLabel_3.setText()
        self.textLabel_4.setText()
        self.textLabel_5.setText()
        self.textLabel_6.setText()
        self.textLabel_7.setText()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()