#HMM's for phenome's 'a' and 'e'

import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import random as r

#reading audio files
files = 3
rate = [0 for i in range(files)]
sig = [0 for i in range(files)]
file = [ 0 for i in range(files)]
file[0] = "./a/a-srm-1.wav"
file[1] = "./a/a-srm-2.wav"
file[2]= "./a/a-srm-3.wav"

for i in range(files):
	(rate[i],sig[i]) = wav.read(file[i])
	#print(rate[i])
	#print(sig[i])

#print(len(sig[0]))


#extracting MFCC 
mfcc_array  = [0 for i in range(files)]
for i in range(files):
	mfcc_array[i] = mfcc(sig[i],rate[i])
print(mfcc_array[0][0])
print(len(mfcc_array[i]))


#note : MFCC values are observables --> MFCC - 13 * 99 

#intialiastion

# N states , x- emission , z - mfcc

N = len(mfcc_array[i][0])
Pi = [0 for i in range(N)]   #initial state distribution
b = [r.random() for i in range(N)]
alpha = [0 for i in range(N)]	#forward probability

for j in range(N):
	Pi[j] = 1
	alpha[j] = Pi[j] * b[j] * mfcc_array[0][0][j]

#print(alpha)




# emission probability --> gaussian

