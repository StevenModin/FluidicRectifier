# encoding == utf-8
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem
from Ui_toolkit import Ui_Form
from MLP_model import Predictor
import os
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
        self.errorMsgHead = "<span style='color: red; font-weight: bold;'>"
        self.errorMsgTail = "</span>"
        self.ckptPath = "./resource/RFR-bin.ckpt"   # ckpt file path
        self.singleData = [0, 0, 0, 0, 0, 0, 0]     # single data 
        self.batchData = []                         # batch process data
        self.batchResult = None                     # batch result data
        self.predModel = Predictor(self.ckptPath, self.noticeLabel_1)   # Predictor Object
        self.bind()


    # bind the functions to Buttons
    def bind(self):
        self.pathButton_1.clicked.connect(lambda: self.getFilePath(self.loadModelWeights))
        self.pathButton_2.clicked.connect(lambda: self.getFilePath(self.loadBatchData))
        self.classButton.clicked.connect(lambda: self.singleClassification())
        self.clearButton_1.clicked.connect(lambda: self.clear)
        self.batchButton.clicked.connect(lambda: self.batchClassification())
        self.saveButton.clicked.connect(lambda: self.saveFile(0))
        self.saveToButton.clicked.connect(lambda: self.saveFile(1))
        
    # define patterns
    # get model file path
    def loadModelWeights(self):
        # match the regex pattern
        if self.ckptPattern.match(self.ckptPath):
            self.pathEdit_1.setText(self.ckptPath)
            # reset predModel to None
            self.predModel.ckptWeights = None
            # cal predModel method to load the model by path
            self.predModel.loadCkptFile(self.ckptPath, util.setQTextMsg, self.noticeLabel_1)
            print("model loaded")
            self.pathEdit_1.setReadOnly(True)
            
        else: 
            self.pathEdit_1.setStyleSheet("color: red; font-weight: bold;")
            self.pathEdit_1.setText("FILE PATH ERROR")
            self.pathEdit_1.setStyleSheet("")
            
            self.noticeLabel_1.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": You must choose a ckpt file!")
    
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

            self.noticeLabel_2.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": You must choose a csv file!")

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
            self.noticeLabel_1.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": Choose a file OR Load from default path")
    
    # load the csv file to QTable widget
    def loadTable(self, filename):
        self.batchData = []
        title = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)  # Skip the header row
            print(title)
            for row in csv_reader:
                self.batchData.append([float(item) for item in row])
            print("batchData = ")
            print(self.batchData)

        rows = len(self.batchData)
        cols = len(self.batchData[0])
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(self.batchData[row][col]))
                self.tableWidget.setItem(row, col, item)
        self.tableWidget.setHorizontalHeaderLabels(title)

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
            self.noticeLabel_1.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": No ckpt file loaded!")
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
            predClass = self.predModel.predict([self.singleData], self.noticeLabel_1)
            print(f"predClass = {predClass}")
            number = predClass[0]
            print(f"number = {number}")
            if predClass:
                status = "Water-permeable"
            else:
                status = "Completely water-blocking"
            # display result
            self.resultLabel.setText(self.errorMsgHead + status + self.errorMsgTail)
        else:
            self.noticeLabel_1.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": Input Error!")

    def batchClassification(self):
        if (self.predModel.ckptWeights == None):
            self.noticeLabel_1.setText(self.errorMsgHead + "[NOTICE]" + self.errorMsgTail + ": No ckpt file loaded!")
            return
        print(f"csvData= {self.batchData}")
        self.batchResult = self.predModel.predict(self.batchData, self.noticeLabel_2)
        self.noticeLabel_2.setText("Batch prediction succeed!")
    
    def defaultSavePath(self):
        return "./resource/RFR-bin-pred-res.csv"

    def selectSavePath(self):
        # Prompt user to select a file path
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        if file_dialog.exec_():
            selectedFilePath = file_dialog.selectedFiles()[0]
        return selectedFilePath

    def saveFile(self, mode):
        if (self.batchResult == None):
            self.noticeLabel_2.setText(self.errorMsgHead + "No predition Result" + self.errorMsgTail)
            return
        
        savePath = None

        if mode == 0:
            savePath = self.defaultSavePath()
        elif mode == 1:
            savePath = self.selectSavePath()

        if savePath == None:
            self.noticeLabel_2.setText(self.errorMsgHead + "File Path Error" + self.errorMsgTail)
            return

        # Convert int64 tensor to a list of Python integers
        int_list = [int(value) for value in self.batchResult]

        # Transpose the data to arrange it in a single column
        transposed_data = [[value] for value in int_list]

        with open(savePath, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(transposed_data)

        self.noticeLabel_2.setText(f"Data saved to: {savePath}")

         # Check if the file already exists using Python's os.path.exists
        if os.path.exists(savePath):
            confirm_msg_box = QMessageBox(self)
            confirm_msg_box.setIcon(QMessageBox.Question)
            confirm_msg_box.setWindowTitle("Confirm Overwrite")
            confirm_msg_box.setText(f"The file '{savePath}' already exists. Do you want to overwrite it?")
            confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_response = confirm_msg_box.exec_()

            if confirm_response == QMessageBox.No:
                return

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