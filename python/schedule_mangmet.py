import math
for _ in range(int(input())):
    n,m = map(int,input().split())
    list = [int(i) for i in input().split()]
    workers = [0 for i in range(n)]
    for i in list:
        workers[i-1]+=1
    min_count = math.ceil(m/n)
    count= min_count
    # for i in workers:
    #     if i>=min_count:
    #         count+=i-count
    #     else:
    #         count= min(count-(min_count-i)//2,i+(min_count-i)*2)
    for i in workers:
        count=max(count,i)
    for i in workers:
        count= min(count-(min_count-i)//2,i+(min_count-i)*2)
        # task = i
        # while task+1<min_count:
        #     new_count=max(count-1,task+2)
        #     if new_count<count:
        #         count=new_count
        #         task+=2
        #     else:
        #         break
    print(count)
