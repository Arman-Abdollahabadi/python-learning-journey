import random
list_1 = ['rock', 'paper', 'scissors']
print('Welcome to the Rock Paper Scissors Game, Its easy but fun')
knowledge = input('Are you familiar with this game? Type yes or no (or stop to quit): ').lower()
while knowledge not in['yes','no','stop']:
    print('❌ Invalid choice! Please type Yes, No or stop')
    knowledge = input('Try again: ').lower()
if knowledge == 'stop':
    print('🛑 Game stopped. Bye!')
    exit()
system_rank = 0
user_rank = 0
if knowledge == 'no':
    print("""
    Welcome to Rock, Paper, Scissors! 🪨📄✂️
    
    Rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    - Same choice = Draw
    """)
for round_num in range (1,6):
    system_choice = random.choice(list_1)
    user_choice = input('your turn, choose one: rock, paper or scissors (or stop): ').lower()
    while user_choice not in list_1 and user_choice != 'stop':
        print('❌ Invalid choice! Please type rock, paper or scissors.')
        user_choice = input('Try again: ').lower()
    if user_choice == 'stop':
        print('🛑 Game stopped.')
        break
    if (system_choice == 'rock' and user_choice == 'scissors') or (system_choice == 'paper' and user_choice == 'rock') or (system_choice == 'scissors' and user_choice == 'paper'):
        system_rank += 1
        print(f'system choice was {system_choice} and won this round, Results: pc: {system_rank} vs you: {user_rank}')
    elif (system_choice == 'scissors' and user_choice == 'rock') or (system_choice == 'rock' and user_choice == 'paper') or (system_choice == 'paper' and user_choice == 'scissors'):
        user_rank += 1
        print(f'system choice was {system_choice} and you won this round, Results: pc: {system_rank} vs you: {user_rank}')
    else :
        print(f'system choice was {system_choice} and you chose {user_choice}, so draw this round, Results: pc: {system_rank} vs you: {user_rank}')
if user_rank > system_rank:
    print('🎉 You won the game!')
elif user_rank < system_rank:
    print('🤖 PC  won the game!')
else:
    print("It's a tie! 🤝")
results = f'system: {system_rank} vs you: {user_rank}'
print(results)
