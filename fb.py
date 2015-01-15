import os
import shutil
from fbreader import *

# origPath is <srcDir>/bla/bla, replace <srcDir> part with your <destDir>
def formatDestDir(origPath, srcDir, destDir):
	newPath = origPath.replace(srcDir, destDir)
	print('New path:', newPath)
	return newPath

def backupFolder(curDir, srcDir, destDir):
	print('From', curDir + ':')
	dirs = os.listdir(curDir)
	for fileName in dirs:
		path = os.path.join(curDir, fileName)
		if os.path.isfile(path):
			copyFile(path, destDir)
		else:
			newDestPath = formatDestDir(path, srcDir, destDir)
			os.makedirs(newDestPath)
			backupFolder(path, srcDir, newDestPath)

def copyFile(filePath, destDir):
	print('Copying', filePath, 'to', destDir, '...')
	shutil.copy(filePath, destDir)


confObj = readConf('fb.conf')
print('Src =', confObj.srcDir)
print('Dest =', confObj.destDirs)

for dest in confObj.destDirs:
	if not os.path.exists(dest):
		os.makedirs(dest)
	backupFolder(confObj.srcDir, confObj.srcDir, dest)
	
print('Folder backup completed.')


