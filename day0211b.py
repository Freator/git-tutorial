# -*- coding:utf-8 -*-
# 读取word数据
import docx
def readDocx(docName):
	fullText = []
	doc = docx.Document(docName)
	# 读取全部内容
	paras = doc.paragraphs
	# 将每行数据存入列表
	for p in paras:
		fullText.append(p.text)
		# 将列表数据装换成字符串
	return '\n'.join(fullText)
print(readDocx('test.docx'))