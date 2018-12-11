# -*- coding: utf-8 -*-  

import math

movie_data = {"��������": [45, 2, 9, "ϲ��Ƭ"],  
              "������": [21, 17, 5, "ϲ��Ƭ"],  
              "���ŷ���3": [54, 9, 11, "ϲ��Ƭ"],  
              "������è3": [39, 0, 31, "ϲ��Ƭ"],  
              "��Ӱ����": [5, 2, 57, "����Ƭ"],  
              "Ҷ��3": [3, 2, 65, "����Ƭ"],  
              "�׶�����": [2, 3, 55, "����Ƭ"],  
              "�ҵ��ع�үү": [6, 4, 21, "����Ƭ"],  
              "����": [7, 46, 4, "����Ƭ"],  
              "ҹ��ȸ": [9, 39, 8, "����Ƭ"],  
              "��������": [9, 38, 2, "����Ƭ"],  
              "�²�������": [8, 34, 17, "����Ƭ"]} 
              
            
x = [23, 3, 17]  
KNN = []  
for key, v in movie_data.items():  
    d = math.sqrt((x[0] - v[0]) ** 2 + (x[1] - v[1]) ** 2 + (x[2] - v[2]) ** 2)  
    KNN.append([key, round(d, 2)]) 
KNN.sort(key=lambda dis: dis[1])  
KNN=KNN[:5] 


labels = {"ϲ��Ƭ":0,"����Ƭ":0,"����Ƭ":0}
for s in KNN:
		label = movie_data[s[0]]
		labels[label[3]] += 1
labels =sorted(labels.items(),key=lambda l: l[1],reverse=True)
print(labels,labels[0][0])		


print str(labels).decode('string_escape') 
