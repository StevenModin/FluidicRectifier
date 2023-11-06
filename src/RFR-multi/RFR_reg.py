# encoding == utf-8
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem
from Ui_toolkit import Ui_Form
from RFR_multiple_model import MultiRFR
import re
import csv


class MyWindow(Ui_Form, QWidget):
    # static variables
    modelPattern = re.compile(r".+\.cbm$")
    csvPattern = re.compile(r".+\.csv$")
    floatPattern = re.compile(r'^[-+]?[0-9]*\.?[0-9]+$')

    errorMsgHead = "<span style='color: red; font-weight: bold;'>"
    errorMsgTail = "</span>"
    
    # constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modelPath = "./resource/catboost_model.cbm"     # weight file path
        self.singleData = [0, 0, 0, 0, 0]           # single data
        self.multiModel = MultiRFR()                # Predictor Object
        # auto load model file
        notice = self.multiModel.loadModel(self.modelPath)
        self.noticeLabel_1.setText(notice)
        self.pathEdit_1.setText("load from default path...")
        self.bind()


    # bind the functions to Buttons
    def bind(self):
        self.pathButton_1.clicked.connect(lambda: self.getFilePath(self.loadModel))
        self.pathButton_2.clicked.connect(lambda: self.getFilePath(self.loadBatchData))
        self.classButton.clicked.connect(lambda: self.singleClassification())
        self.clearButton_1.clicked.connect(lambda: self.clear())
        self.batchButton.clicked.connect(lambda: self.batchClassification())
        self.saveButton.clicked.connect(lambda: self.saveFile(0))
        self.saveToButton.clicked.connect(lambda: self.saveFile(1))
        self.clearButton_2.clicked.connect(lambda: self.clearAll())
        
    # define patterns
    # get model file path
    def loadModel(self):
        # match the regex pattern
        if self.modelPattern.match(self.modelPath):
            self.pathEdit_1.setText(self.modelPath)
            # cal regModel method to load the model by path
            resMsg = self.multiModel.loadModel(self.modelPath)
            self.noticeLabel_1.setText(resMsg)
            print("model loaded")
            self.pathEdit_1.setReadOnly(True)
            
        else: 
            self.pathEdit_1.setStyleSheet("color: red; font-weight: bold;")
            self.pathEdit_1.setText("FILE PATH ERROR")
            self.pathEdit_1.setStyleSheet("")
            
            self.noticeLabel_1.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": You must choose a cbm file!")
    
    # get csv file path
    def loadBatchData(self):
        # match the regex pattern
        if self.csvPattern.match(self.modelPath):
            self.pathEdit_2.setText(self.modelPath)
            self.noticeLabel_2.setText("csv file loaded successfully!")
            self.loadTable(self.modelPath)
            print("csv loaded")
            self.pathEdit_2.setReadOnly(True)
        else:
            # show error info.
            self.pathEdit_2.setStyleSheet("color: red; font-weight: bold;")
            self.pathEdit_2.setText("FILE PATH ERROR")
            self.pathEdit_2.setStyleSheet("")

            self.noticeLabel_2.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": You must choose a csv file!")

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
            self.modelPath = str(file_path)
            func()
        
        # if cancelled
        else:
            self.noticeLabel_1.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": Choose a file")
    
    # load the csv file to QTable widget
    def loadTable(self, filename):
        self.batchData = []
        title = []
        with open(filename, 'r', encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)  # Skip the header row
            print(title)
            for row in csv_reader:
                self.batchData.append([float(item) for item in row])
            print("batchData = ")
            print(self.batchData)
        print(title)

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
        if (not self.multiModel.isLoaded):
            self.noticeLabel_1.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": No cbm file loaded!")
            return
        # get values from QText Widget
        ret1 = self.getText(self.lineEdit_1, 0)
        # ret2 = self.getText(self.lineEdit_2, 1)
        ret3 = self.getText(self.lineEdit_3, 1)
        ret4 = self.getText(self.lineEdit_4, 2)
        # ret5 = self.getText(self.lineEdit_5, 4)
        ret6 = self.getText(self.lineEdit_6, 3)
        ret7 = self.getText(self.lineEdit_7, 4)

        # ensure all the data are set to a valid number
        if (ret1 and ret3 and ret4 and ret6 and ret7):
            # do predict
            resMsg = self.multiModel.predict([self.singleData])

            # display result
            print(f"value={self.multiModel.value[0][0]}")
            self.resultLabel.setText(self.multiModel.value[0][0])

            self.noticeLabel_1.setText(resMsg)
        else:
            self.noticeLabel_1.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": Input Error!")

    def batchClassification(self):
        if (self.multiModel.isLoaded == None):
            self.noticeLabel_1.setText(MyWindow.errorMsgHead + "[NOTICE]" + MyWindow.errorMsgTail + ": No cbm file loaded!")
            return
        batchNotice = self.multiModel.predict(self.batchData)
        print(f"value={self.multiModel.value}")
        self.noticeLabel_2.setText("batch " + batchNotice)
    
    def defaultSavePath(self):
        return "./resource/RFR-multi-pred-res.csv"

    def newSavePath(self):
        # Prompt user to select a file path
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV Files (*.csv)")
        selectedFilePath, _ = file_dialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        return selectedFilePath

    def saveFile(self, mode):
        if (self.multiModel.value is None):
            self.noticeLabel_2.setText(MyWindow.errorMsgHead + "No Classification Result" + MyWindow.errorMsgTail)
            return
        
        savePath = None

        if mode == 0:
            savePath = self.defaultSavePath()
        elif mode == 1:
            savePath = self.newSavePath()

        if savePath == None:
            self.noticeLabel_2.setText(MyWindow.errorMsgHead + "File Path Error" + MyWindow.errorMsgTail)
            return

        # Convert tensor to a list of Python integers
        intList = [int(value) for value in self.multiModel.value]

        # Transpose the data to arrange it in a single column
        transposed_data = [[value] for value in intList]

        with open(savePath, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(transposed_data)

        self.noticeLabel_2.setText(f"Data saved to: {savePath}")

    def clear(self):
        self.resultLabel.setText("TBD.")
        self.textLabel_1.setText()
        # self.textLabel_2.setText()
        self.textLabel_3.setText()
        self.textLabel_4.setText()
        # self.textLabel_5.setText()
        self.textLabel_6.setText()
        self.textLabel_7.setText()

    def clearAll(self):
        self.batchData = None
        self.batchResult = None
        self.tableWidget.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()