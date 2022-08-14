for _ in range(int(input())):
    length = int(input())
    list = [int(i) for i in input().split()]
    answer="YES"
    for i in range(1,length):
        if list[i]%list[0]!=0:
            answer="NO"
            break
    print(answer)
    