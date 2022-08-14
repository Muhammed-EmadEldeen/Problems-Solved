def find_gcd(index,start):
    r=start%index
    if r==0:
        number =start
    else:
        number = start+index-r
    return number

for _ in range(int(input())):
    n,l,r = map(int,input().split())
    list_gcds=[]
    answer=True
    i=1
    while i<n:
        gcd = find_gcd(i,l)
        if gcd in range(l,r+1):
            list_gcds.append(gcd)
        else:
            answer =False
            break
        i-=1
    if answer:
        print("YES")

        print(*list_gcds)
    else:
        print("NO")