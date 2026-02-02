#!/usr/bin/env python3
import random

def create_board(size=100, special_percentage=0.25):
    """
    Creates a 1-D board represented by a list of integers.
    Index represents the space number.
    Value represents the rule: 0 for normal, +/- int for move rules.
    """
    
    board = [0] * (size + 1)

    num_special = int(size * special_percentage)
    
    available_spaces = list(range(2, size))
    
    special_indices = random.sample(available_spaces, num_special)
    
    for idx in special_indices:

        val = random.randint(-10, 10)
        while val == 0: 
            val = random.randint(-10, 10)
        board[idx] = val
        
    return board

def play_game():
    print("--- Virtual Board Game (Lab 2) ---")
    
    while True:
        try:
            num_players = int(input("Enter number of players (at least 2): "))
            if num_players >= 2:
                break
            print("Please enter at least 2 players.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    board_size = 100
    board = create_board(board_size, 0.25)
    
    player_positions = [1] * num_players
    game_over = False
    turn = 0
    
    while not game_over:
        current_player_idx = turn % num_players
        player_num = current_player_idx + 1
        
        roll = random.randint(1, 6)
        
        print(f"\n--- Player {player_num}'s Turn ---")
        
        print(f"Player {player_num} rolled a {roll}.")
        
        player_positions[current_player_idx] += roll
        current_pos = player_positions[current_player_idx]
        
        if current_pos >= board_size:
            print(f"Player {player_num} reached space {board_size}!")
            print(f"*** Player {player_num} WINS! ***")
            game_over = True
            break
            
        rule = board[current_pos]
        
        if rule != 0:
            if rule > 0:
                print(f"LADDER! Landed on special space {current_pos}. Moving forward {rule} spaces.")
            else:
                print(f"SNAKE! Landed on special space {current_pos}. Moving backward {abs(rule)} spaces.")
            
            player_positions[current_player_idx] += rule
            
            if player_positions[current_player_idx] < 1:
                player_positions[current_player_idx] = 1

        print(f"Player {player_num} is now at space {player_positions[current_player_idx]}.")
        
        if player_positions[current_player_idx] >= board_size:
            print(f"*** Player {player_num} WINS! ***")
            game_over = True
        
        turn += 1

if __name__ == "__main__":
    play_game()