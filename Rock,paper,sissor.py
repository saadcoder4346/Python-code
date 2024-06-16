import random
lsit=["rock","paper","scissor"]
user_input=input(f"choose wat u wnna throw:{lsit}\n".lower())
computer_input=random.choice(lsit)
if(user_input==computer_input):
    print("tie")
elif(user_input=="rock" and computer_input=="scissor"):
    print("user wins")  
elif(user_input=="paper" and computer_input=="rock"):
    print("user wins")  
elif(user_input=="scissor" and computer_input=="paper"):
    print("user winss")
elif user_input not in lsit:
    print("pls throw somehting valid")    
else:
    print("computer wins")           
 
