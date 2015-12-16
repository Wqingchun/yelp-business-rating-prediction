__author__ = 'harshad'

import pickle
import simplejson

def loadUsers():
    file = open('/Users/harshad/PycharmProjects/Yelp Data/yelp_training_set/yelp_training_set_user.json')
    json_list = []
    user_hash_set = set()
    for each_row in file:
        json_dict = simplejson.loads(each_row)
        # json_list.append(json_dict)
        user_hash_set.add(json_dict['user_id'])
    return json_list,user_hash_set

if __name__ == '__main__':
    users_info, user_hash_set = loadUsers()
    user_file = open('user_file',mode='w')
    pickle.dump(user_hash_set,user_file)
    print len(user_hash_set)
