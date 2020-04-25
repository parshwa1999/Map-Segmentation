import cv2
import numpy as np

total = 0

for i in range(29):
    original = cv2.imread(str(i) + "GroundTruth.png", 0)
    predicted = cv2.imread(str(i) + "Prediction_Threshold.png", 0)

    original = original.flatten()
    predicted = predicted.flatten()

    original = (original>127)
    predicted = (predicted>127)

    #print(np.unique(predicted))
    #print(np.unique(original))
    print(i)
    
    sum = np.sum((predicted * original)*1 + (np.invert(predicted) * np.invert(original))*1)

    print(sum*100/57600)
    total += sum*100/57600
   
print(total/29)
