for _ in range(int(input())):
    length,iq=map(int,input().split())
    list=[int(i) for i in input().split()]
    list.reverse()
    str=""
    Q=0
    for i in list:
        if i<=Q:
            str+='1'
        elif i>Q and Q<iq:
            str+='1'
            Q+=1
        elif i>Q and Q==iq:
            str+='0'
    print(str[::-1])

    # dict={}
    # j=0
    # for i in list:
    #     try:
    #         dict[i].append(j)
    #     except:
    #         dict[i]=[j]
    #     j+=1
    # i=0
    # while i <length:
    #     item= list[i]
    #     if item<=iq:
    #         dict[item].pop(0)
    #         str+="1"
    #         i+=1
    #     else:
    #         try:
    #             iq_next=dict[iq][0]
    #             if length-iq_next>iq:
    #                 str+='0'
    #                 i+=1
    #                 while i<=iq_next:
    #                     item= list[i]
    #                     if item<=iq:
    #                         dict[item].pop(0)
    #                         str+="1"
    #                     else:
    #                         str+='0'
    #                     i+=1
    #             else:
    #                 str+='1'
    #                 iq-=1
    #                 i+=1
    #         except:
    #             if iq>0:
    #                 str+='1'
    #                 iq-=1
    #                 i+=1
    #             else:
    #                 str+='0'*(length-i)
    #                 break

