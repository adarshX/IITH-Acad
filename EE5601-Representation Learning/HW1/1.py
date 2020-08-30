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


'''fig = plt.figure(figsize=(5, 5))
plt.scatter( x_pix,y_pix,z_pix ,color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in range(k):
    plt.scatter(x_centroid,y_centroid,z_centroid, color=colmap[i+1])
plt.show()
'''
## Assignment Stage

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

 df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
















