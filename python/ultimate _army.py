import re
def compute_leader(leader,count):
    next=str[count+1]
    if next=='(':
        list[str[count]]=leader
        compute_leader(str[count],count+2)
    elif next==')':
        return count+2
    else:
        




for _ in range(int(input())):
    n=int(input())
    list=[0 for _ in range(n)]
    str=input()
    count=2
    while count<n:
        count=compute_leader(str[0],count)
