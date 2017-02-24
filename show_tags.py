import pymongo
import jieba.analyse

conn = pymongo.MongoClient(host='localhost', port=27017)
db = conn['baidu_top']
coll = db['data']

data = coll.find()

content = ' '.join(d['keyword'] for d in data)

tags = jieba.analyse.extract_tags(content, topK=50)

tags_str = ' '.join(tags)

with open('data.txt', 'w',encoding='utf-8') as f:
    f.write(tags_str)

