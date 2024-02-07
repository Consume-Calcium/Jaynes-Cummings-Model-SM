import numpy as np
import matplotlib.pyplot as plt
import math

ave_n = 10
max_n = 20

n_values = np.arange(0,max_n+1)

Pn = (ave_n**n_values / np.array([math.factorial(n) for n in n_values])) * np.exp(-ave_n)

plt.plot(n_values, Pn, 'or')
plt.ylabel('Probability')
plt.xlabel('Number of photons')
plt.xticks(n_values)
plt.show()