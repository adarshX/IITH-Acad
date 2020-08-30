#Auto encoder on mnist data
# network size 

#from mlxtend.data import loadlocal_mnist
#from mnist import MNIST
import cPickle
import numpy as np 
import matplotlib.pyplot as plt
import csv
import struct


def read_idx(filename):
    with open(filename, 'r') as f:
        zero, data_type, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
        return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)

A = read_idx('train-images-idx3-ubyte')
print(A)

n = len(A)
print(n)
m = len(A[0])
print(m)



