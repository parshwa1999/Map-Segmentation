"""import os

f = open("data.txt", "r")

for x in f:
	print(x[0:len(x)-1-4] + ".png")
	if os.path.exists("/home/bisag/Desktop/png/roadlabel" + x[0:len(x)-1-4] + ".png" ):
		print("Found")
	else:
		os.system("gdal_translate -of PNG -b 1 /home/bisag/Desktop/tiff/roadlabel/" + x[0:len(x)-1-4] + ".tif " + x[0:len(x)-1-4] + ".png ")
		#print("gdal_translate -of PNG -b 1 /home/bisag/Desktop/tiff/roadlabel/" + x[0:len(x)-1-4] + ".tif " + x[0:len(x)-1-4] + ".png ")"""

import h5py
import cv2
import numpy as np
import glob

x = "1.png"

#image = cv2.imread(x)

images = [cv2.imread(file) for file in glob.glob("/home/bisag/Desktop/png/test/*.png")]

print(np.shape(images))

"""
###Write
with h5py.File('test.h5', 'w') as hf:
    hf.create_dataset("test",  data=image)
"""

"""
###Read
with h5py.File('test.h5', 'r') as hf:
    image = hf['test'][:]
"""

#cv2.imshow("test", image)
#cv2.waitKey(3000)
