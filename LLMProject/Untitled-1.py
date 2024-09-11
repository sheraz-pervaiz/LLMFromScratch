print("This line will be printed.")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    # Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))
print ("Pynum successully imported")
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print("Value of BMI %s")
print(bmi)
# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]