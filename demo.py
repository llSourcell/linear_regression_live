from numpy import genfromtxt, mean
from matplotlib.pyplot import plot, scatter, show
from os.path import dirname


current_dir = dirname(__file__)
data_set = genfromtxt(current_dir + "/data.csv", delimiter=",")
x_list = data_set[:, 0]
y_list = data_set[:, 1]

b = 0
m = 0

predected_y = m * x_list + b
avg_error = mean((y_list - predected_y) ** 2)

print("initially : ")
print("intercept =", b)
print("slope =", m)
print("error =", avg_error)
print("----------")

N = len(x_list)
num_iterations = N * 100
learning_rate = 1 / num_iterations

for _ in range(num_iterations):
    predected_y = m * x_list + b
    y_difference = y_list - predected_y

    b_gradient = sum(2 / N * y_difference)
    m_gradient = sum(2 / N * x_list * y_difference)

    b += learning_rate * b_gradient
    m += learning_rate * m_gradient

predected_y = m * x_list + b
avg_error = mean((y_list - predected_y) ** 2)

print("finally :")
print("intercept =", b)
print("slope =", m)
print("error =", avg_error)
print("----------")

scatter(x_list, y_list)
plot(x_list, predected_y)

show()
