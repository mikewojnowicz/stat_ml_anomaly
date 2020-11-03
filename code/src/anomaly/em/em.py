"""
Use EM to fit a mixture model in the special case of 
2 mixture components, each univariate Gaussian 
"""

# TODO: Update requirements once I split this off into a smlfad repo.
import numpy as np 
from scipy.stats import norm
from recordclass import recordclass

from anomaly.em.generate import sample_from_gaussian_mixture
from anomaly.em.util.objects import Normal, Params, print_params 
from anomaly.em.util.compute import compute_responsibilities, estimate_parameters

### Generate True Data 
data=sample_from_gaussian_mixture(mu1 = 0.0, mu2= 10.0, scale1 = 1.0, scale2 = 5.0, pi = .8, n=1000)

### Initialize Parameters
cluster1 = Normal(loc = -1.0, var = 1.0)
cluster2 = Normal(loc = 1.0, var = 1.0)
pi = .80 # mixture weight on cluster 1 
params=Params(cluster1=cluster1, cluster2=cluster2, pi=pi)

### Run some iterates of the EM algorithm 
## What a fun exercise!
n_iterates = 10 
for i in range(n_iterates):
    # E-Step 
    responsibilities = compute_responsibilities(data, params)
    # M-step
    params = estimate_parameters(responsibilities, data)
    
    #Print
    print(f"\n ---- Iterate {i} ----- \n")
    print_params(params)
