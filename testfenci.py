# encoding:utf-8
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

def savefile(savepath, content):
    fp = open(savepath, "wb")
    fp.write(content)
    fp.close()


def readfile(path):
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    return content


corpus_path = "G:/python_txt/answer/train/"  # 未分词分类语料库路径
seg_path = "G:/python_txt/answer/test/"  # 分词后分类语料库路径


catelist = os.listdir(corpus_path)


for mydir in catelist:
    class_path = corpus_path + mydir + "/"
    seg_dir = seg_path + mydir + "/"
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    filelist = os.listdir(class_path)
    for filepath in filelist:
        fullname = class_path + filepath
        content = readfile(fullname).strip()
        content = content.replace("\r\n", "").strip()
        content_seg = jieba.cut(content)
        savefile(seg_dir + filepath, " ".join(content_seg))

        print "中文语料分词结束!!!"