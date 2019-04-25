# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:06:27 2019

@author: user
"""

# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line) ## strip: 針對 str, 我能將多餘的空格或換行 '去除'
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)

print('留言的平均長度是', sum_len/len(data))