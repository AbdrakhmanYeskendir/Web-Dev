def power(a, n):
    return a ** n

line = input().split()
a = float(line[0])
n = int(line[1])
print(power(a, n))