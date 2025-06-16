import matplotlib.pyplot as plt
import numpy as np

def details(tit,xax,yax):
    plt.title(tit)
    plt.xlabel(xax)
    plt.ylabel(yax)
    plt.legend()
    plt.autoscale()
    plt.grid(True, linestyle =':')
    
# subplot margins: left, right, top, bottom, wspace, hspace
a,b,c,d,e,f = 0.1,0.9,0.9,0.05,0.1,0.4

# Charles Law 2atm
fig = plt.figure(figsize = (10, 10)) 

T2atm = [22,100]
V2atm = [0.00001805,0.008205]
P2atm = [202650,202650] # constant pressure

plt.subplot(3,1,1)
plt.plot(T2atm, V2atm, 'b', label = "V2atm = (8.205x10^(-5))T")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V2atm, P2atm, 'b', label = "P2atm = 202650")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T2atm, P2atm, 'b', label = "P2atm = 202650")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

# Charles Law 1atm

fig = plt.figure(figsize = (10, 10)) 

T1atm = [22,100]
V1atm = [0.001805,0.008205] 
P1atm = [101325,101325] # constant pressure

plt.subplot(3,1,1)
plt.plot(T1atm, V1atm, 'b', label = "V2atm = (8.205x10^(-5))T")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V1atm, P1atm, 'b', label = "P2atm = 101325")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T1atm, P1atm, 'b', label = "P2atm = 101325")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

# Amonton's Law 1m^3

fig = plt.figure(figsize = (10, 10)) 

T1m3 = [22,100]
V1m3 = [1,1] # constant Volume
P1m3 = [182.9,831.4]

plt.subplot(3,1,1)
plt.plot(T1m3, V1m3, 'b', label = "V1m3 = 1")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V1m3, P1m3, 'b', label = "V1m3 = 1")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T1m3, P1m3, 'b', label = "P1m3 = (8.314)T")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

# Amonton's Law 0.1m^3

fig = plt.figure(figsize = (10, 10)) 

T01m3 = [22,100]
V01m3 = [0.1,0.1] # constant Volume
P01m3 = [1829,8314]

plt.subplot(3,1,1)
plt.plot(T01m3, V01m3, 'b', label = "V0.1m03 = 1")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V01m3, P01m3, 'b', label = "V0.1m3 = 1")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T01m3, P01m3, 'b', label = "P0.1m3 = (8.314)T")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

plt.show()
