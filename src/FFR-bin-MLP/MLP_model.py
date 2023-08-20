import torch
import torch.nn as nn
import util

class Predictor:
    def __init__(self, filePath, noticeObj):
        self.model = nn.Sequential(
            nn.Linear(7, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 7),
            nn.ReLU(),
            nn.Linear(7, 2),
        )
        self.ckptWeights = None
        weights, msg = util.tryLoadFile(filePath,
                                        errorMsg="file not found from default path!")
        if (weights != None):
            self.ckptWeights = self.model.load_state_dict(weights)
            util.setQTextMsg(noticeObj, msg, True)
        else:
            noticeObj.setText(msg)
            util.setQTextMsg(noticeObj, msg, False)
    

    def predict(self, inputData, noticeObj):
        self.model.eval()
        predictedClass = None
        try:
            inputTensor = torch.tensor(inputData, dtype=torch.float32)
        # print(inputTensor.shape)
        # print(f"inputTensor = {inputTensor}")
            output = self.model(inputTensor)
            _, predictedClass = torch.max(output, dim=1)
        except RuntimeError:
            noticeObj.setText("<span style='color: red; font-weight: bold;'>Check your input data format</span>")
        return predictedClass
    
    
    def loadCkptFile(self, filePath, callback, noticeObj):
        util.tryLoadFile("")
        weights, msg = util.tryLoadFile(filePath)
        if (weights != None):
            callback(noticeObj, msg, True)
            self.ckptWeights = self.model.load_state_dict(weights)
        else:
            callback(noticeObj, msg, False)

        
        # print(checkPoint)
        


