def find_min_max(lst):
    return min(lst), max(lst)

# Test the function
lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
min_value, max_value = find_min_max(lst)
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
