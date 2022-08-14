def add_numbers(num):
    global max_int
    try:
        del dict[num]
        add_numbers(num+1)
    except:
        dict[num]=True
        if num>max_int:
            max_int=num

n,q= map(int,input().split())
integers=[int(i) for i in input().split()]
for _ in range(q):
    pos,val= map(int,input().split())
    integers[pos-1]=val
    max_int=0
    dict={}
    for i in integers:
        add_numbers(i)
    print(max_int)