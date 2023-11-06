from catboost import CatBoostClassifier
import numpy as np

class MultiRFR():
    errorMsgHead = "<span style='color: red; font-weight: bold;'>"
    errorMsgTail = "</span>"
    
    
    def __init__(self):
        super().__init__()
        self.classifier = CatBoostClassifier()
        self.isLoaded = False
        self.value = None


    def loadModel(self, filePath):
        try:
            self.classifier.load_model(filePath)
        except FileNotFoundError:
            return MultiRFR.errorMsgHead + "file not found!" + MultiRFR.errorMsgTail
        except Exception as e:
            print("An error occurred:", str(e))
            return "check terminal for errors!"
        
        self.isLoaded = True  
        return "file loaded successfully."


    def predict(self, weights):
        normalized = MultiRFR.dataPreprocess(weights)

        if isinstance(normalized, str):  # Check if it's a string (error message)
            return MultiRFR.errorMsgHead + normalized + MultiRFR.errorMsgTail
        self.value = self.classifier.predict(normalized)
        return "classification successful."
    

    @staticmethod
    def dataPreprocess(weights):
        reshaped = np.array(weights)
        cols = reshaped.shape[1]
        print(cols)
        if (cols != 5 and cols != 7):
            return "Invalid number of columns in input data."
        # reshape mat
        if (cols == 7):
            reshaped = reshaped[:, [0, 2, 3, 5, 6]]
        # normalization
       
        print(f"reshaped=\n{reshaped}")
        mean = np.mean(reshaped, axis=1).reshape(-1, 1)
        print(f"mean={mean}")
        std = np.std(reshaped, axis=1).reshape(-1, 1)
        print(f"std={std}")
        normalized = (reshaped - mean) / (std + 1e-10)
        print(f"normalized=\n{normalized}")
        return normalized