#to ask random number from system, we should import random
import random
secret = random.randint(1,20)

print("How lucky are you? Find the secret number in 5 attempts!")
input("Are you ready? If yes, press Enter... :D ")

for attempt in range(1,6):
    user_guess = int(input(f"Attempt {attempt}/5 - enter a number between 1 and 20: "))
    
    if user_guess > secret:
        print("The secret number is SMALLER than your guess...")
    elif user_guess < secret:
        print("The secret number is BIGGER than your guess...")
    else:
        print("WOW, YOU WIN!  🎉  ")
        print(f"the secret number was {secret}, and you found it in {attempt} attempts.")
        break
else:
    print(f"You are out of attempts. The number was {secret}. Maybe next time!")


                 