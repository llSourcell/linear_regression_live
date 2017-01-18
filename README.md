# linear_regression_live
This is the code for the "How to Do Linear Regression the Right Way" live session by Siraj Raval on Youtube


##Overview

This is the code for [this](https://youtu.be/uwwWVAgJBcM) video on Youtube by Siraj Raval. I'm using a small dataset of student test scores and the amount of hours they studied. Intuitively, there must be a relationship right? The more you study, the better your test scores should be. We're going to use [linear regression](https://onlinecourses.science.psu.edu/stat501/node/250) to prove this relationship. 

Here are some helpful links:

####Gradient descent visualization
https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif

####Sum of squared distances formula (to calculate our error)
https://spin.atomicobject.com/wp-content/uploads/linear_regression_error1.png

####Partial derivative with respect to b and m (to perform gradient descent)
https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png

##Dependencies

* numpy

Python 2 and 3 both work for this. Use [pip](https://pip.pypa.io/en/stable/) to install any dependencies.

##Usage

Just run ``demo.py`` to see the results.

##Credits

Credits for this code go to [mattnedrich](https://github.com/mattnedrich). I've merely created a wrapper to get people started. 
