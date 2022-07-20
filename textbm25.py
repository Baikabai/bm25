from enum import EnumMeta
from gensim import corpora
from gensim.summarization import bm25
import os
import re

def cor(f):
    file = 'E:/M2/code_name/'+f
    f = open(file,'r',encoding='utf-8')
    text = f.read()
    text = text.split(' ')
    new_text = []
    for i in text:
        i = i.replace('\n','')
        new_text.append(i)
    return new_text
    

corpus = []
dirname = 'E:/M2/code_name/'
filename = os.listdir(dirname)
filenames = []
for i in filename:
    corpus.append((cor(i)))
    filenames.append(i)
dictionary = corpora.Dictionary(corpus)
doc_vectors = [dictionary.doc2bow(text) for text in corpus]
vec1 = doc_vectors[0]
vec1_sorted = sorted(vec1, key=lambda x:x[1], reverse=True)

bm25Model = bm25.BM25(corpus)
average_idf = sum(map(lambda k: float(bm25Model.idf[k]), bm25Model.idf.keys())) / len(bm25Model.idf.keys())
query = ['電気自動車','電池','ハイブリッド車']
scores = bm25Model.get_scores(query)
dic = {}
for i,s in enumerate(scores):
    dic[i] = s

d = sorted(dic.items(),key=lambda x:x[1],reverse=True)
na = []
for i,(k,v) in enumerate(d):
    na.append(k)
    if i == 478:
        break
fna = []
for i in na:
    fname = filenames[i]
    fname = int(re.sub('.txt','',fname))
    fna.append(fname)
print(len(fna))

import pandas as pd
df = pd.read_excel('111.xlsx')
l = list(df['証券コード'])
t = []
for i in fna:
    if i in l:
        t.append(i)
print(len(t)/479)


