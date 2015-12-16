__author__ = 'harshad'

import pickle
import json
import numpy as np
import time
import scipy
import math
from MatrixFactorization import *
# from sklearn.decomposition import NMF
import sklearn
from sklearn.metrics import mean_squared_error

new_matrix = pickle.load(open('ratings_file',mode='rb'))

u_map = open('user_map',mode='rb')
u_map = pickle.load(u_map)
b_map = open('business_map',mode='rb')
b_map = pickle.load(b_map)

u_name= open('user_name',mode='rb')
u_name = pickle.load(u_name)
b_name = open('business_name',mode='rb')
b_name = pickle.load(b_name)

print 'size of ratings matrix = ',new_matrix.shape
print 'nonzero entries index for reference = ', np.nonzero(new_matrix)

print 'main process..'
start = time.time()
# N = len(new_matrix)
# M = len(new_matrix[0])
# latent_features = 70
# U = numpy.random.rand(N,latent_features)
# V = numpy.random.rand(M,latent_features)
# # nP, nQ = mFactorization(new_matrix, P, Q, latent_features)
# gen_U, gen_V = matrixFactorization(new_matrix,latent_features, U, V,alpha=0.0005,beta=0.05)
# gen_mat = numpy.dot(gen_U, gen_V.T)
#
# print np.nonzero(np.subtract(new_matrix,gen_mat))
# # print 'rmse = ', np.sqrt(mean_squared_error(np.ndarray.flatten(new_matrix),np.ndarray.flatten(nR)))
#
# unpredicted_flattened = []
# predicted_flattened = []

# sum = 0.0
# count_nonzero = 0
# for i in range(len(new_matrix)):
#     for j in range(len(new_matrix[0])):
#         if new_matrix[i,j] != 0.0:
#
#             unpredicted_flattened.append(new_matrix[i,j])
#             predicted_flattened.append(gen_mat[i,j])
#
#             diff = ((float(new_matrix[i,j]) - float(gen_mat[i,j]))**2)
#             sum = sum + diff
#             count_nonzero = count_nonzero + 1
#
# rmse = math.sqrt(float(sum)/float(count_nonzero))
# print 'rmse = ',rmse
# print 'predicted values = ', gen_mat

gen_mat = pickle.load(open('predicted_ratings',mode='rb'))

while True:
    i = int(raw_input('enter user number (between 0 and 405)\n'))
    print 'name of the user entered : ', u_name[u_map[i]]
    j = int(raw_input('enter business number (between 0 and 273)\n'))
    print 'name of the business entered : ', b_name[b_map[j]]
    print 'oringal rating = ',new_matrix[i,j]
    print 'predicted rating = ',gen_mat[i,j]
    ans = raw_input('show recommendations?')
    if ans == 'yes':
        print 'Recommended Businesses for "',u_name[u_map[i]],'" are \n'
        for ind in range(len(gen_mat[0])):
            if new_matrix[i,ind] == 0.0 and gen_mat[i,ind] >= 4.5 and gen_mat[i,ind] < 5.0:
                print b_name[b_map[ind]], ' ; rating = ',gen_mat[i,ind]
    else:
        decision = raw_input('Do you want to continue ? ')
        if decision == 'no':
            break

''' to uncomment this section of code, first delete the belowmentioned files.
 then run the script.
 the generated files can be used in the Plotting.py script to plot the results
 '''
#
# predicted_ratings = open('predicted_ratings',mode='wb')
# pickle.dump(gen_mat,predicted_ratings)
# predicted_ratings.close()

# unpredicted_flattened_file = open('unpredicted_flattened_file',mode='wb')
# pickle.dump(unpredicted_flattened,unpredicted_flattened_file)
# unpredicted_flattened_file.close()
#
# predicted_flattened_file = open('predicted_flattened_file',mode='wb')
# pickle.dump(predicted_flattened,predicted_flattened_file)
# predicted_flattened_file.close()

'''end of to_uncomment '''

print 'time required = ', time.time() - start