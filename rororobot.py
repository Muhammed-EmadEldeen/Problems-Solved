n,m=map(int,input().split())
list = [i for i in input().split()]
for _ in range(int(input())):
    y1,x1,y2,x2,s = map(int,input().split())
    if (x2-x1)%s!=0 or (y2-y1)%s!=0 :
        print("NO")
    else:
        height= y1+((n-y1)//s)*s
        answer = 'YES'
        test_list= list[min(x1,x2)-1:max(x1,x2)-1]
        for i in test_list:
            if height<=int(i):
                answer ="NO"
                break
        print(answer)