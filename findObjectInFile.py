#!/bin/python
# -*- coding: utf-8 -*-

# Author: EdwardZhou E-mail: zrfedward@gmail.com
# Date: 2016-10

class findObjectInFile:

	@staticmethod
	def findStringInFile(filePath, strVal):
	'''
	@function: 用于查找字符串是否存在于文件中，若存在，返回字符串所在行数
	@filePath: 文件绝对路径
	@strVal: 字符串内容
	'''
		lineNum = 0
		msg = "There is no result"
		with open(filePath, 'r') as file:
			for line in file.readlines():
				lineNum = lineNum + 1
				if strVal in line.strip():
					msg = "'%s' string in line %d" % (strVal, lineNum)
					break
		print msg

if __name__ == '__main__':
	findObjectInFile.findStringInFile(r"F:\a.txt", "Hello")