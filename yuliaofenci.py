# encoding:utf-8
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')


def savefile(savepath, content):  # 保存至文件
    fp = open(savepath, "wb")
    fp.write(content)
    fp.close()


def readfile(path):  # 读取文件
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    return content


corpus_path = "G:/python_txt/answer/train/"  # 未分词分类语料库路径
seg_path = "G:/python_txt/answer/test/"  # 分词后分类语料库路径

catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录

for mydir in catelist:
    class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径
    seg_dir = seg_path + mydir + "/"  # 拼出分词后的语料分类目录
    if not os.path.exists(seg_dir):  # 是否存在目录，没有则创建
        os.makedirs(seg_dir)
    file_list = os.listdir(class_path)  # 获取类别目录下的所有文件
    for file_path in file_list:  # 遍历类别目录下的文件
        fullname = class_path + file_path  # 拼出文件名全路径
        content = readfile(fullname).strip()  # 读取文件内容
        content = content.replace("\r\n", "").strip()  # 删除换行和多余的空格
        content_seg = jieba.cut(content)  # 为文件内容分词

        savefile(seg_dir + file_path, " ".join(content_seg))

        print "中文语料分词结束!!!"
