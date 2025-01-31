from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,10,100)

# print (n)

labels = ['Constante','Log','Linear','Log Linear','Quadrático','Cúbico','Exponencial']
big_O = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_O)):
    plt.plot(n, big_O[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()
