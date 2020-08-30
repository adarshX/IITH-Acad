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
#pix_val_1 = list(set(pix_val))
#print(pix_val)
#print("pix_val = ",pix_val[0])
N = len(pix_val)
#d = 3
k = 30
e  = 0.01 #ephisolon
f = 0  #stopping contdn
#d = []
S = [[] for u in range(k)]
centroid = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(k)]
#print(centroid)
b = N/10;
j = 0
#print(b)
#print(pix_val[b-1])
while f < e :
	for i in range(b):
		d = []
		for l in range(k):
			d.append (distance.euclidean(pix_val[i], centroid[l]))
			#print(d)
			t = np.argmin(d)
			S[t].append(pix_val[i])
print(S)






'''print(d)
h = centroid[0]
print(centroid[0])
f = distance.euclidean(pix_val[b-1],h)
print(f)'''



#pix_val_flat = [x for sets in pix_val for x in sets]
'''
with open('1.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(pix_val_1)
#plt.plot(pix_val_1)
#plt.show()

data = pix_val

plt.imshow(data, interpolation='nearest')
plt.xticks(np.arange(0.0, 2.5, 1), np.arange(0.5, 2, 0.5))
plt.yticks(np.arange(2, -0.5, -1), np.arange(0.5,2,0.5))
plt.show()
'''

