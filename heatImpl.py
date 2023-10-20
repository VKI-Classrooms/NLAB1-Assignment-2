import time
from math import pi
import numpy as np
from scipy.sparse import diags, linalg

import matplotlib.pyplot as plt

def heat(N: int, T: float) -> float:
    # grid
    h = 1./N
    x = np.arange(0,1+h,h)

    # initial conditions
    u = np.sin(pi*x)
    #plt.plot(x,u)
    #plt.show()

    # set up time stepping
    a = 1.
    lam = 0.5 # lam = a*tau/h**2
    tau = lam*h**2/a

    M = int(np.ceil(T/tau))
    tau = T/M
    lam = a*tau/h**2

    # indexing
    I = np.arange(1,N)
    Im = I-1
    Ip = I+1

    A_h = diags([-lam, 1+2*lam, -lam], [-1,0,1],shape=(N-1,N-1))
    LUsolve = linalg.factorized(A_h.tocsc())
    
    
    # iteration
    for _ in range(M):
        u[I] = LUsolve(u[I])
        #plt.plot(x,u)
        #plt.pause(.1)

    ue = np.exp(-a*pi**2*T)*np.sin(pi*x)
    return max(abs(u-ue))


if __name__ == '__main__':
    NN = [10,100,1000]
    tic = time.perf_counter()
    err = [heat(N=n,T=0.2) for n in NN]
    toc = time.perf_counter()
    print(f"Time: {toc-tic}")
    print(err)

    plt.loglog(NN,err)
    plt.xlabel("N")
    plt.ylabel(r"$|u-u_e|$")
    plt.show()
