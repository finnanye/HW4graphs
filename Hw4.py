import matplotlib.pyplot as plt
import numpy as np

def details(titl,xax,yax):
    plt.title(titl)  
    plt.xlabel(xax)
    plt.ylabel(yax)
    plt.legend()
    plt.autoscale()
    plt.grid(True, linestyle =':')

def boyleslaw(P=1, K=True):
    if K:
        print ("boyles law, K ",24.23/P,P)
        return np.divide(24.23,P)
    else:
        print ("boyles law, C ",24.23/P)
        return np.divide(831.4,P)



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

plt.subplots_adjust(left=a, right=b,top=c, bottom=d, wspace=e, hspace=f)
'''
# Boyle's Law 295K

fig = plt.figure(figsize = (10, 10)) 

Tk = [295.15,295.15] # constant temp K
Pk = [1,2]
Vk = Pk.copy()
for i in range (len(Pk)):
    Vk[i] = boyleslaw(Pk[i])


plt.subplot(3,1,1)
print(Tk, Vk)
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
'''
fig = plt.figure(figsize = (10, 10)) 

Tc = np.arange(float(100),float(100)) # constant temp C
Vc = np.arange(0.004103,0.008205)
Pc = np.arange(101325,202650)

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
'''

# Adiabetic expansion/compression

fig = plt.figure(figsize = (10, 10)) 

PAd = [x*0.01 for x in range(100,201)]
VAd = [86.6*x**(-5/7) for x in PAd]

plt.plot(PAd, VAd, 'b', label = "P = 86.6V^(-5/7)")
details("P-V","Pressure (atm)","Volume (m^3)")

# add isotherm
fig = plt.figure(figsize = (10, 10)) 

plt.plot(PAd, VAd, 'b', label = "P = 86.6V^(-5/7)")
plt.plot(Pk, Vk, 'r', label = "P = 24.23V")
details("P-V","Pressure (atm)","Volume (m^3)")

# Work Cycle

fig = plt.figure(figsize = (10,10))

# Process 1
Vol1 = [V*0.000009 for V in range (100,223)] # Obtain 122 Volume values between 0.0009 and 0.002
Press1 = [189.9/V for V in Vol1] # Calculate initial Pressure

plt.plot(Vol1,Press1,'r', label = "P1 = 182.9*V1^(-1)")
details("V-P","Volume (m^3)","Pressure (atm)")




plt.show()
