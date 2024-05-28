from math import comb,sqrt, erf
from scipy.special import erfinv

# General mean and standard deviation formulas for discrete random number variables
#     l1 = discrete random variable
#     l2 = probablity for each
def meanSTD(l1,l2):
    lst = list(zip(l1,l2))
    mean = 0
    std = 0
    for tup in lst:
        mean += tup[0]*tup[1]
    for tup in lst:
        std = ((tup[0]-mean)**2)*tup[1]
    std = sqrt(std)
    print(f"Mean: {mean}, std dev: {std}, sum: {sum(l2)}")

# Bernoulli Trials / Binomial Distribution
def bern(x,n=10,p=0.3):
    print(f"P(X=x) = {comb(n,x)*(p**x)*((1-p)**(n-x))}\nmean = {n*p}\nstd dev = {sqrt(n*p*(1-p))}")

# Normal Distribution
#     Calculates area to the left of Z-value
def area(z_value):
    area = 0.5*(1+erf(z_value/sqrt(2)))
    return area

def z(area):
    # Assuming the distribution is standard normal (mean = 0, standard deviation = 1)
    z_value = erfinv(2 * area - 1) * sqrt(2)
    return z_value
#**************************************************************************************************
meanSTD([2,4,5,6,7,8],[0.023,0.049,0.357,0.251,0.314,0.006])
print(f"Area: {area(-1.66):.4f}")
print(f"Z-value: {(z(0.01)):.2f}")
print(comb(11,4))

print((3.893-3.52)/(1.258/sqrt(15)))