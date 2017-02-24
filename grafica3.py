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

plt.subplot(2,4,6)
plt.plot([1,2,3,1],[2,7,4,2],linewidth=4, color='b')
plt.subplot(2,4,3)
plt.plot(5,6,'*r',markersize=10)
plt.show()
