__author__ = 'Prateek Sohlot'

import json
from Lab1_Agents_Task2_Deck import Deck
from Lab1_Agents_Task2_Agents import randomAgent, reflexAgent, fixedAgent


def play_game(player1, player2):
    bids = {player1.name: [],player2.name: [], 'winning':[]}

    # we play 50 rounds
    for _ in range(50):

        player1.updateHand(Deck().deal_cards())
        player2.updateHand(Deck().deal_cards())

        total = 0
        # we have 3 rounds of bidding
        for idx in range(3):
            print(f'Staring round {idx+1}')
            bid1 = player1.calculateBid()
            print(f'{player1.name} bid {bid1}')
            bid2 = player2.calculateBid()
            print(f'{player2.name} bid {bid2}', '\n')            
            total += bid1 + bid2

        #########################
        # phase 2:  Showdown and Hand Analysis   #
        #########################
        winner = ' '

        print('*'*50)
        print("Analysing player1's hand :", player1.hand)
        analysis1 = player1.identifyHand()
        print(f'{player1.name} has {analysis1["category"]}')
        print(f'{player1.name} has {sorted(analysis1["rank"], reverse = True)}')
        print('*'*50)

        print('*'*50)
        print("Analysing player2's hand :", player2.hand)
        analysis2 = player2.identifyHand()
        print(f'{player2.name} has {analysis2["category"]}')
        print(f'{player2.name} has {sorted(analysis2["rank"], reverse= True)}')
        print('*'*50)

        if analysis1["cards"][0][2] > analysis2["cards"][0][2]:
            winner = player1.name
        elif analysis1["cards"][0][2] < analysis2["cards"][0][2]:
            winner = player2.name

        else:
            
            if sorted(analysis1['rank'])[0][2] > sorted(analysis2['rank'])[0][2]:
                winner = player1.name

            else:
                winner = player2.name

        print('*'*50)
        print("The winner is:", winner)
        print('*'*50)

        if winner == player1.name:
            bids[player1.name].append(total)
            bids[player2.name].append(0)
        elif winner == player2.name: 
            bids[player1.name].append(0) 
            bids[player2.name].append(total)

    print('*'*50)
    print(f'{player1.name} is a {player1.type}')     
    print(f'The number of games won by {player1.name} are {len(list(filter(None, bids[player1.name])))}')
    print("Total winning bids for player1:", sum(bids[player1.name]))
    print(f'{player2.name} is a {player2.type}')
    print(f'The number of games won by {player2.name} are {len(list(filter(None, bids[player2.name])))}')
    print("Total winning bids for player2:", sum(bids[player2.name]))

    return bids



if __name__ == '__main__':

    player1 = fixedAgent('Prateek')
    player2 = randomAgent('Yuntao')

    result = play_game(player1, player2)
    
    print(player1.type, 'vs', player2.type)
    with open(f'{player1.type}Vs{player2.type}.json', "w") as outfile:
        json.dump(result, outfile)