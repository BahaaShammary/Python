#!/usr/bin/env python
# coding: utf-8

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# 
# Remember the rules:
# 
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# In[ ]:


keep_playing = True
while keep_playing:
    player1 = input("Player 1 - Please enter (rock/paper/scissors) ")
    player2 = input("Player 2 - Please enter (rock/paper/scissors) ")
    if player1 == player2:
        print("Draw")
    elif player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins")
    elif player2 == 'rock' and player1 == 'scissors':
        print("Player 2 wins")
    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 wins")
    elif player2 == 'scissors' and player1 == 'paper':
        print("Player 2 wins")
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins")
    elif player1 == 'rock' and player2 == 'paper':
        print("Player 2 wins")

    continue_playing = input('Would you like to keep playing? ')
    if continue_playing == 'no':
        print('Thanks for playing - Bye')
        keep_playing = False
    else:
        keep_playing = True


# In[ ]:




