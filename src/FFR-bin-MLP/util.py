import torch

# callback function, to set QText success/failure msg
# @var textObj : get QTextEdit object to set text
# @var msg : msg to be set to the QTextEdit
# @var status : True for succes, False for error and show red warning msg
def setQTextMsg(textObj, msg, status):
    if (status):
        textObj.setText(msg)
    else:
        textObj.setText("<span style='color: red; font-weight: bold;'>" + msg + "</span>")

# try except to load ckpt file
def tryLoadFile(filePath, 
                sucessMsg="file loaded successfully.", 
                errorMsg="file not found!"):
    checkPoint = None
    msg = ""
    try:
        checkPoint = torch.load(filePath)
        msg = sucessMsg
    except FileNotFoundError:
        msg = errorMsg
    except Exception as e:
        print("An error occurred:", str(e))
    return checkPoint, msg