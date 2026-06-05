import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import math
#Esto esta sumando la frontera donde k_0=0.5

t = sp.Symbol('t')
r = sp.Symbol('r')
y = sp.Symbol('y')
s = sp.Symbol('s')
x = sp.Symbol('x')
v = sp.Symbol('v')





def summer1(u,v,ds,dx,x,xo,p,sn,k0,xn): #Bounded
    n=0
    for i in range(0,len(v)):
        for j in range(1,len(sn)):
            val = k0(sn[j],xn[i],3)
            n=n+p(v[i],sn[j])*u[j][i]*dx*ds*val
    return float(n)

def summer2(u, v, ds, dx, k, l, sn, expr1, p, xn, s, x):#Force for u
    G=0
    for i in range(0,len(xn)):
        for j in range(1,len(sn)-k):
            k1=np.exp(-sn[k+j])*(np.exp(sn[k+1])-np.exp(sn[k]))
            B=(xn[l+1]**2-xn[l]**2)/2-(xn[l+1]**3-xn[l]**3)/3
            G=G+k1*B*p(v[i],sn[j])*u[j][i]
    return float(G)


def summer3(v,u,dx,xn,t,j,w):#Force for v
    s=0
    for i in range(0,len(u)):
        s=s+w(t,xn[i],xn[j])*v[i]*u[i]*dx
    return float(s)


def PromInicial(expr,xn,sn,u0,v0,s,x,ds,dx,xo,p,k0):
    for i in range(1,len(xn)):
        for j in range(1,len(sn)):
            Ix = sp.integrate(expr, (x, xn[i-1], xn[i]))
            I = sp.integrate(Ix, (s, sn[j-1], sn[j]))
            u0[j-1][i-1]=I
    return u0

def aprox(u0,v0,dt,ds,dx,p,sn,xn,tn,expr1,s,x,w,xo,k0):#Numeric solution.
    Nt=[]
    u=u0[0:-1,0:-1]
    v=v0[0:-1]
    plt.ion()
    fig, (ax_u, ax_v) = plt.subplots(1, 2, figsize=(12, 4))

    im = ax_u.imshow(
        u, origin="lower", aspect="auto",
        extent=[xn[0], xn[-2], sn[0], sn[-1]]
    )
    cb = plt.colorbar(im, ax=ax_u)
    cb.set_label("u(s,x)")
    ax_u.set_xlabel("Spatial position (x)")
    ax_u.set_ylabel("Age/ time since last spike (s)")
    ax_u.set_title("u_n(s,x)")

    (line,) = ax_v.plot(xn[0:-1], v)
    ax_v.set_xlabel("Spatial position (x)")
    ax_v.set_ylabel("Membrane Voltage (mV)")
    ax_v.yaxis.set_label_position("right")
    ax_v.set_title("v_n(x)")
    ax_v.grid(True)

    gif_path = "anim.gif"
    fps = 60  # frames por segundo (ajusta)
    frames = []
    A=[]
    B=[]
    for k in range(1,len(tn)):
        un=u0.copy()
        vn=v0.copy()
        A.append(un)
        B.append(vn)
        Nt.append(un[0])
        
        t_now = tn[k-1]
        u=un[0:-1,0:-1]
        v=vn[0:-1]
###
        # Actualiza u (2D)
        im.set_data(u)
        im.set_clim(float(u.min()), float(u.max()))
        ax_u.set_title(f"u^k(s,x)   t={t_now:.3f}")

        # Actualiza v (1D)
        line.set_data(xn[0:-1], v)
        ax_v.relim()
        ax_v.autoscale_view()


        # Renderiza y captura imagen de la figura completa
        fig.canvas.draw()
        q, h = fig.canvas.get_width_height()
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(h, q, 3)
        frames.append(img)
        for i in range(0,len(xn)-1):
            for j in range(1,len(sn)):
                un[j][i]=u0[j][i]-dt*(u0[j][i]-u0[j-1][i])/ds-p(v0[i],sn[j])*u0[j][i]*dt+summer2(u0,v0,ds,dx,j,i,sn,expr1,p,xn,s,x)*dt
        for i in range(0,len(xn)-1):
            vn[i]=(1-dt)*v0[i]+summer3(v0,un[0],dx,xn,tn[k],i,w)*dt
            un[0][i]=summer1(un,vn,ds,dx,i,xo,p,sn,k0,xn)
            #(u,v,ds,dx,x,xo,p,sn)
    # Avanza en tiempo
        u0 = un
        v0 = vn

    plt.close(fig)

# -------------------------
# Guardar GIF
# -------------------------
    duration_ms = int(round(1000 / fps)) 
    #imageio.mimsave(gif_path, frames, duration=duration_ms)
    imageio.mimsave(gif_path, frames, fps=60)
    print("GIF guardado en:", gif_path)

    
    return A,B,Nt
