import pymongo

# uri = "mongodb://<dbuser>:<dbpassword>@ds163014.mlab.com:63014/mdata"
connect = pymongo.MongoClient("mongodb://wei:qwe728386@ds163014.mlab.com:63014/mdata")
db = connect.mdata # database name
collect = db.mcollect # collection name

collect.stats

data = {
    "name":"Kai",
    "age":23
}

collect.insert_one(data)
data = collect.find({})
for d in data:
    print(d)

collect.delete_many({})