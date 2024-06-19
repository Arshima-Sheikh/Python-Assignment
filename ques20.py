def sum_of_list(numbers):
    return sum(numbers)


numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("The sum of the list is:", sum_of_list(numbers))
