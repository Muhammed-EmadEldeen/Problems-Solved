for _ in range(int(input())):
    first_key=int(input())-1
    list=[int(i) for i in input().split()]
    second_key=list[first_key]
    if second_key !=0:
        if list[second_key-1]!=0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    