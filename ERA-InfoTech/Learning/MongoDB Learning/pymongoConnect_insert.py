import pymongo
import dns
from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0-0qpab.mongodb.net/test?retryWrites=true&w=majority")
db = client['mydB']
posts = db.posts
post_data = {
             'title':'Python and MongoDB connection',
             'content':'Connection code',
             'author':'Palash'
            }
result = posts.insert_one(post_data)
print('First post: {0}'.format(result.inserted_id))

bills_post = posts.find_one({'author': 'Palash'})
print(bills_post)
