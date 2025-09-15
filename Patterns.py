# Basic Star Patterns
print("Star patterns /n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('/n')

# Inverted star pattern
print("Inverted star patterns /n")
for i in range(6,1,-1):
    for j in range(i):
        print("*", end="")
    print('/n')