# Unsupervised Statistical Machine Learning in Python (DRAFT)

## Instructors 
Mike Wojnowicz and Karin Knudson 


## Structure 
* 1.5 hour lecture per day 
* 1.5 hour python lab per day

## Pre-requisites

Calculus;  know one dist besides Normal; know maximum likelihood; know conditional probability, expectation, covariance matrix; some experience with python; some experience with data science + ML; (maybe) create a GitHub account.

## Topics

* Day 1: Statistical Inference / (maybe) Ice Breaker / (maybe) Python Template 
    * Icebreakers (Maybe) 
        * Could be a basis for how to group people for the “python lab"
    * Maximum Likelihood
    * Exponential Families 
    * (Maybe) Why Bayesian?
    * Conjugate Bayesian Models
    * (Maybe) Probabilistic Graphical Models (Independence Relations etc.)
* Day 2: Expectation Maximization (EM) 
    * Overview
    * Mixture Models
    * Hidden Markov Models
    * Cybersecurity:  Malware Ground Truth 
    * (Maybe) Segmented Hidden Markov Models
* Day 3: Variational Inference (VI)
    * Overview
    * Bayesian Mixture Models
    * Bayesian Hidden Markov Models
    * (Maybe) Bayesian Segmented Hidden Markov Models
    * Latent Dirichlet Allocation 
    * (Maybe) Stochastic Variational Inference
* Day 4: Black Box Variational Inference (BBVI)
    * Black Box Extensions - Black Box Variational Inference, Automatic Differentiation Variational Inference, etc.
    * VAE 
    * Normalizing Flow
    * (Probably not) PGMs+NN’s
* Day 5: Flex Day 

# Exercises

## Philosophy

Why have a lab as a part of the course, as opposed to just further lecture?

1. Working actively with the material will help you to better understand it, find good questions to ask, and be better prepared for the next sections.

Why have a lab as a part of the course, as opposed to just working on your own time? 

1. Opportunity to collaborate in groups.
2. Get real-time feedback from instructors.

## Ideas 
Python co-development paradigm -- collaborate in gitpod.io or Google Colab. We could potentially provide unit tests for each module, they could write code to make the tests pass (and perhaps write additional tests). This could include writing little mini functions (like sampling from a DP prior). This could also include calling apis from python packages.  Repo could provide some utilities in src/ (like forward backward algo).

## Codes
* [API] Use a pre-existing api to do something with data
* [Unit] Write a function that performs some suboperation
* [Hand] Mathematical Question 
* [Application] Apply the model to a highlighted domain specific application

## Schedule
### Day 1: Distributions / Ice Breaker / Python Template 
*  [Hand] Check ML estimate for a simple example
    * Extension: for distribution in the survival analysis case.
* [Hand] Compute the conjugate Bayes posterior for a simple example.
* [Hand] Show that certain distributions are in the exponential family
    * Bernoulli, Gaussian: http://www.cs.columbia.edu/~blei/fogm/2015F/notes/exponential-family.pdf.
* [???] Fit a Bayesian Multivariate Gaussian to some data, plot samples from the NIW Posterior.
* Maybe also use some library to fit some distribution to data using (a) maximum likelihood and (b) conjugate Bayes  ?

### Day 2: EM 
* Write Python code for k-means 
* Write Python code for mixture model (Like in the textbook)
    * Hughes has some exercises here; get them.
* [API] Fit a mixture model to data
    * Python notebook: http://krasserm.github.io/2019/11/21/latent-variable-models-part-1/
    * Scikit learn  has mixture models 
    * [Application] Try fitting EM to keystrokes bigrams.
* [Unit] Write Python code for HMM given access to forward backward function.
* [API] Use in a blackbox manner this hmm library 
    * https://github.com/hmmlearn/hmmlearn
    * https://hmmlearn.readthedocs.io/en/latest/index.html
* [Application] Fit HMM to EEG Data
    * https://ocw.mit.edu/courses/biology/7-91j-foundations-of-computational-and-systems-biology-spring-2014/assignments/
* [Application] Fit HMM to Genomics Data 
    * https://ocw.mit.edu/courses/biology/7-91j-foundations-of-computational-and-systems-biology-spring-2014/assignments/ 	 

### Day 3: VI Foundations
* [Unit/Hand] Compute the KL divergence between two distributions.
* [API] Fit Bayesian GMM to data https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html
* [API] Fit LDA to data 
* Other sources: https://github.com/kamperh/bayes_gmm, but that uses collapsed Gibbs sampling rather than VI.

### Day 4: Black Box Models
* [Unit] Change of variables for normalizing flow?
* [Unit] Forward pass for VAE?
* [API] SVI + VAE’s: 
    * Has python code and notebook: http://krasserm.github.io/2019/12/17/latent-variable-models-part-2/
* [Mix] VAE / RNVP:
    * Have them change my code to accomplish some subgoal.


