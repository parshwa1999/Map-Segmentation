import os

f = open("data.txt", "r")

for x in f:
	print(x[0:len(x)-1-4] + ".png")
	if os.path.exists("/home/bisag/Desktop/png/roadlabel" + x[0:len(x)-1-4] + ".png" ):
		print("Found")
	else:
		os.system("gdal_translate -of PNG -b 1 /home/bisag/Desktop/tiff/roadlabel/" + x[0:len(x)-1-4] + ".tif " + x[0:len(x)-1-4] + ".png ")
		#print("gdal_translate -of PNG -b 1 /home/bisag/Desktop/tiff/roadlabel/" + x[0:len(x)-1-4] + ".tif " + x[0:len(x)-1-4] + ".png ")
