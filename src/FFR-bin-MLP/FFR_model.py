import torch
import torch.nn as nn
import util

class RegFFR(nn.Module):
    def __init__(self, filePath, noticeObj):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(7, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 7),
            nn.ReLU(),
            nn.Linear(7, 1),
            nn.ReLU()
        )
        self.weights = None
        weights, msg = util.tryLoadFile(filePath,
                                        errorMsg="file not found from default path!")
        if (weights != None):
            self.weights = self.load_state_dict(weights)
            util.setQTextMsg(noticeObj, msg, True)
        else:
            noticeObj.setText(msg)
            util.setQTextMsg(noticeObj, msg, False)

    def forward(self, inputData, noticeObj):
        self.eval()
        try:
            matrix = torch.tensor(inputData, dtype=torch.float32)
            # normalization
            # mu = matrix.mean(dim=1)
            # sigma = matrix.std(dim=1)
            # matrix = (matrix - mu.unsqueeze(1)) / sigma.unsqueeze(1)
            # print("matrix normal =\n", matrix)

            y_reg= self.model(matrix)
            # print(y_reg)
        except RuntimeError:
            noticeObj.setText("<span style='color: red; font-weight: bold;'>Check your input data format</span>")
        return y_reg
    

    def loadFile(self, filePath, callback, noticeObj):
        util.tryLoadFile("")
        weights, msg = util.tryLoadFile(filePath)
        if (weights != None):
            callback(noticeObj, msg, True)
            self.weights = self.load_state_dict(weights)
        else:
            callback(noticeObj, msg, False)

        