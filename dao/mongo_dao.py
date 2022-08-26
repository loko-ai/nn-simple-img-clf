import pymongo


def get_client(host, port=27017):
    client = pymongo.MongoClient(host=host,port=port)
    return client.db

class MongoDAO:

    def __init__(self, db):
        self.db = db

    def insert(self, coll, d):
        return bool(self.db[coll].insert_one(d))

    def search(self, coll, d):
        for el in self.db[coll].find(d, {'_id': False}):
            print(el)
            yield el

    def delete(self, coll, d):
        return bool(self.db[coll].delete_many(d))

if __name__ == '__main__':
    db = get_client("localhost")
