from faker import Faker
import time
import pymongo

conn = pymongo.MongoClient('my_mongodb')
db = conn.students

fake = Faker()

while True:
    name = fake.name()
    doc = {'name': name}
    db.vanilla.insert(doc)

    time.sleep(3)
