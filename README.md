# NLAB1-Assignment-2

Consider the following initial-boundary-value problem for the heat equation:
```math
\begin{align}
	\frac{\partial u}{\partial t} &= a\frac{\partial^2 u}{\partial x^2},&& \mathrm{in}\ (0,1)\times (0,T], \\
	u(0,t), &= 0 && t\in [0,T],\\
	u(1,t), &= 0 && t\in [0,T],\\	
	 u_0(x), &= \sin(\pi x) , && x\in [0,1].
\end{align}
```

For this problem, use a spatial grid with constant mesh spacing,

```math
\mathcal G_h:= \{ i h : i = 0, \dots , N;\, h N = 1\},
```

and implement the Crank Nicolson scheme, which is defined for time index $n = 0, 1, 2,\dots $,

```math
	\frac{u_i^{n+1} - u_i^n}{\tau}  = \frac{a}{2} \left(  \frac{u_{i-1}^n - 2u_i^n+ u_{i+1}^n}{h^2} + \frac{u_{i-1}^{n+1} - 2u_i^{n+1} + u_{i+1}^{n+1}}{h^2}\right), \qquad i=1,\dots ,N-1. \notag
```

The values for $i = 0, N$  and $n = 0$, are defined by the boundary conditions, and the initial conditions, respectively.

##  Part 1

 Perform computations with $N = 20$ and $N = 200$. Choose $\tau = h = \frac{1}{N}$. (Note that this implies $\lambda = \frac{a\tau}{h^2} = aN$, i.e $\lambda$ changes with the mesh!) Plot the error 

 ```math
		\max_{1\leq i \leq N-1} |u_i^n - u(i h, n\tau)  |
```
for $n \tau = T=0.2$, and both values of $N$. (The exact solution $u(x,t)$ is known from class.)

##  Part 2

Assume that the equation is in the non-dimensional form derived in class. If the physical problem is heat conduction for a wire of length $5cm$, made of copper, how much time does it take for the temperature at the midpoint of the domain to be reduced by a factor of two? 

Remark: for this second part, you may use the grid with $N=200$ and  $\lambda$ as in part 1. Just stop the simulation whenever the value at the midpoint drops below half the initial value. You need to convert the non-dimensional time to a dimensional value. To do that you need to find the value for the thermal diffusivity for copper (room temperature is fine.)


