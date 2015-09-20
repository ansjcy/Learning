import numpy as np
from scipy.optimize import leastsq #Least-square fitting
import pylab as pl

def func(x, p):# A * sin(2 * pi * k * x + theta)
    A, k, theta = p
    return A * np.sin(2 * np.pi * k * x + theta)

def residuals(p, y, x): # the difference between x, y
                        # p is the coefficient want to find
    return y - func(x, p)

x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6
y0 = func(x,[A, k, theta])
y1 = y0 + np.random.randn(len(x))

p0 = [7, 0.2, 0]

plsq = leastsq(residuals, p0, args=(y1, x))

print u"real:", [A, k, theta]
print u"nihe", plsq[0]

pl.plot(x, y0, label=u"real")
pl.plot(x, y1, label=u"noise")
pl.plot(x, func(x, plsq[0]), label=u"nihe")
pl.legend()
pl.show()