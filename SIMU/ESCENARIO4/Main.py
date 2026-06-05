import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import Funciones
from Funciones import summer1,summer2,summer3,PromInicial, aprox
import json

########################### LIMITES
N=100 #Muestras....
T=20 #Limite temporal
so=10 #LIMITE DE S [0,so]
xo=1 # [0,x0]
########################## VARIABLES
t = sp.Symbol('t')
r = sp.Symbol('r')
y = sp.Symbol('y')
s = sp.Symbol('s')
x = sp.Symbol('x')
v = sp.Symbol('v')
s1=2
########################## FUNCIONES
#expr = sp.exp(-(s+x))/(1-sp.exp(-so))**2     # ojo: usa **, no ^
#(C+De^(-|x-x^*|/d) d=0.1  #-2 soporte en s, -1 soporte en x, 0.5 donde esta sentrada la integral
#expr =sp.Piecewise(
#    (sp.exp(-s)*(1+sp.exp(-(x-0.5)/5))/((5*(1-sp.exp(-(1-0.5)/5))+1+5*(1-sp.exp(-0.5/5)))*(1-sp.exp(-4))), sp.And(s < 4, x>= 0.5)),
#    (0,     s >= 4),
#    (sp.exp(-s)*(1+sp.exp((x-0.5)/5))/((5*(1-sp.exp(-(1-0.5)/5))+1+5*(1-sp.exp(-0.5/5)))*(1-sp.exp(-4))), sp.And(s < 4, x< 0.5)) #0.5 donde esta centrado en x
#)



expr =sp.Piecewise(
    (sp.exp(-s)*(1+sp.exp(-(x-0.5)/5))/((1+5*(2-sp.exp(-0.5/5)-sp.exp(-(1-0.5)/5)))*(1-sp.exp(-4))), sp.And(s < 4, x>= 0.5)),
    (0,     s >= 4),
    (sp.exp(-s)*(1+sp.exp((x-0.5)/5))/((5*(1-sp.exp(-(1-0.5)/5))+1+5*(1-sp.exp(-0.5/5)))*(1-sp.exp(-4))), sp.And(s < 4, x< 0.5)) #0.5 donde esta centrado en x
)
#expr es la condición inicial.
f = sp.lambdify((s,x), expr, "numpy")       # función numérica rápida, para la condición inicial


#expr1 = (sp.exp(r-s))*2/(xo**2)
#expr1 = (sp.exp(r-s))*2*sp.exp(-sp.Abs(x - y))/2
expr1 =sp.Piecewise(
    ((sp.exp(s-r))*x*(1-x), s < r),
    (0,     s >= r)
)
k1 = sp.lambdify((s,r,y,x), expr1, "numpy")  # $ si k=k_1+k_0, donde k_0 es la parte de la frontera. entonces k1 aparece en el forzante
#Sige k_0

expr0 = (1+sp.exp(-r))/2
k0 = sp.lambdify((r,y,x), expr0, "numpy")

expr2 = sp.Piecewise(
    ((1-sp.exp(-s))/(1+sp.exp(-sp.Abs(v-1))), s > 1),
    (0, s <= 1)
)


p = sp.lambdify((v,s), expr2, "numpy") #la taza de salida de u.
#sp.abs(x-y)/d, esto para controlar la fuerza del acoplamiento espacial y e^{-t/10} la temporal
#expr3=(1+sp.sin(t))*sp.exp(-sp.Abs(x-y)/10)*0.5
expr3=(1+sp.sin(t))*sp.exp(-sp.Abs(x-y)/10)*0.5
w = sp.lambdify((t,y,x), expr3, "numpy")# La coneción sinaptica
######################### MALLADO
dt=0.1  #Mallado en t
ds=0.6   #Mallado en s
dx=0.1   #Mallado en x
tn=np.arange(0,T,dt)
sn=np.arange(0,so,ds)
xn=np.arange(0,1.1,dx)
u0=np.zeros((len(sn),len(xn)))

########################### VOLTAJE INICIAL Y FRONTERA

n_periodos = 5  # número de ciclos a lo largo del intervalo [xn[0], xn[-1]]
#v0 = np.sin(2*np.pi*n_periodos * (xn - xn[0])/(xn[-1] - xn[0]))
v0=np.random.randn(len(xn))+10*np.sin(2*np.pi*n_periodos * (xn - xn[0])/(xn[-1] - xn[0]))

############################ Arreglo de condiciones iniciales.
u0=PromInicial(expr,xn,sn,u0,v0,s,x,ds,dx,xo,p,k0)
print(u0)
A,B,Nt=aprox(u0,v0,dt,ds,dx,p,sn,xn,tn,expr1,s,x,w,xo,k0)



########################################
########################################
data = {
    "A": [a.tolist() for a in A],
    "B": [b.tolist() for b in B],
    "Nt": [n.tolist() for n in Nt]
}

with open("datosNoiseX.txt", "w") as f:
    json.dump(data, f)
