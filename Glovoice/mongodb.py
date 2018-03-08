from pymongo import MongoClient

client = MongoClient()
db = client.database

def builddb():

 db.words.remove()
 dictionary = open("dictionary.txt", 'r')

 for line in dictionary:
       word, num = line.split(" ")
       num = float(num)
       db.words.insert_one({"word":word,"float":num})

 dictionary.close()

def word(f):
    return db.words.find_one({"float": f}, {'_id': 0, "word": 1})['word']

builddb()
print(word(1.6))
