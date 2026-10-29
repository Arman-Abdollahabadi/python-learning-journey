# 🎯 Number Guessing Game

My first Python program! The computer picks a random number between 1 and 20.
You have **5 attempts** to find it, with a hint after each guess.

## 🕹️ How it works
1. Press Enter to start
2. Enter a number between 1 and 20
3. The game tells you if the secret number is **bigger** or **smaller**
4. Find it within 5 attempts to win 🎉

## 🧠 Concepts practiced
- `random.randint()` to generate a random number
- `input()` and `int()` for user input
- `for` loop with `range()`
- `if / elif / else` conditions
- `break` to stop the loop when the player wins
- `for ... else` to detect when the player runs out of attempts
- f-strings for formatted output

## ▶️ How to run
    python number_guessing.py

## 🚀 Next improvements
- [ ] Handle invalid input (letters) with `try / except`
- [ ] "Play again?" option
- [ ] Difficulty levels (easy / medium / hard)
