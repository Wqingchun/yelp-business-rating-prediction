__author__ = 'harshad'

import numpy as np
import scipy
import matplotlib.pyplot as plt
import pickle

predicted_arr = pickle.load(open('predicted_flattened_file',mode='rb'))
unpredicted_arr = pickle.load(open('unpredicted_flattened_file',mode='rb'))
print 'len of predicted and unpredicted = ',len(unpredicted_arr),len(predicted_arr)
plt.plot(range(len(unpredicted_arr)),unpredicted_arr)
plt.plot(range(len(predicted_arr)),predicted_arr)
plt.show()

# user_map = open('user_map',mode='rb')
# obj = pickle.load(user_map)
# user_map.close()
#
# b_map = open('business_map',mode='rb')
# b_obj = pickle.load(b_map)
# b_map.close()


