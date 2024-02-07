import numpy as np
import matplotlib.pyplot as plt
import math

ave_n = 20 #average n
max_n = 1000 #n that the sum goes up to
lam = 1

t = np.linspace(0, 50, 1000)

terms = np.zeros(max_n)
Pe = np.zeros_like(t)

for i in range(len(terms)):
    term_i = ((ave_n**i / math.factorial(i))**(1/2) * np.exp(-ave_n/2) * np.sin(lam*np.sqrt(i)*t))**2
    Pe += term_i

plt.plot(t, Pe, label = 'excited', color = 'orange')
plt.ylabel('Probability')
plt.xlabel('Time')
plt.legend()
plt.show()