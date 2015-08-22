import random
import os, sys
import re

path = "D:/Python/Programs/work"
extension = [".txt", ".dat", ".src"]

def createNewFolder():
	os.mkdir(path, 0777)
	pass

def createNewFiles():
	os.chdir(path)

	for x in xrange(30):
		name = '%d' %(random.randint(10,50)) + random.choice(extension)
		file = open(name, "w").close()
		pass
	pass

def addNewFiles():
	os.chdir(path)
	work = os.listdir(path)

	for x in xrange(30):
		name = '%d' %(random.randint(10,50)) + random.choice(extension)
		if work.count(name) == 0:
			file = open(name, "w")
			file.write("new")
			file.close
		else:
			file = open(name, "w")
			file.write("old")
			file.close
		pass
	pass

def searchTxtFiles():
	os.chdir(path)
	result = []
	work = os.listdir(path)

	for x in xrange(len(work)):
		y = re.match(r"1..txt", work[x])
		if y != None :
			result.append(y.group(0));
		pass
	return result
	pass

def renameTxtToSrc(result):
	os.chdir(path)
	work = os.listdir(path)

	for x in xrange(len(result)):
		name = result[x][0:2] + ".src"
		if work.count(name) == 0:
			os.rename(result[x], name)
		else:
			os.remove(path + "/" + name)
			os.rename(result[x], name)
		pass
	pass

def createDictionary():
	listOld = []
	listNew = []
	listEmpty = []
	dictionary = {"old" : listOld, "new" : listNew, "" : listEmpty}
	return dictionary
	pass

def destribution(dictionary):
	os.chdir(path)
	work = os.listdir(path)

	for x in xrange(len(work)):
		y = work[x]
		file = open(y, "r")
		z = file.read()
		if z=="old":
			dictionary["old"].append(y)
			pass
		elif z=="new":
			dictionary["new"].append(y)
			pass
		elif z=="":
			dictionary[""].append(y)
			pass
		pass
	print dictionary.get("old")
	pass

reateNewFolder()
createNewFiles()
addNewFiles()
renameTxtToSrc(searchTxtFiles())
destribution(createDictionary())

print "You really crazy! This program is working!!! Bit I'm not sure, that it works as we need... But it works!"
