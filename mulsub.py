import matplotlib.pyplot as plt 
import numpy as np 

x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(3,3,1)
plt.plot(x1,y1,'o-')
plt.title('a table of 2 subplots')
plt.ylabel('damped os cillation')

plt.subplot(3,3,5)
plt.plot(x2,y2,'.-')
plt.xlabel('time(s)')
plt.ylabel('undamped')

plt.show()