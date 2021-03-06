import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.bitbox
strategies = db.strategies


def submit_strategy(fnm, name=None, longname=None):
    max_id_test = strategies.find_one({}, sort=[('id', pymongo.DESCENDING)])
    if max_id_test is None:
        max_id = -1
    else:
        max_id = max_id_test['id']
    curr_id = max_id + 1
    if name is None:
        name = 'strategy_{}'.format(curr_id)
    if longname is None:
        longname = name
    if strategies.count({'name': name}) > 0:
        raise Exception('Strategy with that common name already added')
    strategies.insert({
        'id': curr_id,
        'fnm': fnm,
        'name': name,
        'longname': longname})
    print('Strategy submitted with name {} and id {}'.format(name, curr_id))
