import requests
from requests.exceptions import ConnectionError
import json
import pymongo
from multiprocessing import Pool


conn=pymongo.MongoClient(host='localhost',port=27017)
db=conn['baidu_top']
coll=db['data']


def save_data(url):
    try:
        html = requests.get(url)
        data_str = html.text
        data_dict = json.loads(data_str)
        for data in data_dict:
            try:
                coll.insert(data)
                print(data)
            except:
                print('error',data)
    except ConnectionError:
        print('ConnectionError:', url)


if __name__ == '__main__':
    urls = ('http://top.baidu.com/news/pagination?pageno={0}'.format(x) for x in range(1, 100))
    pool=Pool(processes=4)
    pool.map(save_data,urls)


