import os
import json
import numpy as np
from numpy.fft import fft, fftfreq
###################
import matplotlib.pyplot as plt

ruta = "."

datos_totales = []
T=10 #Limite temporal
dx=0.1
dt=0.2
ds=1
plt.figure()

for archivo in os.listdir(ruta):
    if archivo.endswith(".txt"):
        with open(archivo, "r") as f:
            data = json.load(f)
        
        A = [np.array(a) for a in data["A"]]
        B = [np.array(b) for b in data["B"]]
        Nt = [np.array(n) for n in data["Nt"]]
        tn=[]
        N=[]
        t=0
        for i in range(0,len(Nt)):
            s=0
            for k in range(0,len(Nt[0])):
                s=s+Nt[i][k]*dx
            N.append(s)
            tn.append(t)
            t=t+dt
        print(len(N),len(tn))    
        for p in ["1","2","e1"]:
            if str(p) in archivo:
                if p=="1":
                    name="Refractory is 1"
                if p=="2":
                    name="Refractory is 2"
                if p=="e1":
                    name="Refractory is 0.1"
        plt.plot(tn,N,label=r"$d$="+str(name))
        plt.title("Mean firing activity N(t)")
       
        #datos_totales.append({
        #    "archivo": archivo,
        #    "A": A,
        #    "B": B,
        #    "Nt": Nt
        #})
plt.xlabel("t")
plt.ylabel("N(t)")
plt.legend(loc="upper left")
plt.savefig("graficaNT.png")  # guarda la imagen
plt.show()
plt.close()






plt.figure()

for archivo in os.listdir(ruta):
    if archivo.endswith(".txt"):
        with open(archivo, "r") as f:
            data = json.load(f)
        
        A = [np.array(a) for a in data["A"]]
        B = [np.array(b) for b in data["B"]]
        Nt = [np.array(n) for n in data["Nt"]]
        tn=[]
        N=[]
        t=0
        for i in range(0,len(Nt)):
            s=0
            for k in range(0,len(Nt[0])):
                s=s+Nt[i][k]*dx
            N.append(s)
            tn.append(t)
            t=t+dt
        X = fft(N).real
        f = np.fft.fftfreq(len(N), d=1/dt)
        mask = f >= 0

        f = f[mask]
        X = X[mask]
        PSD = (np.abs(X)**2)/len(N)
        for p in ["1","2","e1"]:
            if str(p) in archivo:
                if p=="1":
                    name="Refractory is 1"
                if p=="2":
                    name="Refractory is 2"
                if p=="e1":
                    name="Refractory is 0.1"
        plt.plot(f,PSD,label="PSD "+r"$d$="+str(name))
        plt.title("Normalized Power Spectral Density of Mean firing activity)")
       
        #datos_totales.append({
        #    "archivo": archivo,
        #    "A": A,
        #    "B": B,
        #    "Nt": Nt
        #})
plt.xlabel("t")
plt.ylabel("PSD N(t)")
plt.legend(loc="upper left")
plt.savefig("graficaFFT.png")  # guarda la imagen
plt.show()
plt.close() 


