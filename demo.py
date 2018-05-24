from numpy import genfromtxt, mean
from matplotlib.pyplot import plot, scatter, show
from os.path import dirname


# printing values
def print_values():
    print("intercept =", b)
    print("slope =", m)
    print("error =", error)
    print("----------")


# reading csv file as a list
current_dir = dirname(__file__)
data_set = genfromtxt(current_dir + "/data.csv", delimiter=",")
x = data_set[:, 0]
y = data_set[:, 1]

# initializing both intercept b & slope m as 0
b = 0
m = 0

# calculating predected values and errors
predected_y = m * x + b
error = mean(y - predected_y)

# printing & plotting initial values
print_values()
scatter(x, y)

# approximating learning rate
num_iterations = len(data_set) * 10
learning_rate = 2 / (num_iterations * 10)

# adjusting slope & intercept values for each iteration
for i in range(num_iterations):
    # predecting points & calculating error
    predected_y = m * x + b
    error = mean(y - predected_y)

    # calculating correcting value
    avg_change = 2 / len(data_set) * error
    correction = avg_change * learning_rate

    # updating intercept & slope values
    b += correction
    m += sum(x) * correction


# calculating predected values
predected_y = m * x + b

# printing & plotting initial values
print_values()
plot(x, predected_y)

# plotting graph
show()
