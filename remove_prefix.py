for _ in range(int(input())):
    n=int(input())
    list = [int(i) for i in input().split()]
    dict={}
    answer=0
    while n>0:
        item=list[n-1]
        if item in dict:
            answer=n
            break
        else:
            dict[item]=True
        n-=1
    print(answer)