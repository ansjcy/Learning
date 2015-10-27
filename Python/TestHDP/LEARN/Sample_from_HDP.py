__author__ = 'jason'
from numpy.random import choice
from scipy.stats import beta
from scipy.stats import norm
from pandas import Series
import matplotlib.pyplot as plt


class DirichletProcessSample():
    def __init__(self, base_measure, alpha): #basemeasure: some samples
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
#prove that sampling from norm distribution is unique..
###############################
base_measure = lambda: norm().rvs()
ndraws = 10000
print("Number of unique samples after {} draws..".format(ndraws))
draws = Series([base_measure() for _ in range(ndraws)])
print(draws.unique().size)
################################
norm_dp = DirichletProcessSample(base_measure, alpha=100)
print("Number of unique samples after {} draws:".format(ndraws))
dp_draws = Series([norm_dp() for _ in range(ndraws)])
print(dp_draws.unique().size)
#################################
norm_hdp = DirichletProcessSample(norm_dp, alpha=10) #samples..
Series(norm_dp() for _ in range(10000)).hist()
_=plt.title("Histogram of Samples from norm_dp")
plt.show()
