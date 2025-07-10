def newtonRaphson(g, x0, eps, delta, itermax):
#newtonRaphson:Determines the approximate root of a function using Newton-Raphson method.
#    Input:
#        g (function): Function that returns both the function value and its derivative.
#        x0 (float): Initial guess of x
#        eps (float): Tolerance for convergence.
#        delta (float): Tolerance for divergence.
#        itermax (int): Maximum number of iterations.
#
#    Output:
#        x2: Root of the function using Newton-Raphson method.
#        iter: No of iterations
    
    x1 = x0
    iter = 0
    while iter < itermax:
        f, f1 = g(x1)
        x2 = x1 - f / f1
        if abs(x2 - x1) < eps:
            x1=x2
            return x2,iter+1
        elif abs(x2 - x1) > delta:
            raise ValueError("Error: Divergence")
        x1 = x2
        iter += 1
    raise ValueError("Error: Maximum Number of Iterations")
