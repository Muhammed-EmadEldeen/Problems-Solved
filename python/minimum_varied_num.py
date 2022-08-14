for _ in range(int(input())):
    n=int(input())
    answer=0
    current=9
    while n>0:
        if n >=current:
            n-=current
            answer+=current*(10**(9-current))
            current-=1
        else:
            answer+=n*(10**(9-current))
            break
    print(answer)
