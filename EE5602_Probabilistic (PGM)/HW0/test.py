import numpy as np
from scipy import signal
import matplotlib.image as mpimg
 
def gaussian_kernel(k, s = 0.5):
    # generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma = s
    probs = [exp(-z*z/(2*s*s))/sqrt(2*pi*s*s) for z in range(-k,k+1)]
return np.outer(probs, probs)
 
def create_graph(imfile, k=1., sigma=0.8, sz=1):
    # create the pixel graph with edge weights as dissimilarities
     rgb = mpimg.imread(imfile)[:,:,:3]
     gauss_kernel = gaussian_kernel(sz, sigma)
     for i in range(3):
         rgb[:,:,i] = signal.convolve2d(rgb[:,:,i], gauss_kernel, boundary='symm', mode='same')
     yuv = rgb2yiq(rgb)
     (w, h) = yuv.shape[:2]
     edges = {}
     for i in range(yuv.shape[0]):
         for j in range(yuv.shape[1]):
             #compute edge weight for nbd pixel nodes for the node i,j
             for i1 in range(i-1, i+2):
                 for j1 in range(j-1, j+2):
                     if i1 == i and j1 == j: continue
 
                     if i1 >= 0 and i1 = 0 and j1 < h:
                        wt = np.abs(yuv[i,j,0]-yuv[i1,j1,0])
                        n1, n2 = ij2id(i,j,w,h), ij2id(i1,j1,w,h)
                        edges[n1, n2] = edges[n2, n1] = wt
     return edges