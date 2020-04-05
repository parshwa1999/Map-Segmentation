#Source: https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2

from keras import backend as K
import keras.losses, keras.metrics
import cv2
import numpy as np

def iou_coef(y_true, y_pred, smooth=1):
  intersection = K.sum(K.abs(y_true * y_pred), axis=[1,2,3])
  union = K.sum(y_true,[1,2,3])+K.sum(y_pred,[1,2,3])-intersection
  iou = K.mean((intersection + smooth) / (union + smooth), axis=0)
  return iou

def dice_coef(y_true, y_pred, smooth = 1):
  y_true_f = K.flatten(y_true)
  y_pred_f = K.flatten(y_pred)
  intersection = K.sum(y_true_f * y_pred_f)
  return (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)

def soft_dice_loss(y_true, y_pred):
  return 1-dice_coef(y_true, y_pred)

keras.losses.soft_dice_loss = soft_dice_loss
keras.metrics.iou_coef = iou_coef

from keras.models import load_model
model = load_model('/home/parshwa/Desktop/Map-Segmentation/Map-Segmentation/Train_and_Test_Notebooks/models/Massachusetts_Roads_and_Building_Dataset/UnetModel.h5',
                   custom_objects={'loss': soft_dice_loss})

model.load_weights("/home/parshwa/Desktop/Map-Segmentation/Map-Segmentation/Train_and_Test_Notebooks/weights/Massachusetts_Roads_and_Building_Dataset/Final_unet_road_weights.h5")

image = []
image.append(cv2.imread ("Img0.png"))
image = np.array(image)

output = np.squeeze(model.predict(image, verbose=1)*255)

cv2.imwrite("output.png", output)

output[output>127] = 255
output[output<127] = 0
output = np.uint8(output)

edge = np.expand_dims(cv2.Canny(output, 30, 200), -1)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of Contours found = " + str(len(contours))) 

filename = "Road1.csv"
f = open(filename,"w+")
f.write("id,geom\n")
for i in range(len(contours)):
  contours[i] = np.squeeze(contours[i], axis = 1)
  f.write(str(i) + ",\"POLYGON ((")
  for j in contours[i]:
    f.write(str(j[0]) + " " + str(j[1]*-1) + ", ")
  f.write(str(contours[i][0][0]) + " " + str(contours[i][0][1]*-1) + "))\"\n")

f.close()




