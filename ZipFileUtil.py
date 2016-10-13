#!/bin/python
# -*- coding: utf-8 -*-

# Function:
# Author: ZhouRuoFan
# Date: 2016-06

import os, zipfile

class ZipFileUtil:

	@staticmethod
	def fileToZip(sourceFilePath, zipFilePath, fileName):
		'''
		@Fuction: 将存放在sourceFilePath目录下的源文件,打包成fileName名称的ZIP文件,并存放到zipFilePath
		args:
		sourceFilePath 待压缩的文件路径
		zipFilePath	压缩后存放路径
		fileName	   压缩后文件的名称
		return: flag
		'''
		flag = False

		if not os.path.exists(sourceFilePath):
			print(u">>>>>> 待压缩的文件目录：" + sourceFilePath + u" 不存在. <<<<<<")
		else:
			try:
				if os.path.isfile(os.path.join(zipFilePath, fileName)):
					print(">>>>>> " + zipFilePath + u" 目录下存在名字为：" + fileName + u" 打包文件. <<<<<<")

				sourceFiles = os.listdir(sourceFilePath)
				if sourceFiles == None or len(sourceFiles) < 1:
					print(u">>>>>> 待压缩的文件目录：" + sourceFilePath + u" 里面不存在文件,无需压缩. <<<<<<")
				else:
					zipFileFullDir = os.path.join(zipFilePath, fileName)
					print zipFileFullDir
					f = zipfile.ZipFile(zipFileFullDir, 'w' ,zipfile.ZIP_DEFLATED)
					for sourceFile in sourceFiles:
						sourceFileFullDir = os.path.join(sourceFilePath, sourceFile)
						f.write(sourceFileFullDir)
					f.close()
			except Exception, e:
				print str(e)

if __name__ == '__main__':
	ZipFileUtil.fileToZip("123", "E:\TestZip", "zipFiles.zip")