from pymongo import MongoClient
from bson import binary

connect = MongoClient()
db = connect.test
collect = db.image

def insertFile():
    with open('./photo/test.jpg', 'rb') as myimage:
        collect.insert_one(dict(
            content= binary.Binary(myimage.read()),
            filename = 'test.jpg'
        ))

def getFile():
    data = collect.find_one( {'filename':'test.jpg'} )
    out = open('./photo/test1.jpg','wb')
    out.write(data['content'])
    out.close()

# insertFile()
# getFile()