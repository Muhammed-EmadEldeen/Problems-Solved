def increase_tower_height(num):
    new_floors = max(towers_heights[num-1],towers_heights[num+1])-towers_heights[num]+1
    if new_floors>0:
        return new_floors
    else:
        return 0

for _ in range(int(input())):
    n=int(input())
    towers_heights = [int(i) for i in input().split()]
    if n%2==0:
        dict={}
        min_sum_even=0
        for i in range(1,n-1,2):
            min_sum_even +=increase_tower_height(i)
        i=n-2
        sum_even=min_sum_even
        while i>0:
            sum_even +=increase_tower_height(i)
            sum_even -=increase_tower_height(i-1)
            i-=2
            min_sum_even=min(sum_even,min_sum_even)
        print(min_sum_even)
    else:
        sum=0
        i=1
        while i<n-1:
            sum+=increase_tower_height(i)
            i+=2
        print(sum) 


