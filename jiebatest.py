#encoding:utf-8
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("С��1995���ҵ�ڱ����廪��ѧ", cut_all=False)
print "Default Mode:", " ".join(seg_list)

seg_list = jieba.cut("С��1995���ҵ�ڱ����廪��ѧ")
print " ".join(seg_list)

seg_list = jieba.cut("С��1995���ҵ�ڱ����廪��ѧ", cut_all=True)
print "Full Mode:", " ".join(seg_list)

seg_list = jieba.cut_for_search("С��˶ʿ��ҵ���й���ѧԺ�������������ձ�������ѧ����")
print "/ ".join(seg_list)