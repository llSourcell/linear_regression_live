from numpy import genfromtxt, mean
from matplotlib.pyplot import plot, scatter, show
from os.path import dirname


def print_values():
    print("intercept =", b)
    print("slope =", m)
    print("error =", error)
    print("----------")


current_dir = dirname(__file__)
data_set = genfromtxt(current_dir + "/data.csv", delimiter=",")
x = data_set[:, 0]
y = data_set[:, 1]

b = 0
m = 0

predected_y = m * x + b
error = mean(y - predected_y)

print_values()
scatter(x, y)

num_iterations = len(data_set) * 10
learning_rate = 2 / (num_iterations * 10)

for i in range(num_iterations):
    predected_y = m * x + b
    error = mean(y - predected_y)

    avg_change = 2 / len(data_set) * error
    correction = avg_change * learning_rate

    b += correction
    m += sum(x) * correction


predected_y = m * x + b

print_values()
plot(x, predected_y)

show()
