for _ in range(int(input())):
    length = int(input())
    towers_color={}
    answers=[]
    j=1
    for i in input().split():
        i = int(i)
        try:
            towers_color[i].append(j)
        except:
            towers_color[i]=[j]
        j+=1
    for k in range(1,length+1):
        if k in towers_color:
            places=towers_color[k]
            start=places[0]
            answer=0
            for i in places:
                if (i-start-answer)%2==0:
                    answer+=1
            answers.append(answer)
        else:
            answers.append(0)

    print(*answers)


