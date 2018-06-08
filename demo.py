from numpy import genfromtxt, mean
from matplotlib.pyplot import plot, scatter, show


data_set = genfromtxt("data.csv", delimiter=",")
x_list = data_set[:, 0]
y_list = data_set[:, 1]

intercept = 0
slope = 0

count = len(x_list)

num_iterations = count * 100
learning_rate = 1 / num_iterations

for _ in range(num_iterations):
    predected_y = slope * x_list + intercept
    y_difference = y_list - predected_y

    intercept_gradient = sum(2 / count * y_difference)
    slope_gradient = sum(2 / count * x_list * y_difference)

    intercept += learning_rate * intercept_gradient
    slope += learning_rate * slope_gradient

predected_y = slope * x_list + intercept
avg_error = mean((y_list - predected_y) ** 2)

print("intercept =", intercept)
print("slope =", slope)
print("error =", avg_error)

scatter(x_list, y_list)
plot(x_list, predected_y)

show()
