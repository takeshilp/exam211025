def calculate_sum(a, * b):
    sum = a
    for i in b:
        sum += i
    return sum

calculate_sum(10,12)
print(calculate_sum(10,12))
print(calculate_sum(10,12,15))