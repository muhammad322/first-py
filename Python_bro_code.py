import random
choices = ["rock","scissors","paper"]
computer_choice = random.choice(choices)
user_choice = ""
while True:
    user = input("1 for rock, 2 for , 3 for scissors: ")
    if user == "":
      print("try again")
    
    elif user.isalpha() != False:
      print("try again")
    elif user.isspace() != False:
        print("try again")
    if user.isnumeric() == True:
       user = int(user)
       if user == 0:
           print("try again")
       elif user > 3:
           print("try again")
       else:
            break
         

    

        

if user == 1:
    user_choice = "rock"
elif user == 2:
    user_choice = "paper"
elif user == 3:
    user_choice = "scissors"
if computer_choice == user_choice:
        print("u lose")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "scissors" and user_choice == "paper":
        print("u lose")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "paper" and user_choice == "scissors":
        print("u win")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "scissors" and user_choice == "rock":
        print("u win")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "rock" and user_choice == "scissors":
        print("u lose")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "rock" and user_choice == "paper":
        print("u win")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        
elif computer_choice == "paper" and user_choice == "rock":
        print("u lose")
        print("the computer choose: "+computer_choice)
        print("you choose: "+user_choice)
        


    