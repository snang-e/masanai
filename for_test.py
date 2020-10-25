def gugudan():
    dan = [2, 3, 4, 5, 6, 7, 8, 9]
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in dan:
        if i == 3:
           continue

        for j in number: 
            print(i, ' * ', j, ' = ', i*j)
        print('=============')

#gugudan()

def hello(name, location):
    print("{}에 계신 {}님 안녕하세요".format(location, name))

hello('어묵', '마산')