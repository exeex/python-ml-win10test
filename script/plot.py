import matplotlib.pyplot as plt
import numpy as np

plt.ion()
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')
plt.pause(0)