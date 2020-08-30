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
#print(pix_val)
#print("pix_val = ",pix_val[0])
N = len(pix_val)
#d = 3
k = 10
e  = 0.1  #ephisolon
f = 0 #stopping contdn
#d = []
S = [[] for u in range(k)]
centroid = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(k)]
print(centroid)
b = N/1000;
j = 0
U = [[]for v in range(j+1)]
NK = []
x_1 = []
x_2 = []
x_3 = []
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
	for h in range(k):
		n_k = len( S[h] )
		for r in range(n_k):
			x_1.append(S[h][r][0])
			x_2.append(S[h][r][1])
			x_3.append(S[h][r][2])
		#print(n_k)
		if(n_k != 0 ):
			u_1 = sum(x_1) / n_k
			u_2 = sum(x_2) / n_k
			u_3 = sum(x_3) / n_k
			u = (u_1,u_2,u_3)                #add if  n_k = 0 case
			U.append(u)
		NK.append(n_k)
	#j = j + 1
	f = f + 1                 #change this condntn for final answer 
	#f = U[j][k] - 
print(NK)
for i in range(k):
	print(S[i])
print(U)
