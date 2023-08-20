# import sys
# import torch
# from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
# import csv
# import os

# app = QApplication(sys.argv)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         layout = QVBoxLayout()

#         self.text_edit = QTextEdit()
#         layout.addWidget(self.text_edit)

#         self.save_button = QPushButton("Save Column to CSV")
#         self.save_button.clicked.connect(self.save_to_csv)
#         layout.addWidget(self.save_button)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def save_to_csv(self):
#         # Create a sample torch matrix (replace this with your actual matrix)
#         torch_matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])

#         # Select a specific column to save (e.g., the first column)
#         column_to_save = torch_matrix[:, 0]

#         # Prompt user to select a file path
#         file_dialog = QFileDialog(self)
#         file_dialog.setFileMode(QFileDialog.AnyFile)
#         file_dialog.setNameFilter("CSV Files (*.csv)")
#         if file_dialog.exec_():
#             selected_file_path = file_dialog.selectedFiles()[0]

#             # Check if the file already exists using Python's os.path.exists
#             if os.path.exists(selected_file_path):
#                 confirm_msg_box = QMessageBox(self)
#                 confirm_msg_box.setIcon(QMessageBox.Question)
#                 confirm_msg_box.setWindowTitle("Confirm Overwrite")
#                 confirm_msg_box.setText(f"The file '{selected_file_path}' already exists. Do you want to overwrite it?")
#                 confirm_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#                 confirm_response = confirm_msg_box.exec_()

#                 if confirm_response == QMessageBox.No:
#                     return

#             # Convert the column to a Python list and write it to CSV
#             column_list = column_to_save.tolist()
#             with open(selected_file_path, 'w', newline='') as file:
#                 csv_writer = csv.writer(file)
#                 csv_writer.writerows([[value] for value in column_list])  # Each value is a list containing a single element

#             self.text_edit.setPlainText(f"Column saved to: {selected_file_path}")

# if __name__ == "__main__":
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())
