import jieba   #导入分词库
import math
import sys     #导入命令行参数模块

orig_text=open(sys.argv[1], 'r', encoding='utf-8')
tested_text=open(sys.argv[2],'r',encoding='utf-8')
result=open(sys.argv[3],'w',encoding='utf-8')

or_txt=orig_text.read()
te_txt=tested_text.read()
words1=jieba.lcut(or_txt)
words2=jieba.lcut(te_txt)

def CalEachWordAp(words): #文本中记录各词语出现次数r
    d={}
    for word in words:
        d[word]=0
    
    for word in words:
        d[word]+=2

    return d

d1=CalEachWordAp(words1) 
d2=CalEachWordAp(words2)       

#计算相似度用Jaccard index


n=0#分子
m=0#分母
for word1 in d1:
    for word2 in d2:
        if word1==word2:
            n+=d1[word1]>d2[word2] and d2[word2] or d1[word1]
            m+=d1[word1]>d2[word2] and d1[word1] or d2[word2]
t=0#标志是否有相同
for word1 in d1:
    t=0
    for word2 in d2:
        if word1==word2:
            t=1
    if t==0:
        m+=d1[word1]

for word2 in d2:
    t=0 
    for word1 in d1:
        if word1==word2:
            t=1
    if t==0:
        m+=d2[word2]


J=n/m

result.write(str(J))
print(n,m)
print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))