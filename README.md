[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i-S4iVKr)
# eas501-newtonRaphson

Write a python function with a call of `x, iter = newtonRaphson(g, x0, eps, delta, itermax)` which used the Newton-Raphson method which returns the root of a function `g`. The inputs are:
 - `g`: A function which returns `f, fx = g(x)` where `f` is the function value and `fx` is the function derivative evaluated at `x`.
 - `x0`: The initial guess at the root.
 - `eps`: The tolerance to use. Consider the method converged when the magnitude of the full step is less than this value.
 - `delta`: Criteria for divergence. Consider the method as diverging when the magnitude of the full step is more than this value. If the method is diverging raise an exception with this exact error message: `Error: Divergence`
 - `itermax`: The maximum number of iterations. If the maximum number of iteration is exceeded raise an exception with this exact error message: `Error: Maximum Number of Iterations`

The outputs are:
 - `x`: The root of the function `g`
 - `iter`: The number of iterations required to obtain the root.

*NOTE:* This is an individual programming project.

# Information regarding unit tests and autograding

- You can test your code by running `python newtonRaphson_unit.pyo` in the same directory as your `newtonRaphson.py` file. You _must_ use python version 3.8 to run the unit test locally.
- The autograder will use a unit test that is obtained externally. 
- If your commit does not pass the autograder you will receive an email stating so.
- To check status of the autograder perform the following steps in GitHub:
  1. Select `Actions`
  2. Select `GitHub Classroom Workflow`
  3. Select the workflow you are interested in viewing
  4. Select `Autograding`
  5. Select `Run education/autograding@v1`
