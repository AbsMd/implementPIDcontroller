import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def main():
    kp=2.0
    tau=1.0
    zeta=0.25
    dx=1.0

    #second order differential eqn: tau^2(d^2y/dt^2)+ 2*zeta*tau(dy/dt)=-y+Kp(x)
    def model(x,t):
        y = x[0]
        dy_dt = x[1]
        d2y_dt2 = (-2.0*zeta*tau*dy_dt - y + kp*dx)/tau**2
        return [dy_dt,d2y_dt2]
    t = np.linspace(0,25,100)
    u = odeint(model,[0,0],t)
    y = u[:,0]

    plt.figure(1)
    plt.plot(t,y,'r-',linewidth=1,label='ODE Integrator')
    plt.xlabel('Time')
    plt.ylabel('Response (y)')
    plt.legend()
    plt.show()

main()
