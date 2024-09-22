import random

# start

player1: str = str(input('what is the name of player1?'))
player2: str = str(input('what is the name of player2?'))
player3: str = str(input('what is the name of player3?'))
player4: str = str(input('what is the name of player4?'))

winner_player: str = random.choice([player1, player2, player3, player4])
print(f'random winner player is: {winner_player:}')

# stop
