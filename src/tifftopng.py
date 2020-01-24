import os

f = open("data.txt", "r")

for x in f:
	#print(x[0:len(x)-1-5] + ".png    " + str(os.path.exists("/home/bisag/Desktop/png/road/" + x[0:len(x)-1-5] + ".png")))
	if os.path.exists("/home/bisag/Desktop/png/road/" + x[0:len(x)-1-5] + ".png"):
		print("Found")
	else:
		os.system("gdal_translate -of PNG -b 1 -b 2 -b 3 /home/bisag/Desktop/tiff/road/" + x[0:len(x)-1-5] + ".tiff " + x[0:len(x)-1-5] + ".png ")
		#print("gdal_translate -of PNG -b 1 -b 2 -b 3 /home/bisag/Desktop/tiff/road/" + x[0:len(x)-1-5] + ".tiff " + x[0:len(x)-1-5] + ".png ")
