# genfromtxt will read csv as array & mean will calculate average
from numpy import genfromtxt, mean

# reading csv file as an array
points = genfromtxt("data.csv", delimiter=",")

# initializing intercept and slope values as 0
intercept, slope = 0, 0

# printing initial output values one by one
print("\nInitially..,")
print("intercept =", intercept)
print("slope =", slope)
print("error =", mean(
    (points[:, 1] - (slope * points[:, 0] + intercept)) ** 2))

# itteration count to 10 times the length of data set
num_iterations = len(points) * 10

# learning rate to 100th of data set size
learning_rate = 1 / (num_iterations * 10)

# running the loop for 10x the length of data to generate accurate slope and intercept
for i in range(num_iterations):
    # calculating average change in values when compared with predected and actual values
    avg_change = mean(2 / len(points) *
                      (points[:, 1] - (slope * points[:, 0]) + intercept))

    # using that average change to adjust intercept
    intercept += avg_change * learning_rate

    # using that average change to adjust slope
    slope += (avg_change * sum(points[:, 0])) * learning_rate

# printing final output values one by one
print("\nAfter", num_iterations, "itterations..,")
print("intercept =", intercept)
print("slope =", slope)
print("error =", mean(
    (points[:, 1] - (slope * points[:, 0] + intercept)) ** 2))
