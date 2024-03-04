# Fluidic Rectifier

## RFR Tool

This is a simple tool for processing single and batch data using a pre-trained model. The tool has a graphical user interface (GUI) built using PySide6, a Python binding for the Qt framework.

### Features

- **Single Group Data Processing:** Load a pre-trained model file (torch .ckpt file) and input a single set of data for classification.
- **Batch Processing:** Load a CSV file containing multiple sets of data for batch processing.
- **User Interface:** Intuitive graphical interface for easy interaction.
- **Model Architecture:** The tool uses a neural network model with a specific architecture defined in `model.py`.
- **Error Handling:** Alerts the user with warning messages in case of incorrect file paths or input errors.

### Requirements

- Python 3.x
- PySide6
- torch

### Usage

1. Run the tool by executing `main.py`.
2. Load a pre-trained model file (ckpt) using the "Load Model" button or load a CSV file for batch processing using the "Load CSV" button.
3. Input data for single group processing in the corresponding fields.
4. Click the "Classify" button to get the classification result for single group data.
5. For batch processing, load a CSV file and click the "Process" button to analyze all data in the file.
6. Results are displayed in the GUI, and messages indicate the status of file loading and processing.

### File Structure

- **main.py:** Main script containing the GUI setup and user interaction logic.
- **model.py:** Defines the neural network model and a `Predictor` class for loading ckpt files.
- **toolkit.ui:** UI file generate from Qt Designer, defining the layout and elements of the GUI.
- **Ui_toolkit.py:** python file compile by pyside6-uic from toolkit.ui
- **util.py:** Utility functions, including a callback for setting QText success/failure messages and loading ckpt files with error handling.

### Note

This tool is designed for educational purposes and may require additional modifications to suit specific use cases.

