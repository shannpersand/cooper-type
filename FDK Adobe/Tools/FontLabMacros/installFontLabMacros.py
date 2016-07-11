#!/bin/env python

__copyright__ =  """
Copyright 2015-2016 Adobe Systems Incorporated (http://www.adobe.com/). All Rights Reserved.
This software is licensed as OpenSource, under the Apache License, Version 2.0. This license is available at: http://opensource.org/licenses/Apache-2.0. */
"""

__doc__ = """
v 2.0 Apr 11 2016

Copies the folders under the parent directory of this script file
to the appropriate place under FontLab program's Macros directory.
"""

import sys
import re
import os
import shutil
import traceback

class InstallError(IOError):
	pass

import stat
kPermissions = stat.S_IWRITE | stat.S_IREAD | stat.S_IRGRP | stat.S_IWGRP | stat.S_IRUSR | stat.S_IWUSR

def copyFile(srcPath, dstPath):
		if os.path.isfile(srcPath):
			try:
				shutil.copy(srcPath, dstPath)
				shutil.copystat(srcPath, dstPath)
				os.chmod(dstPath, kPermissions)
			except IOError:
				print "Failed to copy file %s to %s." % (srcPath, dstPath)
				print traceback.format_exception_only(sys.exc_type, sys.exc_value)[-1]
				print "Quitting - not all files were copied."
				raise InstallError
			print "Copied %s\n    to %s\n" % (srcPath, dstPath)
		else:
			print "Failed to find src file '%s'." % (srcPath)


def copyDir(srcDirPath, destDirPath):
	if not os.path.exists(destDirPath):
		os.mkdir(destDirPath)

	fileList = os.listdir(srcDirPath)
	for fileName in fileList:
		srcPath = os.path.join(srcDirPath, fileName)
		if os.path.isfile(srcPath):
			name,ext = os.path.splitext(fileName)
			if not ext in [".so", ".pyd", ".py"]:
				continue
			dstPath = os.path.join(destDirPath, fileName)
			copyFile(srcPath, dstPath)
		elif os.path.isdir(srcPath):
			newDestDirPath = os.path.join(destDirPath, fileName)
			copyDir(srcPath, newDestDirPath)
		else:
			print "Say what? this file is neither a dir nor a regular file:", srcPath

def run():
	# define where we will copy things
	if len(sys.argv) != 2:
		print "You must provide the path to FontLab's Macros folder."
		print "An example for Mac OSX:"
		print "   python installFontLabMacros.py /Users/<your Mac user name>/Library/Application\ Support/FontLab/Studio\ 5/Macros"
		return
	destBasePath = sys.argv[1]
	if not os.path.isdir(destBasePath):
		print "The path you supplied does not exist or is not a directory. Try again."
		return

	# get the path to the folder that contains this script
	srcBasePath = os.path.dirname(os.path.abspath(__file__))

	# copy all folders and their contents to FontLab's Macros folder.
	# the Modules folder requires special handling
	dirList = os.listdir(srcBasePath)
	for dirName in dirList:
		if dirName.startswith('.'):
			continue
		srcDirPath = os.path.join(srcBasePath, dirName)
		if not os.path.isdir(srcDirPath):
			continue
		if dirName == "Modules":
			destDirPath = os.path.join(destBasePath, "System", dirName)
		else:
			destDirPath = os.path.join(destBasePath, dirName)
		copyDir(srcDirPath, destDirPath)


if __name__ == "__main__":
	try:
		run()
	except InstallError:
		pass


