import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k=1.0
R=20000.0
C=math.exp(10,-6)
tau=R*C

#RC ckt eqn: RC(dVc/dt)=-Vc+V
#Take V=x(input), k=arbitraty constant(here 1)

def model(y,t):
    x=1
    return (-y+k*x)/tau

t=np.linspace(0,14,100)
y=odeint(model,0,t)

plt.figure(1)
plt.plot(t,y,r-)
plt.xlabel('Time')
plt.ylabel('Response(y)')

plt.show()
