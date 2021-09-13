import os
print(os.path.exists('../train.txt'))
with open('../train.txt', 'r') as f:
	for line in f.readlines():
		line = "/".join(line.split('/')[-4:]).strip()
		if os.path.exists("../" + line):
			os.system("cp ../" + line + " ../VOC/images/train")
		line = line.replace('JPEGImages', 'labels').replace('jpg', 'txt')
		if os.path.exists("../" + line):
			os.system("cp ../" + line + " ../VOC/labels/train")
print(os.path.exists('../2007_test.txt'))
with open('../2007_test.txt', 'r') as f:
	for line in f.readlines():
		line = "/".join(line.split('/')[-4:]).strip()
		if os.path.exists("../" + line):
			os.system("cp ../" + line + " ../VOC/images/val")
		line = line.replace('JPEGImages', 'labels').replace('jpg', 'txt')
		if os.path.exists("../" + line):
			os.system("cp ../" + line + " ../VOC/labels/val")