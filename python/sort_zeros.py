for _ in range(int(input())):
    n=int(input())
    list = [int(i) for i in input().split()]
    positions={}
    first_number=list[n-1]
    answer=set()
    while n>0:
        n-=1
        second_number=list[n-1]
        if second_number> first_number:
            i=0
            while i <n:
                number=list[i]
                try:
                    n=max(n,positions[number])
                except:
                    None
                answer.add(number)
                i+=1
            n=0
        else:
           if first_number not in positions:
            positions[first_number]=n
        first_number=second_number
    print(len(answer))




