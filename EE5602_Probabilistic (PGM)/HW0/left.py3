import numpy as np 
from  scipy import misc
import matplotlib.pyplot as plt 
from PIL import Image


Im_left = Image.open('HW0-left-gray.png', 'r')
pix_val_left = list(Im_left.getdata())
set(pix_val_left)
pix_val_left = list(set(pix_val_left))
#print(pix_val_left)
plt.imshow(Im_left)
plt.show()