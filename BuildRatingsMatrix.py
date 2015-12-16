__author__ = 'harshad'

import pickle
import json
import simplejson
import numpy as np
import time
import scipy
from MatrixFactorization import *
# from sklearn.decomposition import NMF
import sklearn
from sklearn.metrics import mean_squared_error

def processData():
    start_time = time.time()

    user_file = open('user_file')
    business_file = open('business_file')
    ratings_file = open('ratings_file',mode='wb')
    big_file = open('Yelp Data/yelp_training_set/yelp_training_set_review.json')

    user_ids = pickle.load(user_file)
    business_ids = pickle.load(business_file)

    user_hash_map = { }
    business_hash_map = { }

    i=0
    for user in user_ids:
        user_hash_map[user] = i
        user_hash_map[i] = user
        i += 1

    i=0
    for business in business_ids:
        business_hash_map[business] = i
        business_hash_map[i] = business
        i += 1

    matrix = np.zeros(shape=(len(user_ids),len(business_ids)))

    count = 0
    for record in big_file:
        '''if the user id is in the user hash set info, add its review to the matrix'''
        # dict = json.loads(str(record).replace("\'", ''));-
        dict = simplejson.loads(record)
        if dict['user_id'] in user_ids:
            user_index = user_hash_map[dict['user_id']]
            business_index = business_hash_map[dict['business_id']]
            # print 'indexes = ', (user_index,business_index)
            matrix[user_index,business_index] = dict['stars']
            count = count + 1

    print 'original matrix shape = ',matrix.shape

    sum_of_cols = np.sum(matrix, axis=1)
    cols_sum = []
    print sum_of_cols.shape
    cols_sum = np.ndarray.flatten(sum_of_cols)
    sorted_cols_sum = sorted(cols_sum)
    print 'shape of sum of all columns = ',len(cols_sum)

    print 'all users with more reviews = ', len([i for i in cols_sum if i >= 255])
    rows_index_list = [ ]
    j = 0

    for each in cols_sum:
        if each >= 255:
            rows_index_list.append(j)
        j = j + 1

    new_users_map = { }
    new_business_map = { }

    for i in range(len(rows_index_list)):
        new_users_map[i] = user_hash_map[rows_index_list[i]]
        new_users_map[user_hash_map[rows_index_list[i]]] = i

    print 'total len of new rows = ', len(rows_index_list)
    print '# this is how the rows_index_list looks like -> ', rows_index_list
    print 'total length of new hashmap = ', len(new_users_map)

    new_matrix = matrix[rows_index_list,:]

    print 'new matrix shape = ', new_matrix.shape

    sum_of_rows = np.sum(new_matrix,axis=0)
    rows_sum = []
    rows_sum = np.ndarray.flatten(sum_of_rows)
    cols_index_list = [ ]

    print 'all columns with reviews = ', len([i for i in rows_sum if i >= 110.0])
    j = 0
    for each in rows_sum:
        if each >= 110.0:
            cols_index_list.append(j)
        j = j + 1

    for i in range(len(cols_index_list)):
        new_business_map[i] = business_hash_map[cols_index_list[i]]
        new_business_map[business_hash_map[cols_index_list[i]]] = i

    print 'length of cols_index_list = ',len(cols_index_list)
    print '# this is how the cols_index_list looks like -> ', cols_index_list
    print 'length of the new formed columns hashmap = ',len(new_business_map)
    print 'for example, first entry in new business hash map corresponds to the business : ',new_business_map[0]
    print 'for example, vice versa : ',new_business_map['ke3RFq3mHEAoJE_kkRNhiQ']

    new_matrix = new_matrix[:,cols_index_list]
    print 'ready matrix shape = ',new_matrix.shape
    print 'number of ratings to predict = ', len(np.nonzero(np.ndarray.flatten(new_matrix))[0])
    print new_matrix
    pickle.dump(new_matrix,file=ratings_file)

    '''For the new matrix created, store the index to name mapping for users and businesses.'''

    '''Users: User_id to Name mapping'''
    u_file = open(name='Yelp Data/yelp_training_set/yelp_training_set_user.json',mode='r')
    user_name_map = { }
    for each_line in u_file:
        u_dict = simplejson.loads(each_line)
        u_id = u_dict['user_id']
        u_name = u_dict['name']
        user_name_map[u_id] = u_name
    u_file.close()

    '''Businesses: Business_id to Name mapping'''
    b_file = open(name='Yelp Data/yelp_training_set/yelp_training_set_business.json',mode='r')
    business_name_map = { }
    for each_line in b_file:
        b_dict = simplejson.loads(each_line)
        b_id = b_dict['business_id']
        b_name = b_dict['name']
        business_name_map[b_id] = b_name
    b_file.close()

    '''For displaying names of the results, dump the pickles of
    1. new_users_map
    2. new_business_map
    3. user_name_map
    4. business_name_map
    '''
    new_uMap_file = open('user_map',mode='wb')
    print 'first entry of user map = ',new_users_map[0]
    pickle.dump(new_users_map, new_uMap_file)
    new_uMap_file.close()

    new_bMap_file = open('business_map',mode='wb')
    pickle.dump(new_business_map, new_bMap_file)
    new_bMap_file.close()

    user_name_file = open('user_name',mode='wb')
    pickle.dump(user_name_map, user_name_file)
    user_name_file.close()

    business_name_file = open('business_name',mode='wb')
    pickle.dump(business_name_map, business_name_file)
    business_name_file.close()

    print 'time =', time.time() - start_time

if __name__ == '__main__':
    processData()