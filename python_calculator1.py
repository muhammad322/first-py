choices = ["A","B","C","D"]

def game():
    score = 0
    user_input1 = None
    ans1 = "D"
    while True:
        user_input1 = input("how many provinces does pakistan have?\nA)1\nB)3\nC)7\nD)5\nAns: ").upper()
        if user_input1 not in choices:
            print("please re enter")
        else:
            break
    if user_input1 == ans1:
        score = score + 1
    user_input2 = None
    ans2 = "D"
    while True:
        user_input2 = input("what is the name of the cureent pm of india?\nA)satya gopal\nB)arnab goswami\nC)vijay maliya\nD)narendar modi\nAns: ").upper()
        if user_input2 not in choices:
            print("please re enter")
        else:
            break
    if user_input2 == ans2:
        score = score + 1
    
    user_input3 = None
    ans3 = "C"
    while True:
        user_input3 = input("who is russia at war with right now?\nA)usa\nB)india\nC)ukraine\nD)china\nAns: ").upper()
        if user_input3 not in choices:
            print("please re enter")
        else:
            break
    if user_input3 == "C":
        score = score + 1
    
    user_input4 = None
    ans4 = "B"
    while True:
        user_input4 = input("who has the most subscribers on youtube?\nA)pewdiepie\nB)T series\nC)mr beast\nD)dude perfect\nAns: ").upper()
        if user_input4 not in choices:
            print("please re enter")
        else:
            break
    if user_input4 == ans4:
        score = score + 1
    print("the quiz has ended here is your score: {}".format(score))
    user_ans = [user_input1,user_input2,user_input3,user_input4]
    print("your answers were: ")
    for i in user_ans:
        print(i, end=",")
    print()
    actual_ans = [ans1,ans2,ans3,ans4]
    print("the actual answers were: ")
    for i in actual_ans:
        print(i, end=",")
    print()   

while True:
    lol = input("welcome to my quiz! press enter when you are ready to begin " )
    if lol == "":
        game()
        break
    else:
        print("whenever your ready...")
choice = None
while True:
    choice = input("would you like to play again?(yes/no) ").lower()
    if choice != "yes":
        print("see ya!")
        break
    else:
        game()






   


   





    