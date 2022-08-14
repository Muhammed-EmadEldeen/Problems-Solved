def binarySearch(x, low, high): 
    mid = (low + high) // 2 
    try:
        if x >= values[mid] and x < values[mid+1]:
            return mid+1
        elif x >= values[mid]:     
            return binarySearch(x, mid + 1, high)
        else:                        
            return binarySearch(x, low, mid - 1)
    except:
        return count

for _ in range(int(input())):
    n=int(input())
    list_of_numbers=[int(i) for i in input().split()]
    numbers=[]
    values=[]
    count=0
    answer=0
    for i in range(1,n+1):
        value=list_of_numbers[i-1]
        if value<i:
            values.append(value)
            numbers.append(i)
            count+=1
    values.sort()
    for i in numbers:
        answer +=count-binarySearch(i,0,count)
    print(answer)


