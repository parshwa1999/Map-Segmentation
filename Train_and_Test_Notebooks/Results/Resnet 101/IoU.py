import cv2
import numpy as np

total = 0

for i in range(29):
    original = cv2.imread(str(i) + "GroundTruth.png", 0)
    predicted = cv2.imread(str(i) + "Prediction_Threshold.png", 0)
    #print(np.shape(original))

    original = original.flatten()
    predicted = predicted.flatten()

    original = (original>127)	
    predicted = (predicted>127)

    #print(np.unique(predicted))
    #print(np.unique(original))
    print(i)
    
    if np.sum(np.invert(original)) != 0:
        sum0 = np.sum((np.invert(predicted) * np.invert(original))*1) / np.sum(np.invert(original))
    else:
        sum0 = 1
    
    if np.sum(original) != 0:
        sum1 = np.sum((predicted * original)*1) / np.sum(original)
    else:
        sum1 = 1
    
    print("SUM: " + str( np.sum(original)))
    #print("SUM: " + str( np.sum(np.invert(original))))
    #print("MUL	: " + str(np.sum(np.invert(original) * original)))
    IoU = ((sum0 + sum1) / 2) * 100
    print("IoU: " + str(sum0) + "   " + str(sum1) + "    " + str(IoU))


    total += IoU
   
print(total/29)
