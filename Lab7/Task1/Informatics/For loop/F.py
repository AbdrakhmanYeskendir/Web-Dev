x = input()
reversed_x = ""

for i in reversed(x):
    reversed_x += i

print(int(reversed_x))  # int() сам убирает ведущие нули