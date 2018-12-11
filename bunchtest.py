#encoding:utf-8
import sys
import os
import jieba
import pickle 

from sklearn.datasets.base import Bunch          #����Bunch��

#Bunch���ṩһ��key,value�Ķ�����ʽ
#target_name:���з��༯�����б�
#label:ÿ���ļ��ķ����ǩ�б�
#filenames:�ļ�·��
#contents:�ִʺ��ļ���������ʽ

bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])
wordbag_path = "G:/python_txt/answer/train_set.bat"          #�ִ�����Bunch����־û��ļ�·��
seg_path = "G:/python_txt/answer/test/"                      #�ִʺ�������Ͽ�·��


def readfile(path):          
		fp = open(path,"rb")
		content = fp.read()
		fp.close()	
		return 	content


catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)                           #�������Ϣ���浽Bunch������
for mydir in catelist:
		class_path = seg_path + mydir + "/"
		file_list = os.listdir(class_path)
		for file_path in file_list:
				fullname = class_path + file_path
				bunch.label.append(mydir)                    #���浱ǰ�ļ��ķ����ǩ
				bunch.filenames.append(fullname)             #���浱ǰ�ļ����ļ�·��
				bunch.contents.append(readfile(fullname).strip())           #�����ļ�������

#Bunch����־û�
file_obj = open(wordbag_path,"wb")
pickle.dump(bunch,file_obj)
file_obj.close()

print "�����ı��������!!!"