# -*- coding: utf-8 -*-
# @Time : 2020/4/1 18:15
# @Author : wangmengmeng
import os
count_list = []
for dirpath, dirnames, filenames in os.walk(r"D:\parse_swagger_api\api"):
    file_count = 0
    for file in filenames:
        file_count = file_count + 1
    count_list.append(file_count)
    print(dirpath,file_count)
print(sum(count_list))
    # print(dirpath,dirnames,filenames)