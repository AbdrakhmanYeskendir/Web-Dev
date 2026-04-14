def min_4_numbers(num1, num2, num3, num4):
    result = num1
    if num2 < result:
        result = num2
    if num3 < result:
        result = num3
    if num4 < result:
        result = num4
    return result

arr = list(map(int, input().split()))
print(min_4_numbers(arr[0], arr[1], arr[2], arr[3]))