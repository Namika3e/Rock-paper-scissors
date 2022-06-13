import random

# a dictionary to hold elements for the game
game = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}

# list of option that will run or end the loop
option = ['y', 'n']

# message to be printed after every game
msg = 'Player({}) ; CPU({})'

# loop starts
i = 0
while i < 1:

# gets input from Player
    ask_p1 = input('Enter R for rock, P for paper, S for scissors : ').title()

# get random selection for CPU
    ask_com = random.choice(list(game))
    
# conditions for the game
    if ask_p1 in game:

# condition for a draw, if true then run loop again
        if ask_p1 == ask_com:
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Draw')
            ask_p1

# condition for a win, if true then ask to continue or stop loop
        elif (ask_p1 == 'P') & (ask_com == 'R'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner Player')
            play_again = input('Play again? \'y\' for Yes and \'n\' for No : ').lower()

# stops loop by choosing n and continue by choosing y
            if play_again == option[0]:
                ask_p1
            elif play_again == option[1]:
                i += 1
            else:
                print('An error occured: input either y or n')

# condition for a lose, if true then run the loop again            
        elif (ask_p1 == 'S') & (ask_com == 'R'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner CPU')
            ask_p1

# condition for a win, if true then ask to continue or stop loop
        elif (ask_p1 == 'R') & (ask_com == 'S'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner Player')
            play_again = input('Play again? \'y\' for Yes and \'n\' for No : ').lower()

# stops loop by choosing n and continue by choosing y
            if play_again == option[0]:
                ask_p1
            elif play_again == option[1]:
                i += 1
            else:
                print('An error occured: input either y or n')

# condition for a win, if true then ask to continue or stop loop
        elif (ask_p1 == 'S') & (ask_com == 'P'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner Player')
            play_again = input('Play again? \'y\' for Yes and \'n\' for No : ').lower()

# stops loop by choosing n and continue by choosing y
            if play_again == option[0]:
                ask_p1
            elif play_again == option[1]:
                i += 1
            else:
                print('An error occured: input either y or n')

# condition for a lose, if true then run the loop again
        elif (ask_p1 == 'R') & (ask_com == 'P'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner CPU')
            ask_p1

# condition for a lose, if true then run the loop again
        elif (ask_p1 == 'P') & (ask_com == 'S'):
            print(msg.format(game[ask_p1], game[ask_com]))
            print('Winner CPU')
            ask_p1

# condition for if a Player inputs a letter that is not a key in the game dictionary            
    else: 
        print('An error ocurred : input not recognised')