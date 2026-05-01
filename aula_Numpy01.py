import numpy as np
import matplotlib.pyplot as plt

# criando um array numpy
vector = np.array([3,4,0,10,30,50])
print(vector)
plt.plot(vector, linestyle = "--")
plt.grid()
plt.show()

#criando uma lista
lista = [20,30,2,11,5,70,50]
print(lista)
dobro_lista = [lista*2 for i in lista]
print(dobro_lista)
dobro_array = vector*2
print(dobro_array)