# m = int(input('m : '))
# n = int(input('n : '))
# l = int(input('l : '))

# def root_ex(a, b, c):
#     x1 = (-b + (b**2-4*a*c)**0.5) / 2 * a
#     x2 = (-b - (b**2-4*a*c)**0.5) / 2 * a
#     print('해는 ', x1, '또는 ', x2)

# root_ex(m, n, l)

def get_sum(a, b):
    return a+b

def get_sum_1(a=1, b=2):
    return a+b

def get_sum_2(a, b, c=3, d=4):
    result_1 = a + b
    result_2 = c - d
    return result_1, result_2



n1 = get_sum(10, 20)
print('10과 20의 합 : ', n1)

n2 = get_sum(100, 200)
print('100과 200의 합 : ', n2)

n3 = get_sum_1()
print(n3)

n4 = get_sum_2(3, 4)
print(n4)

