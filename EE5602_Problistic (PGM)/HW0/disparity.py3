import numpy as np 
from  scipy import misc
import matplotlib.pyplot as plt 
from PIL import Image
#import sklearn.feature_extraction.image
import math

Im_left = Image.open('HW0-left-gray.png', 'r')
pix_val_left = (Im_left.getdata())
#set(pix_val_left)
#pix_val_left = list(set(pix_val_left))
#print(pix_val_left)
#plt.imshow(Im_left)
#plt.show()
#print("--------------")
N_left = len(pix_val_left)
#print(N_left)


Im_right = Image.open('HW0-right-gray.png', 'r')
pix_val_right = (Im_right.getdata())
#set(pix_val_right)
#pix_val_right = list(set(pix_val_right))
#print(pix_val_right)

N_right = len(pix_val_right)
#print(N_right)
#plt.imshow(Im_right)
#plt.show()

Diff = [(0,0,0) for i in range(N_left)]
for i in range(N_left):
	Diff[i] = np.subtract(pix_val_left[i] , pix_val_right[i])
#print("--------------")
#print(Diff)

'''
Im_left = Image.open('HW0-left-gray.png', 'r')
pix_val_left = Im_left.getdata()
#Im_left = 'HW0-left-gray.png'
graph_left = sklearn.feature_extraction.image.img_to_graph(pix_val_left)

print(graph_left)
plt.plot(graph_left)
plt.show()



'''
disp = [0 for i in range(N_left)]
#t = [1 for i in range(N_left)]
sigma = 1
phi =  [0 for i in range(N_left)]

#def compatibility(disp):

for i in range(N_left - 5):
	t = pix_val_left[i][1] - pix_val_right[i ][1]
	phi[i] =  10 * math.exp((- 1 / (2 * pow(sigma,2)   )) * pow(t,2))
print(phi)




