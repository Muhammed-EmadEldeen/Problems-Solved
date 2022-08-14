def main(n):
    for i in range(n):
        for j in range(n):
            if list[i][j]=="#":
                list[i][j]='.'
                try:
                    if list[i+1][j]!='.' and list[i+2][j]!='.' and list[i+1][j+1]!='.' and list[i+1][j-1]!='.':
                        list[i+1][j]='.'
                        list[i+2][j]='.'
                        list[i+1][j+1]='.'
                        list[i+1][j-1]='.'
                    else:
                        return "NO"
                except:
                    return "NO"
    return "YES"



n = int(input())
list=[]
for i in range(n):
    list.append([i for i in input()])

print(main(n))