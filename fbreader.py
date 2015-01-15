class fbConfig():
	def __init__(self, srcDir, destDirs):
		self.srcDir = srcDir
		self.destDirs = destDirs

def readConf(filePath):
	f = open(filePath, 'r')
	srcDir, destDirs = "", []
	for line in f:
		pair = line.split('=')
		if pair[0].strip() == 'fb.sourceFolder':
			srcDir = pair[1].strip()
		elif pair[0].strip() == 'fb.destinationFolders':

			destDirs = pair[1].strip().split(",")
	f.close()
	return fbConfig(srcDir, destDirs)


