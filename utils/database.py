# encoding=utf-8
'''
    数据库数据获取
'''
import pymongo


class Mongodb(object):

    # 初始化
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        self.host = dbconfig.get('host')
        self.port = dbconfig.get('port')
        self.user = dbconfig.get('user')
        self.password = dbconfig.get('password')
        self.database = dbconfig.get('database')
        self._client = pymongo.MongoClient(self.host, self.port)
        if self.database:
            self._db = self._client[self.database]
        if self.user and self.password:
            self._db.authenticate(self.user, self.password)

    # 查询所有结果, 不去掉_id就返回
    def all_items(self, collection_name):
        collection = self._db[collection_name]
        collection_list = collection.find()
        cl = []
        for r in collection_list:
            # r.pop('_id')
            r['_id'] = str(r['_id'])
            cl.append(r)
        return cl

    # 查询符合条件的所有结果
    def find(self, collection_name, query=None):
        collection = self._db[collection_name]
        if query is None:
            rs = collection.find()
            cl = []
            for r in rs:
                # r.pop('_id')
                r['_id'] = str(r['_id'])
                cl.append(r)
        else:
            rs = collection.find(query)
            cl = []
            for r in rs:
                # r.pop('_id')
                r['_id'] = str(r['_id'])
                cl.append(r)
        return rs

    # 查询符合条件的数量
    def find_count(self, collection_name, query=None):
        collection = self._db[collection_name]
        if query is None:
            rs = collection.find().count()
        else:
            rs = collection.find(query).count()
        return rs

    def find_and_mark(self, collection_name, query=None, update=None):
        collection = self._db[collection_name]
        if query is None:
            rs = collection.find()
        else:
            rs = collection.find_and_modify(query, update={"$set": update})
        return list(rs)

    # 查询符合条件的第一条结果
    def find_one(self, collection_name, query=None):
        if query is None:
            query = {}
        collection = self._db[collection_name]
        rs = collection.find_one(query)
        return rs

    # 查询符合条件的第一条结果
    def find_one_and_mark(self, collection_name, query, update):
        collection = self._db[collection_name]
        rs = collection.find_one_and_update(query, update={"$set": update})
        return rs

    # 插入时默认不去重, 可以按特定值去重 可以插1条或多条
    def insert_many(self, collection_name, data_input, condition=None):
        if isinstance(data_input, list):
            for data in data_input:
                self.insert_one(collection_name, data, condition)
        else:
            self.insert_one(collection_name, data_input, condition)

    def insert_one(self, collection_name, input, condition=None):
        if input is None:
            pass
        else:
            collection = self._db[collection_name]
            query = {}
            if condition is None:
                collection.insert_one(input)
            else:
                for key in condition:
                    query[key] = input.get(key)
                tmp = self.find_one(collection_name, query)
                if tmp is None:
                    collection.insert_one(input)

    # 更新单条数据，upsert如果为true，没有与过滤器匹配的文档，则执行插入，可选
    def update_one(self, collection_name, query, form, upsert=False):
        collection_name = self._db[collection_name]
        collection_name.update_one(query, form, upsert=upsert)

    def update_many(self, collection_name, query, form):
        collection = self._db[collection_name]
        rs = collection.update_many(query, form)
        return rs

    def remove(self, collection_name, query):
        collection = self._db[collection_name]
        collection.remove(query)

    def database_info(self):
        databases = list(filter(lambda x:  x != 'admin' and x != 'config' and x != 'local', [
            database for database in self._client.list_database_names()]))
        collection_dict = []
        for database in databases:
            collections = self._client[database].list_collection_names(session=None)
            collection_count = [{'collection': i, 'count': self._client[database][i].find().count()} for i in collections]
            collection_dict.append(collection_count)
        return dict(zip(databases, collection_dict))

    def all_collection(self):
        return self._db.list_collection_names(session=None)

    def __enter__(self):
        """Setup; Must return a Mongodb object."""
        print('数据库正在连接')
        return Mongodb(self.dbconfig)

    def __exit__(self, exception_type, exception_value, traceback):
        self._client.close()
        print('数据量连接已关闭')


if __name__ == "__main__":
    dbconfig = {
        'host': '192.168.1.184',
        'port': 27017,
        'user': '',
        'password': '',
        'database': 'journal'
    }
    collection_name = 'issn_info'
    with Mongodb(dbconfig) as data:
        query = {'series_id': 'bc0dfc51309ff77fc56733b99bb81e77'}
        form = {'$set': {'issns.xeissn': '2'}}
        data.update_one(collection_name, query, form)
        print(data.find_one(collection_name, query))
