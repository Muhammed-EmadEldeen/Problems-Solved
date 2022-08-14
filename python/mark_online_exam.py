no_of_questions = int(input())

answers= ["T"]*no_of_questions
new_answers=answers
print(new_answers)
input()
old_input= int(input())


def inverse_answers(s,e):
    for i in range(s-1,e):
        if new_answers[i]=="T":
            new_answers[i]='F'
        else:
            new_answers[i]="T"

def half_main(s,e):
    global new_answers
    global new_input
    global old_input
    global answers
    length=e-s+1
    inverse_answers(s,e)
    print(new_answers)
    new_input=int()
    if new_input>old_input:
        if length+old_input==new_input:
            return None
        else:
            answers=new_answers
            old_input=new_input
            main(s,e)
    elif new_input<old_input:
        if new_input==length+old_input:
            return None
        else:
            new_answers=answers
            main(s,e)
    else:
        main(s,e)




def main(s,e):
    if s==e:
        return None
    input()
    length=e-s+1
    s1=s
    e1=s+length//2-1
    s2=s+length//2
    e2=e
    half_main(s1,e1)
    half_main(s2,e2)
    

main(1,no_of_questions)
print(new_answers)
    
