# 🪨📄✂️ Rock Paper Scissors

Play 5 rounds of Rock Paper Scissors against the computer in the terminal.
The score is shown after every round, and the final winner at the end.

## 🕹️ How it works

1. Tell the game if you know the rules (if not, they are shown)
2. Each round, type `rock`, `paper` or `scissors`
3. The computer picks randomly, and the round winner gets 1 point
4. Type `stop` anytime to end the game early
5. After 5 rounds, the winner is announced 🎉

## 🧠 Concepts practiced

- Lists and `random.choice()`
- `input()` with `.lower()` for case-insensitive input
- `for` loop for rounds, `while` loop for input validation
- `in` / `not in` to check valid choices
- Complex conditions with `and` / `or`
- `break` and `exit()` to stop the game
- Score counting with variables

## ▶️ How to run

    python rock_paper_scissor.py

## 🚀 Next improvements

- [ ] "Play again?" option
- [ ] Use a dictionary to simplify the win rules
- [ ] Best-of-N mode (first to 3 wins)
