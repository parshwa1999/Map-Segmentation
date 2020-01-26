import os

path = "roadlabel/"

listofimages = os.listdir("clean_road/")

#print(listofimages)

for i in listofimages:
	if os.path.exists(path + i) and not os.path.exists("clean_roadlabel/" + i):
		os.system("cp -v " + path + i + " clean_roadlabel/" + i)
		#print("cp " + path + i + " clean_road/" + i)
	else:
		print("Not Found " + i)


