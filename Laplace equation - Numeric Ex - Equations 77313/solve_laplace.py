import numpy as np
import numba

@numba.jit
def solve(xx, yy, potential, r, theta, alpha, upper_bound, dn):
    mean_before = potential.mean()
    for i in range(n-1):
        for j in range(n-1):
            rr = r[i][j]
            tt = theta[i][j]
            condition = ((rr<=R) and 
                         (np.rad2deg(tt)<=np.rad2deg(alpha)) and 
                         (np.rad2deg(tt)>=0)) or (upper_bound - np.abs(xx[i]) <= dn) or (upper_bound - np.abs(yy[j]) <= dn)
            if not condition:
                potential[i][j] = 1/4 * (potential[i+1][j] + potential[i-1][j] + potential[i][j+1] + potential[i][j-1])
    return potential, potential.mean()-mean_before