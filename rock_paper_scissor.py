"""
Create a Rock Paper Scissors game where the player inputs their choice and plays against a computer that randomly selects its move, 
with the game showing who won each round. Add a score counter that tracks player and computer wins,
and allow the game to continue until the player types ‘quit’.
"""
import random       
def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the player's and computer's choices."""
    if player_choice == computer_choice:
        return 'tie'
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'player'
    else:
        return 'computer'
    # //create a function to play the game.
def play_game():    
    """Play the Rock Paper Scissors game."""
    player_score = 0
    computer_score = 0
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        print(f"Score - Player: {player_score}, Computer: {computer_score}")

    # Display final scores
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()