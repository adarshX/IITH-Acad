#Basic Autoencoder(Vanilla)
#The dataset used here is "MNIST"
# The framework : 1 input layer , i hidden layer , 1 ouptut layer

from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt



def sigmoid_function(x):
	f = 1 / (1 + math.exp(-x))
	return f 

n_epoch = 60  #no.of epochs

(x_train, _), (x_test, _) = mnist.load_data()    #loading data from mnist
x_train = x_train.astype('float32') / 255.       #normalising values to range of 0 and 1
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))


dimension_encod = 32  
imageInput = Input(shape=(784,))    #input image


encoded = Dense(dimension_encod, activation='relu')(imageInput)
decoded = Dense(784, activation='sigmoid')(encoded)  #sigmoid function is used


autoencoder = Model(imageInput, decoded)

encoder = Model(imageInput, encoded)  #encoder model


 
encoded_input = Input(shape=(dimension_encod,))
decoder_layer = autoencoder.layers[-1]
decoder = Model(encoded_input, decoder_layer(encoded_input))  #decoder model


autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy') #loss

autoencoder.fit(x_train, x_train,epochs=60,batch_size=256,shuffle=True,validation_data=(x_test, x_test))


encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)



n = 20  # no.of digits 
plt.figure(figsize=(25, 4))
plt.title('Input and predicted images',  loc='center',)
for i in range(n):
    
    ax = plt.subplot(2, n, i + 1) # original images
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28)) # output images
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
