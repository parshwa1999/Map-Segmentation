import cv2
import numpy as np

image_path = "/home/bisag/Desktop/png/road/"

x="1.png"



def crop_image(x, save_path):
	image = cv2.imread(x) #data_path
	image = image[110:110+1280, 110:110+1280]

	print(np.shape(image))
	
	count = 0
	for i in range(0, 1280, 256):
			for j in range(0, 1280, 256):
				count+=1
				print(str(i) + " " + str(j))
				print(count)
				cv2.imwrite(save_path + x[0:len(x) - 4] + "_"+ str(count) +".png", image[i:i+256,j:j+256])
				print(save_path + x[0:len(x) - 4] + "_"+ str(count) +".png")

crop_image(x, "/home/bisag/Desktop/cropped/road/")

