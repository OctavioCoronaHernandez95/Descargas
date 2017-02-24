import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(3,-3,100)

y=x**2
z=x
w=x**3
plt.plot(x,y,linewidth=3,color= 'r',label= 'parabola')
plt.plot(z,w,linewidth=3,color='g',label='una cubica')

plt.legend()
plt.title('muchas graficas')
plt.xlabel('Algo')
plt.ylabel('una funcion de algo')
plt.grid(True)
plt.show()
plt.savefig('grafica.png')

plt.cla()

x=np.linspace(1,-1,150)

for n in range(1,16):
    y=x**n
    plt.plot(x,y,linewidth=-3)
    nombre="Grafica"+str(n)+".png"
    plt.savefig(nombre)
