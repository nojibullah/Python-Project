#Name= Md Nojibullah
#cst1101
#project 

def question_1():
    print("do you care if your personal stuff messup")

def question_2():
    print("do you like to dress up your pet")

def question_3():
    print("care if your pet is smarter than you")

def question_4():
    print("do you wish your pet could help desk up a date")

def question_5():
    print("do you require independent")

def question_6():
    print("would rather scratch than bitten")

def ans_1():
    print("wrong chart you are a fish person")
    print("get a fish")

def ans_2():
    print("you are a cat person")
    print ("get a cat")
    
def ans_3():
    print("you are a dog person")
    print("get a cat")

#c=cat
#d=dog
#f=fish
c = 0
d = 0
f = 0
a = input("Are you busy.  (yes or no)")
while (a == "no"): 
    question_1()
    a = input("yes or no")
    if (a == "yes"):
        ans_1()
        f = f+1
        print("have you pulled up all your family members?")
        a = input("yes or no")
    else:
        question_2()
        a = input("yes or no")
        if (a == "yes"):
            question_5
            a = input("yes or no")
            if (a == "yes"):
                question_4
                a = input("yes or no")
                if(a == "yes"):
                    ans_3()
##ans_3=cat person
                  
                    d =d+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
                else:
                    ans_2()
#ans_2=dog person
                    c = c+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
                    
            else:
                question_6()
                a = input("yes or no")
                if(a == "yes"):
                    ans_2()
#ans_2=dog person
                    c = c+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
                else:
                    ans_3()
#ans_3=cat person
                    d = d+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
        else:
            question_3()
            a = input("yes or no")
            if(a == "yes"):
                question_6()
                a = input("yes or no")
                if(a == "yes"):
                    ans_2()
#ans_2=dog person
                    c = c+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
                else:
                    ans_3()
#ans_3=cat person
                    d =d+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
            else:
                question_4()
                a = input("yes or no")
                if(a == "yes"):
                    ans_3()
#ans_3=cat person
                  
                    d =d+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
                else:
                    ans_2()
#ans_2=dog person
                    c = c+1
                    print("have you pulled up all your family members?")
                    a = input("yes or no")
#family vote distribution
                   
else:
    print("family vote distribution")
    print("cat = ",c)
    print("dog = ",d)
    print("fish = ",f)
        
        
            
        








