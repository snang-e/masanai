a = int(input("숫자 입력1 : "))
b = int(input("숫자 입력2 : "))

if (a%2 == 0) and (b%2 == 0):
    print("두 수 모두 짝수입니다.")
elif (a%2 == 0) or (b%2 == 0):
    print("두 수 중 하나 이상이 짝수입니다.")
else:
    print("두 수 모두 홀수입니다.")