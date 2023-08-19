import torch
import torch.nn as nn
import util

class Predictor:
    def __init__(self, filePath, textObj):
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
            util.setQTextMsg(textObj, msg, True)
        else:
            textObj.setText(msg)
            util.setQTextMsg(textObj, msg, False)
    

    def predict(self, inputData):
        self.model.eval()
        try:
            inputTensor = torch.tensor(inputData, dtype=torch.float32)
        # print(inputTensor.shape)
        # print(f"inputTensor = {inputTensor}")
            output = self.model(inputTensor)
            _, predictedClass = torch.max(output, dim=1)
        except RuntimeError:
            
        return predictedClass
    
    
    def loadCkptFile(self, filePath, callback, textObj):
        util.tryLoadFile("")
        weights, msg = util.tryLoadFile(filePath)
        if (weights != None):
            callback(textObj, msg, True)
            self.ckptWeights = self.model.load_state_dict(weights)
        else:
            callback(textObj, msg, False)

        
        # print(checkPoint)
        


