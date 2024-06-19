def count_occurrences(lst, element):
    return lst.count(element)

# Test the function
lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
element = int(input("Enter the element to count: "))
print(f"The element {element} occurs {count_occurrences(lst, element)} times in the list.")
