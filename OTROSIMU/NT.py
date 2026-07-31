import os
import json
import numpy as np
from numpy.fft import fft, fftfreq
import pandas as pd
###################
import matplotlib.pyplot as plt

ruta = "."

datos_totales = []
T=20 #Limite temporal
dx=0.1
dt=0.1
ds=0.6
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
        #for p in [1,3,6,10]:
        #    if str(p) in archivo:
        #        name=p
        #plt.plot(tn,N,label=r"$d$="+str("name"))
        plt.plot(tn,N)
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
        X = fft(N)
        f = np.fft.fftfreq(len(N), d=1/dt)
        mask = f >= 0

        f = f[mask]
        X = X[mask]
        PSD = (np.abs(X)**2)/(len(N)*dt)
        #for p in [1,3,6,10]:
        #    if str(p) in archivo:
        #        name=p
        #plt.plot(f,PSD,label="PSD "+r"$d$="+str("name"))
        plt.plot(f,PSD,label="PSD ")
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

###############################
################################
###################################

for archivo in os.listdir(ruta):
    if archivo.endswith(".txt"):
        with open(archivo, "r") as f:
            data = json.load(f)
        
        A = [np.array(a) for a in data["A"]]
        B = [np.array(b) for b in data["B"]]
        Nt = [np.array(n) for n in data["Nt"]]
        xn=[]
        N=[]
        x=0
        for k in range(0,len(Nt[0])-1):
            s=Nt[len(Nt)-1][k]
            N.append(s)
            xn.append(x)
            x=x+dx
        print(len(N),len(tn))    
        #for p in [1,3,6,10]:
        #    if str(p) in archivo:
        #        name=p
        #plt.plot(tn,N,label=r"$d$="+str("name"))
        plt.plot(xn,N)
        plt.title("firing activity N(20)")
       
        #datos_totales.append({
        #    "archivo": archivo,
        #    "A": A,
        #    "B": B,
        #    "Nt": Nt
        #})
        
plt.xlabel("x")
plt.ylabel("N(20,x)")
plt.legend(loc="upper left")
plt.savefig("graficaN20.png")  # guarda la imagen
plt.show()
plt.close()

########################Conservación de masa.
MM = []

archivos = []

for archivo in os.listdir(ruta):
    if archivo.endswith(".txt"):
        with open(os.path.join(ruta, archivo), "r") as f:
            data = json.load(f)

        A = [np.array(a) for a in data["A"]]

        for n in range(len(A)):
            Un = A[n]
            M = 0.0

            for i in range(1,len(Un)):          # dirección s
                for j in range(0,len(Un[i])):   # dirección x
                    M += Un[i][j] * dx * ds

            MM.append(M)
            archivos.append(archivo)

# Crear DataFrame
df = pd.DataFrame({
    "Archivo": archivos,
    "Masa": MM
})

# Guardar en Excel
df.to_excel("MM.xlsx", index=False)

print(df)
                    




