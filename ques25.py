def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix


string = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with_prefix, ends_with_suffix = check_prefix_suffix(string, prefix, suffix)
print(f"Starts with prefix '{prefix}': {starts_with_prefix}")
print(f"Ends with suffix '{suffix}': {ends_with_suffix}")
