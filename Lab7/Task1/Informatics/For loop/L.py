a = input()
sum = 0
count = 0

for i in reversed(a):
    sum += int(i) * (2 ** count)
    count += 1

print(sum)