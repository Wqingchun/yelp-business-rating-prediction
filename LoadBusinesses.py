__author__ = 'harshad'

import pickle
import simplejson

def loadBusinesses():
    file = open('/Users/harshad/PycharmProjects/Yelp Data/yelp_training_set/yelp_training_set_business.json')
    json_list = []
    user_hash_set = set()
    for each_row in file:
        json_dict = simplejson.loads(each_row)
        # json_list.append(json_dict)
        user_hash_set.add(json_dict['business_id'])
    return json_list,user_hash_set

if __name__ == '__main__':
    business_info, business_hash_set = loadBusinesses()
    business_file = open('business_file',mode='w')
    pickle.dump(business_hash_set,business_file)
    print len(business_hash_set)