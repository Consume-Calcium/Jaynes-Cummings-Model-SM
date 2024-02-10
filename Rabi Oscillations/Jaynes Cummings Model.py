import numpy as np
import matplotlib.pyplot as plt

ce0 = 1
cg0 = 0

n = 10
delta = 0
lam = 1

t = np.linspace(0, 1, 1000)
lamn = np.sqrt((delta/2)**2 + lam**2*n)

cet = np.exp(-1j*delta*t/2)*((np.cos(lamn*t) + 1j*delta/(2*lamn)*np.sin(lamn*t))*ce0 - 1j*lam*np.sqrt(n)/lamn*np.sin(lamn*t)*cg0)
cgt = np.exp(1j*delta*t/2)*(- 1j*lam*np.sqrt(n)/lamn*np.sin(lamn*t)*ce0 + (np.cos(lamn*t) - 1j*delta/(2*lamn)*np.sin(lamn*t))*cg0)

Pe = np.abs(cet)**2
Pg = np.abs(cgt)**2

plt.grid()
plt.plot(t, Pe, label = 'excited', color = 'orange')
plt.plot(t, Pg, label = 'ground', color = 'blue')
plt.ylabel('Probability')
plt.xlabel('Time')
plt.legend()
plt.show()
