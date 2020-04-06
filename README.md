# CS-344: Artificial Intelligence

This repository is a collection of labs, homework, and other resources
associated with the Calvin University course CS-344: Artificial Intelligence.
All submissions in this repository assume that both the AIMA and PAIP tool libraries are already installed on the
user's own machine. Both of these repositories were provided as course material and contain all artificial
intelligence algorithms needed to complete the labs and homework.

This repository was created by Luke Steffen (lhs3) on Febuary 2, 2020.

## Description of Labs and Homework

### Lab 01

Lab 01 is about the General Problem Solver (GPS) program created by Herbert A. Simon, J.C. Shaw, and Allen Newell
in an attempt to create a universal problem solving engine. This lab uses the Monkeys and Bananas problem and the
Blocks World problem to demonstrate the strengths and limitations of the algorithm. This lab also uses the
Sussman Anomaly to show the limitations of the GPS. The lab also asks to come up with a problem that the GPS can 
not solve.

### Lab 02

Lab 02 is about local search algorithms. This lab uses both the hill climbing and simulated annealing algorithms
to demonstrate the general idea behind local search algorithms. This lab shows the benefits and drawbacks of both
algorithms, showing how hill climbing is faster than simulated annealing, but may not find the global maxima if
local maxima are present. This lab shows how each algorithm works by using two graphs of an absolute function and
an absolute sin function.

### Lab 03

Lab 03 is about constraint satisfaction and how search algorithms using constraint satisfaction differ from
traditional search algorithms. This lab shows the difference between the DFS, AC3, Backtracing, and Min
Conflicts algorithms, showing their strengths and weaknesses by using the sudoku and n-Queens problems. Once
the differences between each type of algorithm have been established, the lab then asks to consider the
differences between constraint satisfaction and traditional search methods.

### Lab 04

Lab 04 is about joint probability systems and Bayes' Rule. This lab shows how artificial intelligence can use
statistics to determine things by thinking logically. This lab fist shows how a joint probability system would
work, showing the issues that come with joint probability tables and how unweildy they can become. The lab then
moves on to Bayes' Rule with some hand calculated probabilities. This part of the lab shows that you can calculate
probabilities with less information given by using Bayes' Rule. This part of the lab also shows some statistical
"paradoxes" regarding drug tests and cancer tests.

### Lab 05

Lab 05 is about Bayesian Networks and determining probabilities from them using less space than full joint distribution
tables. The first portion of the lab uses a Burlary/Earthquake Bayesian Network and demonstrates how the syntax is used
to get results. The second part of the lab asks to set up a new Bayesian Network using Cancer and two tests that predict
cancer. The lab then asks to calculate a few probabilities by hand and by using the code set up. The lab then asks for
an explanation as to why the probabilities seem unexpected. The third part of the lab asks to create another new Bayesian
Network and compute some probabilities in it both by hand and through the code provided. The lab again asks why some of
the probabilities may seem unexpected. The lab closes by returning to the first portion of the lab and examining the
different types of functions used to find probabilities, asking why the they give different results.

### Lab 06

Lab 06 is an introduction to Machine Learning Artificial Intelligence. The first portion of the lab is about how Machine
Learning works and asks to solve for the information gain of the aspect "Hungry" in the restaurant dataset. Once the 
information gain has been solved, the lab asks if this aspect is better than the previous examples shown (Partrons, Type).
Next, the lab asks to record the answers given to a Google page about framing and formulating a machine learning problem.
The final portion of the lab asks the user to load the keras and numpy libraries to print out some basic information
about the boston_housing dataset.

### Lab 07

Lab 07 is an introduction to the Pandas, NumPy, and TensorFlow libraries along with a small tutorial of how to manipulate
data and train models. The first portion of the lab discusses how to create a Pandas dataframe and various ways of chaning
and manipulating the data. The second portion of the lab discusses how to build, train, and examine a model by giving it
input data. The final portion of the lab discuesses how to create and train a model using a synthetic feature. All of these
tutorials were Google hosted Jupyter Notebooks that can be found at the following links.

* Intro to Pandas: [https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb]
* First Steps with TensorFlow: [https://colab.research.google.com/notebooks/mlcc/first_steps_with_tensor_flow.ipynb]
* Synthetic Features: [https://colab.research.google.com/notebooks/mlcc/synthetic_features_and_outliers.ipynb]

### Lab 08

Lab 08 looks at both the TensorFlow and Keras libraries and how to train a model to show how to validate models, create
synthetic features, create feature crosses, and work with the Keras library. This lab is a continuation from Lab 07. The
first portion of the lab is a tutorial of how to validate a training model by using validation data. The second portion of
the lab examines how to create and use synthetic features to improve a model's training. The third portion of the lab is a
tutorial of how to create a cross feature for further accuracy in model traininig. The fourth portion of the lab examines
how to use the Keras library to train a model. All of these tutorial can be found at the following links.

* Validation: [https://colab.research.google.com/notebooks/mlcc/validation.ipynb]
* Feature Engineering: [https://colab.research.google.com/notebooks/mlcc/feature_sets.ipynb]
* Feature Crosses: [https://colab.research.google.com/notebooks/mlcc/feature_crosses.ipynb]
* Keras: [https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.7-predicting-house-prices.ipynb]

### Homework 01

Homework 01 revists the local search and CSP algorithms discussed in labs 01-03. This homework fist asks a more
philosophical question about introspection and human cognitive modelling. After this question, homework asks you
to create and formulate the Travelling Salesman Problem for the local search algorithms hill climbing and simulated
annealing to solve. Once a solution to this problem has been formulated, the homework asks you to create a scheduling
problem for constraint satisfaction search algorithms to solve.

### Homework 02

Homework 02 looks at Bayesian Networks and statistical approaches to AI. The first portion of the homework asks to
implement an email spam filter by using word probabilities. After the code has been created, the homeworks asks what
makes this approach a Bayesian approach. The second portion of the homework covers similar things done in Lab 05. The
homework gives a Bayesian Network example and asks to implement this network into code. Once this has been done, the
homework asks to solve some probabilities associated with the Bayesian Network by hand and by code.

