import json
import cv2
import numpy as np

filename = "Img0.png"

with open('template.json') as f:
	data = json.load(f)

shapes = data['shapes'][0]
data['shapes'].remove(shapes)
data['shapes'].remove(shapes)

img = cv2.imread(filename[0:len(filename)-4] + '_mask.png', 0)
img[img>127] = 255
img[img<127] = 0
#img = cv2.Canny(img, 30, 200)

contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("Number of Contours found = " + str(len(contours))) 

contours_list=[]
for i in range(len(contours)):
	added_points = shapes
	added_points['points'] = np.squeeze(np.array(contours)[i]).tolist()
	data['shapes'].append(added_points.copy())
	del added_points

data['imagePath'] = filename

with open(filename[0:len(filename)-3]  + 'json', 'w') as json_file:
  json.dump(data, json_file)