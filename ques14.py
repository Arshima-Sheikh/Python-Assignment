
def read_multiple_lines():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    for line in lines:
        print(line)
print( read_multiple_lines())
