# XOR gate
# 2 input nodes , 2 hidden nodes , 1 output node
#input nodes numbering = 1,2
#hidden nodes numbering = 1,2
#ouput nodes numbering = 1

import numpy as np
import math

x = [(0,0),(1,0),(0,1),(1,1)]  #input array
N = 4
y = [0,1,1,0]                      #expected_output  array



def sigmoid(x):
	f = 1 / (1 + math.exp(-x))
	return f 

def der_sigmoid(x):
	g = sigmoid(x) * (1 - sigmoid(x))      # g = f'(x)
	return g


#weights(w_ij) of with hidden node(i) input node(j) 
w = [(1,2),(3,4)]   #random weights where w = [(w11,w12) , (w21  ,w22)]

b = [-1 ,-2]#biases of hidden nodes  b = [ b1, b2]

#weights(wo_ij) of ouput node(i) with hidden node(j)
wo = [5,6]  # wo = [wo_11,wo_12]

#biases of ouput nodes
bo_1 = 8

#sums at input-hidden nodes
sum1 = [np.zeros(2) for i in range(N)] 	#sum1 = [(0,0) for i in range(N)]
for i in range(N):
	sum1[i] = np.dot(w,x[i]) 
	sum1[i] = sum1[i] + b
	sum1[i] = list(sum1[i])
print(sum1)


#values at hidden nodes
z = [np.zeros(2) for i in range(N)]
for j in range(2):
	for i in range(N):
		z[i][j] = sigmoid(sum1[i][j])
#z = list(z) 
print(z)


#sums at hidden-output nodes 
sum2 = [0 for i in range(N)] 	
for i in range(N):
	sum2[i] = np.dot(wo,z[i]) 
	sum2[i] = sum2[i] + bo_1
print(sum2)

#values at hidden nodes
y_p = [0 for i in range(N)] 	
for i in range(N):
	y_p[i] = sigmoid(sum2[i])
print(y_p)


#squared error for each input
error = [0 for i in range(N)] 	
for i in range(N):
	error[i] = y[i] - y_p[i]        #R(i) = error[i]
	error[i] = np.square(error[i])
#error = error * 100
print(error)

#cumulative error for all N inputs
cum_error = sum(error)
print(cum_error)




gamma = 0.5 #learning rate

#updating weights

#1) updating 'wo' weights (hidden-output) : 
#one  update is enough because no.of ouput nodes = 1
# diff w.r.t wo_11 of R(i) =   diff w.r.t wo_12 of R(i) 

# diff of error of ith input w.r.t weight(wo_11)
print('------')
db_R = [0 for i in range(N)] 	
for i in range(N):
	c1 = y[i] - y_p[i]
	c2 = der_sigmoid(sum2[i])
	db_R[i]  = 2 * c1 * c2
print(db_R)
s_db = sum(db_R)
print(s_db)


wo_new = [0 for i in range(2)] 
for i in range(2):
	p1 = gamma * s_db
	wo_new[i] = wo[i] - p1

print(wo_new)



print('____')


#2) updating 'w' weights (input -hidden) : 
# all 4  updates are req i.e, w.r.t each w
t11 = [0 , 0, 0 ,0]
t12 = [0 , 0, 0 ,0]
t21 = [0 , 0, 0 ,0]
t22 = [0 , 0, 0 ,0]
for i in range (N):
	a1 = y[i] - y_p[i]
	a2 = der_sigmoid(sum2[i])		
	a31 = der_sigmoid(sum1[i][0])
	a32 = der_sigmoid(sum1[i][1])
	t11[i] =  2 * a1 * a2 * wo[0] * a31 * x[i][0]   #alpha11 -- w11
	t12[i] =  2 * a1 * a2 * wo[0] * a31 * x[i][1]	#alpha12 -- w12
	t21[i] =  2 * a1 * a2 * wo[1] * a32 * x[i][0]	#alpha21 -- w21
	t22[i] =  2 * a1 * a2 * wo[1] * a32 * x[i][1]	#alpha22 -- w22

da_R = [[t11,t12],[t21,t22]]
#print(da_R)
s_da = [np.zeros(2) for i in range(2)]
s_da[0][0] = t11[0] + t11[1] + t11[2] + t11[3]
s_da[0][1] = t12[0] + t12[1] + t12[2] + t12[3]
s_da[1][0] = t21[0] + t21[1] + t21[2] + t21[3]
s_da[1][1] = t22[0] + t22[1] + t22[2] + t22[3]

print(s_da)


w_new = [np.zeros(2) for i in range(2)] 
for i in range(2):
	for j in range(2):
		p2 = gamma * s_da[i][j]
		w_new[i][j] = w[i][j] - p2

print(w_new)

