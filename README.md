# Statistical Machine Learning for Anomaly Detection 

## Instructors 
Mike Wojnowicz and Karin Knudson 


## Description
This workshop will introduce students to a variety of models in statistical machine learning that can be used for anomaly detection. Topics will include:  Mixture Models, Hidden Markov Models, Latent Dirichlet Allocation, Variational Autoencoders, and Normalizing Flows. Areas of application range from cybersecurity to biology to speech recognition. 


## Pre-requisites

Students should have some passing familiarity with basic statistical concepts (maximum likelihood, Bayes law, expectations, covariance matrices, conditional probability), and should be comfortable with Python programming.  We will also assume knowledge of calculus.

## Structure 

### Vision
Break the course into four topics, one per day.  (The last day is a flex day.)  Each day in turn has four subtopics.  Each subtopic will consist of about 20 minutes of presentation, followed by about 20 minutes of interactive group activity. 

### Execution

We allow for approximate execution of the vision.

* Some subtopics will have no exercises, some will have multiple.  Some exercises will occur mid-slides.
* It is likely that topics will take more than a day. (The flex day will soak up overflow.)

## Topics

* Day 1: Basics 
    * Frequentist approaches and Maximum Likelihood 
    * Exponential Families 
    * Bayesian approaches and Conjugate Bayesian Models
    * Probabilistic Graphical Models
* Day 2: Expectation Maximization (EM) 
    * Introduction (K-means)
    * Mixture Models
    * General comments
    * Cybersecurity applications
    * Hidden Markov Models
* Day 3: Variational Inference (VI)
    * Overview (and Relation to EM) 
    * Bayesian Mixture Models
    * Bayesian Hidden Markov Models
    * Latent Dirichlet Allocation 
* Day 4: Black Box Models 
    * Introduction (Motivation, PGM's + NN's, etc.) 
    * Automatic Differentiation Variational Inference
    * VAE 
    * Normalizing Flow
* Day 5: Flex Day 

## Goals
By the end of this workshop, we hope that you will

* Have some sense of various possible ways to approach an unsupervised learning problem (e.g., frequentist vs. Bayesian).
* Have some intuition about the the models listed in the description.  This intuition should, for example, support intelligent use of api's when modeling data.
* Understand what expectation maximization and variational inference are, and how they underly the learning of models such as those above.
* Develop and/or reinforce some understanding about modeling tools (e.g., how to determine conditional independence in a probabilistic graphical model; what exponential families mean and are used for; etc.)


## Further Readings

### Day 1: Overview 
* Statistical Inference
   * Casella, G., & Berger, R. L. (2002). Statistical inference (Vol. 2, pp. 337-472). Pacific Grove, CA: Duxbury. 
* Introduction to Bayesian Modeling
	* Hoff, P. D. (2009). A first course in Bayesian statistical methods (Vol. 580). New York: Springer.
	* Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). Bayesian data analysis. CRC press
* Graphical Models
	* CH 8 of Bishop, C. M. (2006). Pattern recognition and machine learning. springer.
	* Ghahramani, Z. (2001). An introduction to hidden Markov models and Bayesian networks. In Hidden Markov models: applications in computer vision (pp. 9-41).
* Exponential Families
	* Michael I Jordan's chapter: https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/other-readings/chapter8.pdf
	* Michael I Jordan's chapter: https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/other-readings/chapter9.pdf

### Day 2: Expectation Maximization (EM)
* Mixture Models and EM  
	* Section 2.3 and Chapter 9 of Bishop, C. M. (2006). Pattern recognition and machine learning. springer.
	* Sections 6.8 and 8.5 of Elements of Statistical Learning by Hastie et al. (2009)
* Hidden Markov Models (HMMs)
	* Sec 13.2 of Bishop, C. M. (2006). Pattern recognition and machine learning. springer
	* Ghahramani, Z. (2001). An introduction to hidden Markov models and Bayesian networks. In Hidden Markov models: applications in computer vision (pp. 9-41).


### Day 3: Variational Inference
* Introduction to VI 
	* Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). Variational inference: A review for statisticians. Journal of the American statistical Association, 112(518), 859-877.
* Latent Dirichlet Allocation
	* Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent dirichlet allocation. Journal of machine Learning research, 3(Jan), 993-1022.

### Day 4: Black Box Models 

* Normalizing Flows 
	* Dinh, L., Sohl-Dickstein, J., & Bengio, S. (2016). Density estimation using real nvp. arXiv preprint arXiv:1605.08803.
	* Papamakarios, G., Nalisnick, E., Rezende, D. J., Mohamed, S., & Lakshminarayanan, B. (2019). Normalizing flows for probabilistic modeling and inference. arXiv preprint arXiv:1912.02762. 
