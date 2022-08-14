# n,m= map(int,input().split())
# list = [int(i) for i in input().split()]
# heights=[]
# for i in range(n-1):
#     heights.append(list[i]-list[i+1])
# list=0

# for _ in range(m):
#     s,e=map(int,input().split())
#     count=0
#     if e>s:
#         case = heights[s-1:e-1] 
#         for i in case:
#             if i>0:
#                 count+=i
#     else:
#         case = heights[e-1:s-1]
#         for i in case:
#             if i<0:
#                 count-=i 
#     print(count)
n=int(input())
two_d_array = [[0 for j in range(n)] for i in range(n)]



