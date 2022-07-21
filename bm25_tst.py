import os
import math
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


f = []
tf = {}
idf = {}
k1 = 1.5
b = 0.5
def inition(docs):
    D = len(docs)
    avgdl = sum([len(doc)+0.0 for doc in docs]) / D
    for doc in docs:
        tmp = {}
        for word in doc:
            tmp[word] = tmp.get(word,0) + 1
        f.append(tmp)
        for k in tmp.keys():
            tf[k] = tf.get(k,0) + 1
    for k,v in tf.items():
        idf[k] = math.log(D-v+0.5) - math.log(v+0.5)
    
    return D , avgdl
D,avgdl = inition(corpus)
document = corpus
def sim(doc,index):
    score = 0.0
    for word in doc:
        if word not in f[index]:
            continue
        d = len(document[index])
        score += (idf[word] * f[index][word] * (k1 + 1) / (f[index][word] + k1 * (1-b + b * d / avgdl)))
    return score

def simall(doc):
    scores = []
    for index in range(D):
        score = sim(doc,index)
        scores.append(score)
    return scores


s = simall(['電気自動車','電池','ハイブリッド車'])
s_d = {}
for idx,value in enumerate(s):
    s_d[idx] = value

s_s = sorted(s_d.items(),key=lambda x:x[1],reverse=True)
print(s_s)

print(filenames[2657],filenames[1750])