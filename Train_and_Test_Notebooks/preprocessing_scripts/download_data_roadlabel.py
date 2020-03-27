import os

url="https://www.cs.toronto.edu/~vmnih/data/mass_roads/train/map/"

f = open("data1.txt", "r")

for x in f:
	print(x[0:len(x)-1])
	if os.path.exists("/home/bisag/Desktop/Labels/" + x[0:len(x)-1]):
		print("Found")
	else:
		print("Not Found")	
		os.system("wget " + url + x)

