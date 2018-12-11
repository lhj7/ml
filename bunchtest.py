#encoding:utf-8
import sys
import os
import jieba
import pickle 

from sklearn.datasets.base import Bunch          #导入Bunch类

#Bunch类提供一种key,value的对象形式
#target_name:所有分类集名称列表
#label:每个文件的分类标签列表
#filenames:文件路径
#contents:分词后文件词向量形式

bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])
wordbag_path = "G:/python_txt/answer/train_set.bat"          #分词语料Bunch对象持久化文件路径
seg_path = "G:/python_txt/answer/test/"                      #分词后分类语料库路径


def readfile(path):          
		fp = open(path,"rb")
		content = fp.read()
		fp.close()	
		return 	content


catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)                           #将类别信息保存到Bunch对象中
for mydir in catelist:
		class_path = seg_path + mydir + "/"
		file_list = os.listdir(class_path)
		for file_path in file_list:
				fullname = class_path + file_path
				bunch.label.append(mydir)                    #保存当前文件的分类标签
				bunch.filenames.append(fullname)             #保存当前文件的文件路径
				bunch.contents.append(readfile(fullname).strip())           #保存文件词向量

#Bunch对象持久化
file_obj = open(wordbag_path,"wb")
pickle.dump(bunch,file_obj)
file_obj.close()

print "构建文本对象结束!!!"