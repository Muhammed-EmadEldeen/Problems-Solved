for _ in range(int(input())):
    n,h,m=map(int,input().split())
    ansh=0
    ansm=0
    ansh_min=23
    ansm_min=59
    for i in range(n):
        hi,mi=map(int,input().split())
        if mi<m:
            ansm=(mi-m)%60
            ansh=(hi-h-1)%24

        else:
            ansm=mi-m
            ansh=(hi-h)%24
        # minimum = min(minimum,ansh*100+ansm)
        print(ansh,ansm)
        if ansh<ansh_min:
            ansh_min=ansh
            ansm_min=ansm
        elif ansh_min==ansh and ansm<ansm_min:
            ansm_min=ansm
    print(ansh_min,ansm_min)


    # if minimum==0:
    #     print(0,0)
    # else:
    #     print(f"{str(minimum)[:-2]} {str(minimum)[-2:]}")