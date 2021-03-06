# Author: Pierre Ablin <pierreablin@gmail.com>
# License: MIT

# This is the simplest example of autoptim use.


import numpy as np
from autoptim import minimize


# Specify the loss function, in a pytorch compatible-way :
def rosenbrock(x):
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

# Choose the starting point:


x0 = np.zeros(2)

x_min, _ = minimize(rosenbrock, x0)
print(x_min)
