import random
import numpy as np
import math
# input matrix "X" --> d*N matrix
X = [(1,2,3),(2,5,6) , (1,6,7) , (1,2,6) , (5,8,9) , (8,9,10) ]
K = 2 # no.of mixtures
d = 3
N = len(X)
pi = math.pi
#assume mean,covaraiance of each mixture.
'''
mean = []
cov = [[[]]]
weight = []
'''
#step1 : Initalisation of mean , weight , covariance matrix of each mixture
mean = [(random.uniform(1,10),random.uniform(1,10) , random.uniform(1,10)) for i in range(K)]
#cov = np.random.rand(K,d,d)
cov =  np.zeros((K,d,d))   							# a diagnol matrix
for i in range(K):
	for j in range(d):
		cov[i][j][j] = random.uniform(1,10)
	 
weight = [random.uniform(0,1) for i in range(K)]
#print(mean)
print(cov)
#print(weight)

#step 2 : compute posterior probability

#step 2(a) : computing probability distirbutions of each GMM
#pdf of N(x,mu,cov) --> f_x --> K * N dimension

def pdf(X,mean,cov):
	pdf_x = [[ 0 for x in range(K)] for y in range(N)]
	for i in range(N):
		for j in range(K):
			a = 0
			det = 1
			for t in range(d):
				p = (X[i][t] - mean[j][t])
				p = p * p
				q =  cov[j][t][t]
				q  = q * q
				r = p/q
				a = a + r 
			a = -0.5 * a
			A = math.exp(a)
			for t in range(d):
				det =  det * cov[j][t][t] * cov[j][t][t]
			b = 2 * pi 
			b = math.pow(b,2) * det
			B = math.sqrt(b)
			pdf_x[i][j] = A / B
	return pdf_x
f_x = pdf(X,mean,cov)
print(f_x)

#step 2(b) : finding weights
m = [] # mixture  indice matrix 
P = [[ 0 for x in range(K)] for y in range(N)]    #probability matrix
for i in range(N):
	D = 0
	for j in range(K):
		d_w = weight[j] * f_x[i][j]
		D = D + d_w
	for j in range(K):
		C =  weight[j] * f_x[i][j]
		P[i][j] = C / D
	#print(P[i])
	t = np.argmax(P[i])
	m.append(t)
#print(m)


#step 3 - update mean,weight ,covar

# 3(a) : finidng N_k
N_k = [0 for x in range(K)]
for j in range(K):
	for i in range(N):
		N_k[j] = N_k[j] + P[i][j] 
#print(N_k)

# 3(b) : finidng mu_k
mu_k = [[0 for x in range(d)]for y in range(K)]

for j in range(K):
	for i in range(N):
		p = [0 for t in range(d)]
		for t in range(d):
			p[t] = P[i][j] * X[i][t]
		for t in range(d):
			mu_k[j][t] = mu_k[j][t] + p[t]
	for t in range(d):
		mu_k[j][t] = mu_k[j][t] / N_k[j]
	mu_k[j] = tuple(mu_k[j])
	#print(mu_k[j])

# 3(c) : finidng cov_k(covar matrix)

cov_k = [[[0 for x in range(d)]for y in range(d)] for z in range(K)]
for j in range(K):
	
	for t in range(d):
		sum = 0
		for i in range(N):
			p = (X[i][t] - mu_k[j][t])
			p = p * p
			p = P[i][j] * p
			sum = sum + p
		cov_k[j][t][t] = sum
	print(cov_k[j])

# 3(d) :  finding updated weights w_k
w_k = [0 for x in range(K)]
for j in range(K):
	w_k[j] = N_k[j]/N

#step 4 : checking convergence 

# 4(a) 
#ln_P = [[ 0 for x in range(K)] for y in range(N)]
S_n = 0 						#"summation of N" intialisation
for i in range(N):
	S_k = 0						#summation of K intialisation
	for j in range(K):
		a = 0
		det = 1
		for t in range(d):
			p = (X[i][t] - mu_k[j][t])
			p = p * p
			q =  cov_k[j][t][t]
			q  = q * q
			r = p/q
			a = a + r 
		a = -0.5 * a
		A = math.exp(a)
		for t in range(d):
		 	det =  det * cov_k[j][t][t] * cov_k[j][t][t]
		b = 2 * pi 
		b = math.pow(b,2) * det
		B = math.sqrt(b)
		P_l = A / B
		P_l = w_k[j] * P_l
		S_k = S_k + P_l
	l = math.log(S_k)
	S_n = S_n + l
print(S_n)
