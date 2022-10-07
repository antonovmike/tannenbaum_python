x = 8
y = 0
top = 0
i = 1
print(" " * x, end = ""), print("A")
while y < x:
    if x%2 == 1:
        print("|")
        print("A")
        print()

    while i <= x:
        for empty_space in range(x-i):
            print(" ", end = "")
        for left_side in range(i):
            print("L", end = "")
        for middle in range(i, i+1):
            print("M", end = "")
        for right_side in range(i):
            print("R", end = "")
        print()
        i= i + 1

    y = y + 1
print(" " * (x-1), end = ""), print("ШШШ")