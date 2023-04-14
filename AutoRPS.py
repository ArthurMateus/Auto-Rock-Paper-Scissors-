from random import randint
from colorama import Fore
from time import sleep

def players():
    #Lists for Data
    results = list()
    chosen = list()
    #Checking the amount of games wanted to be tested
    amount = int(input(Fore.GREEN + 'How many games do you want to be played? ' + Fore.RESET))
    print('Games Are Being Played. . .')
    sleep(4)
    gP = 0 
    #Loop to be played
    while gP < amount:
        #Choosing the thing
        p1 = randint(1,3)
        if p1 == 1:
            chosen.append('Paper')
        if p1 == 2:
            chosen.append('Scisors')
        if p1 == 3:
            chosen.append('Rock')
        p2 = randint(1,3)
        if p2 == 1:
            chosen.append('Paper')
        if p2 == 2:
            chosen.append('Scisors')
        if p2 == 3:
            chosen.append('Rock')
        #Checking who won
        if p1 == 1 and p2 == 1 or p1 == 2 and p2 == 2 or p1 == 3 and p2 == 3:
                results.append('Draw')
        elif p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2:
            results.append('P1 wins')
        elif p2 == 1 and p1 == 3 or p2 == 2 and p1 == 1 or p2 == 3 and p1 == 2:
            results.append('P2 wins')

        #Adding to the score
        gP += 1
    #Checking percentages

    rp1 = results.count('P1 wins') / len(results) * 100
    rp2 = results.count('P2 wins') / len(results) * 100
    rd = results.count('Draw') / len(results) * 100

    rpa = chosen.count('Paper') / len(chosen) * 100 
    rsc = chosen.count('Scisors') / len(chosen) * 100 
    rro = chosen.count('Rock') / len(chosen) * 100 
    #Printing out Results

    print(Fore.LIGHTBLUE_EX + 'Results are in!')
    sleep(1)
    print(f'The amount of games played was {amount}, in which:')
    sleep(.5)

    print(Fore.BLUE + f'{results.count("P1 wins")} Games were won by player 1, or about {round(rp1)}% of the time')
    sleep(1)
    print(Fore.RED + f'{results.count("P2 wins")} Games were won by player 2, or about {round(rp2)}% of the time')
    sleep(1)
    print(Fore.YELLOW + f'{results.count("Draw")} Games were a Draw, or about {round(rd)}% of the time')
    sleep(1)

    print(Fore.MAGENTA + f'Paper was played {chosen.count("Paper")} times, or about {round(rpa)}% of the time')
    sleep(1)
    print(f'Scisors was played {chosen.count("Scisors")} times, or about {round(rsc)}% of the time')
    sleep(1)
    print(f'Rock was played {chosen.count("Rock")} times, or about {round(rro)}% of the time')
    print(Fore.RESET)
    
players()