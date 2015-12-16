__author__ = 'harshad'

import numpy
import numpy as np

def matrixFactorization(ratingsMatrix, latentFeatures, U, V, alpha=0.0005, beta=0.05, numberOfIterations=80):
    V = V.transpose()
    for iteration in range(numberOfIterations):
        row_id = 0
        for each_row in ratingsMatrix:
            for i in range(len(each_row)):
                if each_row[i] > 0.0:
                    error_ij = each_row[i] - np.dot(U[row_id,:],V[:,i])
                    for j in range(latentFeatures):
                        U[row_id,j] += alpha * (2 * error_ij * V[j,i] - beta * U[row_id,j])
                        V[j,i] += alpha * (2 * error_ij * U[row_id,j] - beta * V[j,i])
            row_id += 1

        reconstructed_mat = np.dot(U,V)
        if calcError(ratingsMatrix,U,V,alpha,beta,latentFeatures) < 0.002: break
    return U,V.transpose()

def calcError(ratingsMatrix, U, V, alpha, beta, latentFeatures):
    row_id = 0
    error = 0.0
    for each_row in ratingsMatrix:
            for i in range(len(each_row)):
                if each_row[i] > 0.0:
                    error += ((ratingsMatrix[row_id,i] - numpy.dot(U[row_id,:],V[:,i])) ** 2)
                    for j in range(latentFeatures):
                        error += (beta * 0.5) * ((U[row_id,j] ** 2) + (V[j,i]**2))
            row_id += 1
    return error