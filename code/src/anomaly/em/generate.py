"""
Generate a sample from a mixture model in the special case of 
2 mixture components, each univariate Gaussian 
"""

import numpy as np 
from scipy.stats import norm

def sample_from_gaussian_mixture(
    mu1 : float, mu2 : float , scale1 : float, scale2 : float, pi : float, n : int 
) -> np.array:
    """
    Obtain a sample from a mixture model in the case where there are
    two components, both univariate Gaussian

    Arguments:
        mu1: mean of component 1
        mu2: mean of component 2 
        scale1: standard deviation of mixture component 1 
        scale2: standard deviation of mixture component 2 
        pi : mixture weight on component 1 
        n: number of samples desired
    
    Returns:
        A sample from the mixture model 
    """
    n_samples_for_cluster_1  = int(pi*n)
    n_samples_for_cluster_2 = n - n_samples_for_cluster_1

    data1 = np.random.normal(loc=mu1, scale=scale1, size=n_samples_for_cluster_1)
    data2 = np.random.normal(loc=mu2, scale=scale2, size=n_samples_for_cluster_2)

    data = np.concatenate((data1,data2))
    np.random.shuffle(data)
    return data 
