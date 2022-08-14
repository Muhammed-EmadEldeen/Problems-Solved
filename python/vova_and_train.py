import math
for _ in range(int(input())):
    inputt =[int(i) for i in input().split()]
    total_space=inputt[0]
    space_between_lanterns=inputt[1]
    lanterns = total_space//space_between_lanterns
    hidden_lanterns= (inputt[3]//space_between_lanterns-(inputt[2]-1)//space_between_lanterns)
    print(lanterns-hidden_lanterns)
    