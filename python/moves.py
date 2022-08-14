for _ in range(int(input())):
    num=int(input())

    if num%3==0:
        print(num//3)
    elif num==1:
        print(2)
    else:
        print((num//3) +1)