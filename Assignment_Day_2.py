#Question No 1

def Q1():
    x = input('Enter the elements : ').split()
    l = []
    m = []

    for i in x:
        l.append(int(i))

    for i in l:
        if i % 1 == 0:
            m.append(i)

    print(m)

#Question No 2

def Q2():
    n = int(input('Enter the value of n : '))

    for i in range(1, n + 1):
        print(' ' * (n - i), str(i) * i)

ch = int(input('Enter 1 for Question 1 and 2 for Question 2 : '))

if ch == 1:
    Q1()

elif ch == 2:
    Q2()

else:
    print('Invalid Input')