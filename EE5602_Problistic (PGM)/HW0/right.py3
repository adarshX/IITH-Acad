import numpy as np 
from  scipy import misc
import matplotlib.pyplot as plt 
from PIL import Image


Im_right = Image.open('HW0-right-gray.png', 'r')
pix_val_right = list(Im_right.getdata())
set(pix_val_right)
pix_val_right = list(set(pix_val_right))
#print(pix_val_right)

N_right = len(pix_val_right)
#print(N_right)
plt.imshow(Im_right)
plt.show()
