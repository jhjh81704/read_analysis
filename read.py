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

print(data[0])


# 文字計數
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word  in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的 key 進 wc 字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔! ')

print('感謝使用本查詢功能')





#------------------------------------------------------------------

# 留言分析

sum_len = 0
for d in data:
   sum_len += len(d)
   print(sum_len)

print('留言的平均長度是', sum_len/len(data))


new = []
for d in data:
   if len(d) < 100:
       new.append(d)
print('一共有', len(new), '筆留言長度小於 100')
print(new[0])
print(new[1])


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到 good')
print(good[0])


good = [d for d in data if 'good' in d]
print(good)


bad = ['bab' in d for d in data]
print(bad)

