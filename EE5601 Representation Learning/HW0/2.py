#from numpy import mean,cov,cumsum,dot,linalg,size,flipud
#from pylab import imread,subplot,imshow,title,gray,figure,show,NullLocator

import numpy as np
import pylab as pl
from scipy import linalg
# computing eigenvalues and eigenvectors of covariance matrix

score = 0
def princomp(A,numpc=0):
	global score
	M = (A-np.mean(A.T,axis=1)).T # subtract the mean (along columns)
	[latent,coeff] = linalg.eig( np.cov(M))
	p = np.size(coeff,axis=1)
	idx = np.argsort(latent) # sorting the eigenvalues
	idx = idx[::-1]       # in ascending order
	# sorting eigenvectors according to the sorted eigenvalues
	coeff = coeff[:,idx]
	latent = latent[idx] # sorting eigenvalues
	if numpc < p and numpc >= 0:
		coeff = coeff[:,range(numpc)] # cutting some PCs if needed
		score = np.dot(coeff.T,M) # projection of the data in the new space
	return coeff, score, latent




#from pylab import imread,subplot,imshow,title,gray,figure,show,NullLocator
A = pl.imread('dog.jpg') # load an image
A = np.mean(A,2) # to get a 2-D array
full_pc = np.size(A,axis=1) # numbers of all the principal components
i = 1
dist = []
for numpc in range(0,full_pc+10,10): 
	coeff, score, latent = princomp(A,numpc)
	Ar = np.dot(coeff,score).T + np.mean(A,axis=0) # image reconstruction
	# difference in Frobenius norm
	dist.append(linalg.norm(A-Ar,'fro'))
	# showing the pics reconstructed with less than 50 PCs
	if numpc <= 25:
		ax = pl.subplot(2,3,i,frame_on=False)
		ax.xaxis.set_major_locator(pl.NullLocator()) # remove ticks
		ax.yaxis.set_major_locator(pl.NullLocator())
		i += 1 
		pl.imshow(pl.flipud(A))
		pl.title('PCs # '+str(numpc))     #--------> change
		pl.gray()

figure()
imshow(flipud(A))
title('numpc FULL')
gray()
show()