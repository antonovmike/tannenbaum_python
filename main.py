from time import sleep

x = 18
y = 0
top = 0
i = 1
print(" " * x, end = ""), print("A")
sleep(0.8)
while y < x:
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
        sleep(0.8)

    y = y + 1
print(" " * (x-1), end = ""), print("ШШШ")
