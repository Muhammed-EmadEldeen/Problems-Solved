def get_character(n):
    for i in range(c+1):
        if n<=list[i][0]:
            if i!=0:
                z=n-(list[i-1][0])
                character=(list[i][1]+z)-1
                return get_character(character)
            else:
                return string[n-1]

for _ in range(int(input())):
    global list
    global string
    global c
    m,c,q = map(int,input().split())
    string= input()
    list=[[m,1]]
    for i in range(c):
        l,r = map(int,input().split())
        m+=r-l+1
        list.append([m,l])
    print(list)
    for _ in range(q):
        print(get_character(int(input())))

