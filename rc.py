import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k=1.0
R=2
C=5
tau=R*C

#RC ckt eqn: RC(dVc/dt)=-Vc+V
def dVc_dt(Vc,t):
    V=2
    return (-Vc+k*V)/tau

t=np.linspace(0,50,100)
Vc=odeint(dVc_dt,0,t)

plt.figure(1)
plt.plot(t,y,'r-', linewidth=2.0, label='k=1.0, V=2')
plt.xlabel('Time')
plt.ylabel('Response(y)')
plt.xlim(right=50)
plt.ylim(top=5)

plt.legend()
plt.show()
