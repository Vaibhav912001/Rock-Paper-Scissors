import random 
input_list = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''' , 
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']

while True:

    user_input = input("What would you like to choose? Rock, Paper or Scissors ")
    computer_choice = random.choice(input_list)

    if user_input == "Rock":
        if computer_choice == input_list[0]:
            print(f"Your choice is Rock \n {input_list[0]}")
            print(f"Computer's Choice is also Rock \n {input_list[0]}")
            print("It's a draw")
        
        elif computer_choice == input_list[1]:
            print(f"Your choice is Rock \n {input_list[0]}")
            print(f"Computer's Choice is Paper \n {input_list[1]}")
            print("You lose")
        
        else:
            print(f"Your choice is Rock \n {input_list[0]}")
            print(f"Computer's Choice is Scissors \n {input_list[2]}")
            print("You Won!")
            
    elif user_input == "Paper":
        if computer_choice == input_list[0]:
            print(f"Your choice is Paper \n {input_list[1]}")
            print(f"Computer's Choice is Rock \n {input_list[0]}")
            print("You Won!")
            
        elif computer_choice == input_list[1]:
            print(f"Your choice is Paper \n {input_list[1]}")
            print(f"Computer's Choice is also Paper \n {input_list[1]}")
            print("It's a Draw")
            
        else:
            print(f"Your choice is Paper \n {input_list[1]}")
            print(f"Computer's Choice is Scissors \n {input_list[2]}")
            print("You lose.")
            
    else:
        if computer_choice == input_list[0]:
            print(f"Your choice is Scissors \n {input_list[2]}")
            print(f"Computer's Choice is Rock \n {input_list[0]}")
            print("You lose.")
            
        elif computer_choice == input_list[1]:
            print(f"Your choice is Scissors \n {input_list[2]}")
            print(f"Computer's Choice is Paper \n {input_list[1]}")
            print("You Won")
            
        else:
            print(f"Your choice is Scissors \n {input_list[2]}")
            print(f"Computer's Choice is also Scissors \n {input_list[2]}")
            print("It's a draw.")
