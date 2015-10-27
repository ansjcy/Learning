import numpy as np
from scipy.stats import dirichlet
import matplotlib.pyplot as plt
from scipy.stats import beta, norm
import pandas as pd
from numpy.random import choice

np.set_printoptions(precision=2)
#------when a(scale) is large, the sample result is approximate to G0...and the biao zhun cha is smaller!-----
def stats(scale_factor, G0=[.2, .2, .6], N=10000):
    samples = dirichlet(alpha = scale_factor * np.array(G0)).rvs(N)  #rvs:draw random samples from this distribution.
    print("                          alpha:", scale_factor)
    print("              element-wise mean:", samples.mean(axis=0))    #sample element junzhi
    print("element-wise standard deviation:", samples.std(axis=0))      #biao zhun cha
    print()

for scale in [0.1, 1, 10, 100, 1000]:
    stats(scale)

def dirichlet_sample_approximation(base_measure, alpha, tol=0.01):
    betas = []
    pis = []
    betas.append(beta(1, alpha).rvs()) #sample from beta function(1, alpha)
    pis.append(betas[0])
    while sum(pis) < (1.-tol):         #sum(pis) to infinity, we can get 1..
        s = np.sum([np.log(1 - b) for b in betas])
        new_beta = beta(1, alpha).rvs()
        betas.append(new_beta)
        pis.append(new_beta * np.exp(s))
    pis = np.array(pis)
    thetas = np.array([base_measure() for _ in pis])
    return pis, thetas

def plot_normal_dp_approximation(alpha):
    plt.figure()
    plt.title("Dirichlet Process Sample with N(0,1) Base Measure")
    plt.suptitle("alpha: %s" % alpha)
    pis, thetas = dirichlet_sample_approximation(lambda: norm().rvs(), alpha)
    pis = pis * (norm.pdf(0) / pis.max())
    plt.vlines(thetas, 0, pis, )
    X = np.linspace(-4,4,100)
    plt.plot(X, norm.pdf(X))
    plt.show()

#plot_normal_dp_approximation(.1)
# plot_normal_dp_approximation(1)
# plot_normal_dp_approximation(10)
# plot_normal_dp_approximation(1000)



class DirichletProcessSample():
    def __init__(self, base_measure, alpha):
        self.base_measure = base_measure
        self.alpha = alpha

        self.cache = []
        self.weights = []
        self.total_stick_used = 0.

    def __call__(self):
        remaining = 1.0 - self.total_stick_used
        i = DirichletProcessSample.roll_die(self.weights + [remaining])
        if i is not None and i < len(self.weights) :
            return self.cache[i]
        else:
            stick_piece = beta(1, self.alpha).rvs() * remaining
            self.total_stick_used += stick_piece
            self.weights.append(stick_piece)
            new_value = self.base_measure()
            self.cache.append(new_value)
            return new_value

    @staticmethod
    def roll_die(weights):
        if weights:
            return choice(range(len(weights)), p=weights)
        else:
            return None

#lambda and stuff: is used to a function that generate samples..
base_measure = lambda: norm().rvs()
n_samples = 10000
samples = {}
for alpha in [1, 10, 100, 1000]:
    dirichlet_norm = DirichletProcessSample(base_measure=base_measure, alpha=alpha)
    samples["Alpha: %s" % alpha] = [dirichlet_norm() for _ in range(n_samples)]

_ = pd.DataFrame(samples).hist()
