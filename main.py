# Create the following piece of code:
# If x > 200, print out "Big";
# If x > 100 and x <= 200, print out "Average"; and
# If x <= 100, print out "Small".
# Use the if, elif, and else keywords in your code.

x=99
if x > 200:
    print('Big')
elif 200 >= x > 100:
    print('Average')
else:
    print('Small')

# You can achieve this by traversing the array in a spiral order. Here's a Python function to do that:

def snail(snail_map):
    result = []
    while snail_map:
        result += snail_map.pop(0)
        if snail_map and snail_map[0]:
            for row in snail_map:
                result.append(row.pop())
        if snail_map:
            result += snail_map.pop()[::-1]
        if snail_map and snail_map[0]:
            for row in snail_map[::-1]:
                result.append(row.pop(0))
    return result

 # Example usage:
snail_map = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = snail(snail_map)
print(result)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# if __name__ == '__main__':
#     print_hi('PyCharm')