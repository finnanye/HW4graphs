import matplotlib.pyplot as plt
import numpy as np

def details(tit,xax,yax):
    plt.title(tit)
    plt.xlabel(xax)
    plt.ylabel(yax)
    plt.legend()
    plt.autoscale()
    plt.grid(True, linestyle =':')
    
# Charles Law 2atm
fig = plt.figure(figsize = (10, 10)) 

T2atm = [22,100]
V2atm = [0.00001805,0.008205]
P2atm = [202650,202650]

plt.subplot(3,1,1)
plt.plot(T2atm, V2atm, 'b', label = "V2atm = (8.205x10^(-5))T")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V2atm, P2atm, 'b', label = "P2atm = 202650")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T2atm, P2atm, 'b', label = "P2atm = 202650")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=0.1, right=0.9,top=0.9, bottom=0.005, wspace=0.4, hspace=0.4)

# Charles Law 1atm

fig = plt.figure(figsize = (10, 10)) 

T1atm = [22,100]
V1atm = [0.001805,0.008205]
P1atm = [101325,101325]

plt.subplot(3,1,1)
plt.plot(T1atm, V1atm, 'b', label = "V2atm = (8.205x10^(-5))T")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V1atm, P1atm, 'b', label = "P2atm = 101325")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T1atm, P1atm, 'b', label = "P2atm = 101325")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.005, wspace=0.4, hspace=0.4)

plt.show()
