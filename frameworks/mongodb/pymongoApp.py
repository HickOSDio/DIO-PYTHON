import pprint
from datetime import datetime

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://hick:!JDSKAdKL@12kl1@cluster0.123asda.mongodb.net/?retryWrites=true&w=majority")

#criando collection
db = client.test
collections = client.test.test_collection

print(db.test_collection_names)

# definição para compor o doc
post = {
    'author': 'Hick',
    'text': 'My first mongo db application on python!',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
#print(db.list_collection_names())


#bulk inserts
new_posts = [{
    'author': 'Hick',
    'text': 'Postando de novo',
    'tags': ['bulk', 'insert', 'insert'],
    'date': datetime.utcnow()
    },
    {
    'author': 'Hick',
    'text': 'Terceira vez',
    'tittle': 'Oloquinho meu',
    'date': datetime(2023, 3, 15, 19, 12)
    }
]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

print('Recuperação final')
pprint.pprint(db.posts.find_one({'author': 'Hick'}))

for post in posts.find():
    pprint.pprint(post)
    print('----')
