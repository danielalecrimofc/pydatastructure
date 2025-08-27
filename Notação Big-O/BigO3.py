"""
1 Constant
log(n) Logarithmic
n Linear
nlog(n) Log Linear
n^2 Quadratic
n^3 Cubic
2^n Exponential

"""

from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,10,100)

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape),np.log(n),n,n * np.log(n),n**2,n**3,2**n]

#Eixo x range
plt.figure(figsize=(10,8))
#Eixo y limite range
plt.ylim(0, 100)
#Criação do gráfico do primeiro caso big o [constante]
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
# Label para o eixo y
plt.ylabel('Runtime')
# Label para o eixo x
plt.xlabel('n')

# Comando para exibir o gráfico na tela
plt.show()