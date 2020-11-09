
import numpy as np 
from scipy.stats import norm

from anomaly.em.util.objects import Normal, Params 

def compute_responsibilities(data : np.array, params: Params) -> np.array:
    n_samples = np.size(data)
    responsibilities=np.zeros((2, n_samples)) # initialize 

    pi, cluster1, cluster2 = params.pi, params.cluster1, params.cluster2 
    unnormalized_responsibilities_1 = np.array([pi*cluster1.pdf(x) for x in data])
    unnormalized_responsibilities_2 = np.array([(1.0-pi)*cluster2.pdf(x) for x in data])
    unnormalized_responsibilities_sum = np.add(unnormalized_responsibilities_1,unnormalized_responsibilities_2)
    responsibilities[0,:] = unnormalized_responsibilities_1 / unnormalized_responsibilities_sum
    responsibilities[1,:] = unnormalized_responsibilities_2 / unnormalized_responsibilities_sum
    return responsibilities

def estimate_parameters(responsibilities : np.array, data: np.array) -> Params:

    # sample size 
    n1 = np.sum(responsibilities[0,:])
    n2 = np.sum(responsibilities[1,:])
    n = np.size(responsibilities, 1)

    # estimate individual parameters 
    mu1 = (1.0/n1) * np.dot(responsibilities[0,:],data)
    mu2 = (1.0/n2) * np.dot(responsibilities[1,:], data)

    var1 = (1.0/n1) * np.dot(responsibilities[0,:], (data- mu1)**2 )
    var2 = (1.0/n2) * np.dot(responsibilities[1,:], (data- mu2)**2 )

    pi = n1/n 

    # return as a Params object 
    cluster1 = Normal(loc = mu1, var = var1)
    cluster2 = Normal(loc = mu2, var = var2)
    return Params(cluster1=cluster1, cluster2=cluster2, pi=pi) 
