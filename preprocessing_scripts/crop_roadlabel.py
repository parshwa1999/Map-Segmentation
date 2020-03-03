import cv2
import numpy as np
import os

def crop_image(x, save_path, save_name):
	image = cv2.imread(x) #data_path
	image = image[110:110+1280, 110:110+1280]

	print(np.shape(image))
	
	count = 0
	for i in range(0, 1280, 256):
			for j in range(0, 1280, 256):
				count+=1
				#print(str(i) + " " + str(j))
				#print(count)
				cv2.imwrite(save_path + save_name[0:len(x)-1-4] + "_"+ str(count) +".png", image[i:i+256,j:j+256])
				#print(save_path + x[0:len(x) - 4] + "_"+ str(count) +".png")



f = open("data_roadlabel.txt", "r")

data_path = "/home/bisag/Desktop/png/roadlabel/"
save_path = "/home/bisag/Desktop/cropped/roadlabel/"
for x in f:
	#print(x[0:len(x)-1-5] + ".png    " + str(os.path.exists("/home/bisag/Desktop/png/road/" + x[0:len(x)-1-5] + ".png")))
	if os.path.exists(save_path + x[0:len(x)-1-4]  + "_1.png"):
		print("Found")
	else:
		try:
			crop_image(data_path + x[0:len(x)-1-4] + ".png", save_path, x[0:len(x)-1-4])
			print("Saved")
			#print(data_path + x[0:len(x)-1-5] + ".png")
		except:
			pass
#x="1.png"





