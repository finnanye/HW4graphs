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

'''
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
plt.plot(T01m3, V01m3, 'b', label = "V0.1m03 = 0.1")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(V01m3, P01m3, 'b', label = "V0.1m3 = 0.1")
details("V-P","Volume (m^3)","Pressure (Pa)")

plt.subplot(3,1,3)
plt.plot(T01m3, P01m3, 'b', label = "P0.1m3 = (8.314)T")
details("T-P","Temperature (C)","Pressure (Pa)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)'''

# Boyle's Law 295K

fig = plt.figure(figsize = (10, 10)) 
# Vk = [24.23,18.64,14.25,12.12] 
# Pk = [1,1.3,1.7,2]

Pk = [x for x in range(100,200)]
Tk = [295.15]*len(Pk) # constant temp K
Vk = [24.23/x for x in Pk]

print (Pk)
print (Tk)
print (Vk)



plt.subplot(3,1,1)
plt.plot(Tk, Vk, 'b', label = "T = 295.15K")
details("T-V","Temperature (K)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(Vk, Pk, 'b', label = "V = 24.23/P ")
details("V-P","Volume (m^3)","Pressure (atm)")

plt.subplot(3,1,3)
plt.plot(Tk, Pk, 'b', label = "T = 295.15K")
details("T-P","Temperature (K)","Pressure (atm)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

# Boyle's Law 100C

fig = plt.figure(figsize = (10, 10)) 

Tc = [100,100] # constant temp C
Vc = [0.004103,0.008205] 
Pc = [101325,202650]

plt.subplot(3,1,1)
plt.plot(Tc, Vc, 'b', label = "T = 100 C")
details("T-V","Temperature (C)","Volume (m^3)")

plt.subplot(3,1,2)
plt.plot(Vc, Pc, 'b', label = "V = 831.4/P ")
details("V-P","Volume (m^3)","Pressure (atm)")

plt.subplot(3,1,3)
plt.plot(Tc, Pc, 'b', label = "T = 100 C")
details("T-P","Temperature (C)","Pressure (atm)")

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)

plt.show()
