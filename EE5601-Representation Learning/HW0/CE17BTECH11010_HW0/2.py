#program to perform PCA on 2D dataset

import numpy as np
import pylab as pl
from scipy import linalg

score = 0
def princomp(A,numpc=0):
	global score
	M = (A-np.mean(A.T,axis=1)).T # subtract the mean (along columns)
	[latent,coeff] = linalg.eig( np.cov(M))
	score = np.dot(coeff.T,M)
	return coeff, score, latent

A = np.array([ [2.45,0.75,2.95,2.27,3.05,2.77,1.6,1.1,1.6,0.9],
            [2.56,0.56,2.25,1.9,3.17,2.36,2,1,1.5,1.1] ])

coeff, score, latent = princomp(A.T)

pl.figure()
pl.subplot(121)
# every eigenvector describe the direction
# of a principal component.
m = np.mean(A,axis=1)
pl.plot([0, -coeff[0,0]*2]+m[0], [0, -coeff[0,1]*2]+m[1],'--k')
pl.plot([0, coeff[1,0]*2]+m[0], [0, coeff[1,1]*2]+m[1],'--k')
pl.plot(A[0,:],A[1,:],'ob') # the data
pl.axis('equal')
pl.subplot(122)
# new data
pl.plot(score[0,:],score[1,:],'*g')
pl.axis('equal')
pl.show()



