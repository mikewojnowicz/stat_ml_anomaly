"""
Utility objects to aid in sampling mixture model in the special case of 
2 mixture components, each univariate Gaussian 
"""

import numpy as np 
from recordclass import RecordClass
from scipy.stats import norm

###
# The Normal Object
###
class Normal:

    def __init__(self, loc, var):
        self.loc=loc
        self.var=var
        self.scale=np.sqrt(var) 
    
    def pdf(self, x):
        return norm.pdf(x, loc=self.loc, scale=self.scale)

###
# The Params Object 
###

class Params(RecordClass):
    cluster1: Normal
    cluster2: Normal 
    pi: float 

# clus

def print_params(params : Params) -> None:

    print(f"cluster1: \n\t mean : {params.cluster1.loc : .04}, scale: {params.cluster1.scale : .04} \n"
        f"cluster2:  \n\t mean : {params.cluster2.loc : .04}, scale: {params.cluster2.scale : .04} \n"
        f"pi: {params.pi : .04}")
