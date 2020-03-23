import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

data = [cv2.imread(file) for file in glob.glob("test/*.png")]

mirror_data = []
flip90_data = []
flip180_data = []
flip270_data = []

for i in range(np.shape(data)[0]):
	mirror_data.append(np.fliplr(data[i]))
	flip90_data.append(np.rot90(data[i]))
	flip180_data.append(np.rot90(flip90_data[i]))
	flip270_data.append(np.rot90(flip180_data[i]))

"""
image = data[3]
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate(image, angle)
	cv2.imshow("Rotated (Problematic)", rotated)
	cv2.waitKey(0)
"""

plt.imshow(mirror_data[0])
plt.show()

plt.imshow(data[0])
plt.show()

plt.imshow(flip180_data[0])
plt.show()