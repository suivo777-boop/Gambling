import random

options = ["rock", "paper", "scissors"]
play_again = input("Do you want to play rock, paper, scissors?: (yes/no): ").lower()



while play_again == "yes":
    score_computer = 0
    score_player = 0
    print("Let's play rock paper scissors! First to 3 wins!")
    
    while score_computer < 3 and score_player < 3: 
        user_choice = input("Choose rock, paper or scissors: ").lower()
        
        if user_choice not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
            
        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}!")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            score_player += 1
        else:
            print("You lose this round!")
            score_computer += 1
            
        print(f"Computer: {score_computer} ------ You: {score_player}")
        print()

    print("-" * 40)
    print(f"Final score: Computer: {score_computer} ------ You: {score_player}")
    
    if score_computer < score_player:
        print("Congratulations, you won the game!")
    elif score_computer > score_player:
        print("You lost the game, keep your head up!")
    else:
        print("It's a draw!")
    
    play_again = input("Do you want to play again?: (yes/no): ").lower()
    

print("Thanks for playing!")
print("BYE...")
