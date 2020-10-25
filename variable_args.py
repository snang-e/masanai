def get_sum_3(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(get_sum_3(1, 2, 3, 4))