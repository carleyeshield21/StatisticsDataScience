# Create the following piece of code:
# If x > 200, print out "Big";
# If x > 100 and x <= 200, print out "Average"; and
# If x <= 100, print out "Small".
# Use the if, elif, and else keywords in your code.

# x=99
# if x > 200:
#     print('Big')
# elif 200 >= x > 100:
#     print('Average')
# else:
#     print('Small')
#
# # You can achieve this by traversing the array in a spiral order. Here's a Python function to do that:
# def snail(snail_map):
#     result = []
#     while snail_map:
#         result += snail_map.pop(0)
#         if snail_map and snail_map[0]:
#             for row in snail_map:
#                 result.append(row.pop())
#         if snail_map:
#             result += snail_map.pop()[::-1]
#         if snail_map and snail_map[0]:
#             for row in snail_map[::-1]:
#                 result.append(row.pop(0))
#     return result
#
#  # Example usage:
# snail_map = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result = snail(snail_map)
# print(result)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# def distance_from_zero(num):
#     if type(num)==int:
#         print(abs(num))
#     else:
#         print('Not Possible')
#
# distance_from_zero(-10)
# distance_from_zero('cat')

# Create a range object with start=1, stop=10, step=2
my_range = range(1, 10, 2)

# Convert the range to a list
# my_list = list(my_range)
#
# # Display the list
# print(my_list)
#
# list = list(range(0,11))
# print(list)

import numpy
import pandas
import matplotlib
import seaborn
import sklearn
import scipy
import statsmodels.api as sm
import math

# raw_data = pandas.read_csv('1.03.+Dummies.csv')
# data = raw_data.copy()
# data['Attendance'] = data['Attendance'].map({'Yes': 1, 'No': 0})
# print(data)
# print('Ok')

# list = [12, 24, 37, 42, 55, 62, 72, 77, 246, 592]
# mean = numpy.mod(list)
# print(mean)


# Python int
python_integer = 42

# NumPy int64
numpy_int64 = numpy.int64(42)

# Check types
print(type(python_integer))  # <class 'int'>
print(type(numpy_int64))     # <class 'numpy.int64'>

print(python_integer==numpy_int64)

