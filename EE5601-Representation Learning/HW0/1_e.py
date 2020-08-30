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
#set(pix_val)
#pix_val_1 = list(set(pix_val))
#print(pix_val)
#print("pix_val = ",pix_val[0])
#pix_val = [(25,75,255),(255,167,180),(200,50,89),(167,97,12),(35,56,87),(12,34,56)]
N = len(pix_val)
#print(pix_val)
#d = 3
k = 10
e  = 0.1  #ephisolon
E = 0  #error -- > stopping contdn
j = 1
#d = []
S = [[] for u in range(k)]
#centroid = [[[] for v in range(k)] for u in range(j+1)]
centroid = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(k)]
#centroid(jth iteration)(kth cluster)
#centroid = [(241, 133, 61), (231, 70, 100), (9, 158, 43)]

print(centroid)
b = N/10;

#U = [[]for v in range(j+1)]
NK = []
x_1 = []
x_2 = []
x_3 = []
#print(b)
#print(pix_val[b-1])
while E < e :
	U = [] #cntroids of presnt iteration
	E_S = [] #error sum 
	for i in range(b):
		d = []
		for l in range(k):
			d.append (distance.euclidean(pix_val[i], centroid[l]))
			#print(d)
		t = d.index(min(d))
		S[t].append(pix_val[i])
	for h in range(k):
		n_k = len( S[h] )
		if(n_k > 1):
			for r in range(n_k):
				x_1.append(S[h][r][0])
				x_2.append(S[h][r][1])
				x_3.append(S[h][r][2])
			u_1 = sum(x_1) / n_k
			u_2 = sum(x_2) / n_k
			u_3 = sum(x_3) / n_k
			u = (u_1,u_2,u_3)                #add if  n_k = 0 case
			U.append(u)
		if(n_k == 1):
			u = (S[h][0])
			U.append(u)
		NK.append(n_k)
	print(U)
	#j = j + 1
	for l in range(k):
		f = distance.euclidean(U[l],centroid[l])#change this condntn for final answer
		E_S.append(f)
		#f = U[j][k]-
	print(E_S) 
	E = sum(E_S)  #error of each iteration
	print(E)
