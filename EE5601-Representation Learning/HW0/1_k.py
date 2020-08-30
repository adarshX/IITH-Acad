from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv
import random
from scipy.spatial import distance
import statistics as st

im = Image.open('download.png', 'r')
pix_val = list(im.getdata())
set(pix_val)
pix_val_1 = list(set(pix_val))
N = len(pix_val_1)
N = N/100
x_pix = []
y_pix = []
z_pix = []


x_centroid = []
y_centroid = []
z_centroid = []

for i in range(N):
	x_pix.append(pix_val_1[i][0])
	y_pix.append(pix_val_1[i][1])
	z_pix.append(pix_val_1[i][2])

np.random.seed(200)
k = 3

centroid = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(k)]

for i in range(k):
	x_centroid.append(centroid[i][0])
	y_centroid.append(centroid[i][1])
	z_centroid.append(centroid[i][2])


print(pix_val_1[0])


fig = plt.figure(figsize=(5, 5))
plt.scatter( x_pix,y_pix,z_pix ,color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in range(k):
    plt.scatter(x_centroid,y_centroid,z_centroid, color=colmap[i+1])
plt.show()
