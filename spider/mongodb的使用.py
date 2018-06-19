import pymongo

client = pymongo.MongoClient('localhost',27017)#连接数据库
mydb = client['mydb']#新建mydb数据库
shiyan = mydb['text']#新建text数据集合

shiyan.insert_one({'name':'Jan','sex':'man','grade':89})#插入数据