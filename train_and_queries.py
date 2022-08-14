number_of_test_cases= int(input())

def input_inf():
    global number_of_queries
    global dict
    input()
    dict={}
    number_of_queries=int(input().split(' ')[1])
    j=1
    stations=input().split(' ')
    for i in stations:
        i=i
        try:
            dict[i].append(j)
        except:
            dict[i]=[j]
        j+=1

def input_test():
    test = input().split(' ')  
    return [test[0],test[1]]


def main_iteration(test_case):
    try:
        if dict[test_case[0]][0]<dict[test_case[1]][-1]:
            return ("YES")
        else:
            return ('NO')
    except:
        return ('NO')

def main():
    input_inf()
    for i in range(number_of_queries):
        print(main_iteration(input_test()))

for i in range(number_of_test_cases):
    main()

