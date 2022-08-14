for _ in range(int(input())):
    n,d=map(int,input().split())
    people=sorted(int(i) for i in input().split())
    front_row=people[:n]
    back_row=people[n:]
    answer=("YES")
    for i in range(n):
        if back_row[i]-d<front_row[i]:
            answer=("NO")
            break
    print(answer)

