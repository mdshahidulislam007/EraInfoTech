import pymongo
import dns
from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0-0qpab.mongodb.net/test?retryWrites=true&w=majority")
db = client['mydB']


posts = db.posts

print(posts.count_documents({}))   #how many data in my collection/table

bills_post = posts.find_one({'author': 'Palash'})  #find() diye table er data search kora jay
print(bills_post)

#for update

updt = {
   'author':'Shahidul'
}

posts.update_one({'title':'Python and MongoDB connection'},{'$set':updt})

print(posts)

#for delete

posts.delete_one({'author':'Shahidul'})
print(posts.count_documents({}))

