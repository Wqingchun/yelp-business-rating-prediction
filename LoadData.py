__author__ = 'harshad'

'''Yelp Business Ratings Prediction'''

import simplejson
import json
import time
import numpy as np
from pprint import pprint

start_time = time.time()
file = open('yelp_training_set_review.json')
file_content = file.read()
json_list = []
rows = file_content.split('\n')
print rows[600]

i = 1
count = 0
userA_count = 0
sum_rating = 0
users_hash_set = set()
business_hash_set = set()

print 'rows size = ',len(rows)
file = open('users.txt',mode='w')
for row in rows:
    json_dict = simplejson.loads(row)
    json_list.append(json_dict)

    if json_dict['user_id'] != None:
        file.write(json_dict['user_id']+'\n')
        users_hash_set.add(str(json_dict['user_id']).strip())
    business_hash_set.add(json_dict['business_id'])
    if(json_dict['stars'] != None):
        count += 1
        sum_rating = sum_rating + json_dict['stars']
    # print i
    i += 1

print len(json_list)

print 'exec time = ', time.time() - start_time
print 'average rating of all the businesses = ',(sum_rating/float(229907))
print 'total ratings = ',count
print 'user RRTraCQw77EU4yZh0BBTag ratings\' count = ',userA_count
print 'users total = ',len(users_hash_set)
print 'business total = ',len(business_hash_set)

'''Create users x business ratings matrix'''
matrix = np.ndarray(shape=(len(users_hash_set),len(business_hash_set)))

'''Create users hashmap'''
user_hash_map = { }
reverse_user_hash_map = { }
j = 0
for user in users_hash_set:
    user_hash_map[j] = user
    reverse_user_hash_map[user] = j
    j += 1
print len(user_hash_map)
print len(reverse_user_hash_map)

'''Create business hashmap'''
k=0
business_hash_map = { }
reverse_business_hash_map = { }
for business in business_hash_set:
    business_hash_map[k] = business
    reverse_business_hash_map[business] = k
    k += 1
print len(business_hash_map)
print len(reverse_business_hash_map)

first_i_index = 0
first_j_index = 0

for dict in json_list:
    user_id = dict['user_id']
    business_id = dict['business_id']
    index_i = reverse_user_hash_map[user_id]
    index_j = reverse_business_hash_map[business_id]
    first_i_index = index_i
    first_j_index = index_j
    matrix[index_i,index_j] = dict['stars']

print len(matrix[0])
print 'first entry in the matrix = ',matrix[first_i_index,first_j_index]
