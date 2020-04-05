from keras import backend as K
import keras.losses, keras.metrics
import tensorflow as tf
import cv2
import numpy as np

#Source: https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2

def load_Unet(model_path, weights_path):

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
    model = load_model(model_path + '/UnetModel.h5', custom_objects={'loss': soft_dice_loss})
    model.load_weights(weights_path + '/Final_unet_road_weights.h5')
    graph = tf.get_default_graph()

    return model, graph

def save_road_image(model, graph, read_path, write_path):
    #weights_path = "/home/parshwa/Desktop/Map-Segmentation/Map-Segmentation/Train_and_Test_Notebooks/weights/Massachusetts_Roads_and_Building_Dataset/Final_unet_road_weights.h5"
    #model.load_weights(weights_path)

    image = []
    image.append(cv2.imread (read_path))
    image = np.array(image)
    image = np.array(image)

    """
    from django.conf import settings
    import os

    model = load_Unet(os.path.join(settings.BASE_DIR, "static", "models", "Massachusetts_Roads_and_Building_Dataset"),
                    os.path.join(settings.BASE_DIR, "static", "weights", "Massachusetts_Roads_and_Building_Dataset"))
    """

    with graph.as_default():
        output = model.predict(image, verbose=1)*255

    cv2.imwrite(write_path, np.squeeze(output[0]))


def save_road_CSV(image_path, file_path):
    output = cv2.imread (image_path)

    output[output>127] = 255
    output[output<127] = 0
    output = np.uint8(output)

    edge = np.expand_dims(cv2.Canny(output, 30, 200), -1)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    f = open(file_path,"w+")
    f.write("id,geom\n")
    for i in range(len(contours)):
        contours[i] = np.squeeze(contours[i], axis = 1)
        f.write(str(i) + ",\"POLYGON ((")
        for j in contours[i]:
            f.write(str(j[0]) + " " + str(j[1]*-1) + ", ")
        f.write(str(contours[i][0][0]) + " " + str(contours[i][0][1]*-1) + "))\"\n")

    f.close()
