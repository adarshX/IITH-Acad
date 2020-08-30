import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
A = 10
T = 0.2
t = np.linspace(-2.5*T,2.5*T, 10000)
plt.plot(t,A/2*(1+signal.square(2*np.pi*t/T,0.5)))
plt.grid()
plt.xlabel('t (in ms)')
plt.ylabel('X(t)')
plt.show()
