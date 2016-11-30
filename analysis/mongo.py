# -*- coding: utf-8 -*-

import pymongo
from pprint import pprint


mongo_uri = 'mongodb://localhost:27017'
database_name = 'fedsupcourt'
collection_name = 'rulings'

client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

print(collection.count())

result = collection.aggregate([
    {'$project': {'kw': '$international_treaties.keywords.keyword'}},
    {'$unwind': '$kw'},
    {'$group': {
        '_id': "$kw",
        'count': {'$sum': 1}}
    },
    {'$sort': {'_id': 1}}
])

international_treaties = []

for keyword in result:
    international_treaties.append(keyword)
    print('%-50s | %3d' % (keyword['_id'], keyword['count']))

print(len(international_treaties))


count_containing_field = lambda keyword_type: collection.find({keyword_type: {'$exists': 1}}).count()
count_language = lambda language: collection.find({'language': language}).count()

print(count_containing_field('international_treaties'))
print(count_containing_field('international_customary_law'))
print(count_containing_field('international_law_in_general'))
print('===============================================')

print('Language:')
print(count_containing_field('language'))
print(count_language('de'))
print(count_language('fr'))
print(count_language('it'))
print(count_language('rr'))
print('===============================================')

result = collection.find({'ruling_id.bge_nb': 95, 'ruling_id.volume': 'III', 'ruling_id.ruling_nb': 76},
                         {'title_of_judgement': 1, 'date': 1, 'type_of_proceeding': 1, 'language': 1, 'department': 1,
                          'dossier_number': 1, 'involved_parties': 1, 'url': 1})
print(result.count())
for i, r in enumerate(result):
    pprint(r, width=300)
    if i > 1:
        break
client.close()