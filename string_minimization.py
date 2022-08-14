for _ in range(int(input())):
    n,m=map(int,input().split())
    indeces = [int(i) for i in input().split()]
    dict={}
    for i in range(n):
        index=indeces[i]-1
        index2=m-index-1
        if index<=index2 and index not in dict:
            dict[index]=True
        elif index2 in dict:
            dict[index]=True
        else:
            dict[index2]=True
    string = ''
    for i in range(m):
        if i in dict:
            string+="A"
        else:
            string+="B"
    print(string)
            
         