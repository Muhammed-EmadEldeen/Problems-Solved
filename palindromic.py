for _ in range(int(input())):
    n=int(input())
    num=int(input())
    answer= (10**n)-1-num
    if answer<10**(n-1):
        answer+= int("1"*n)+1
    print(answer)
