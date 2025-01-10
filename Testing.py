import random
is_running = True
choices = ["rock", "paper", "scissors"]
winning_moves = {"rock":"scissors", "paper":"rock", "scissors":"paper"}

print("Welcome to Rock, Paper, Scissors")
while is_running:
    while True:
        user_input = input("Enter your move: ")
        if user_input in choices:
            bot_choice = random.choice(choices)
            break
        else:
            print("Enter a valid move")

    print(f"You choose {user_input}. Bot choose {bot_choice}")
    if user_input == bot_choice:
        print("It's a tie")
    elif winning_moves[user_input] == bot_choice:
        print("You win!")
    else:
        print("You lose!")

    while True:
        user_input = input("Play again? Y/N: ").lower()
        if user_input in ['yes', 'y']:
            break
        elif user_input in ['no', 'n']:
            print("Thanks for playing!")
            is_running = False
            break
        else:
            print("Yes or No only!")

odd_numbers = [i for i in range(20) if i % 2 != 0]
even_numbers = [i for i in range(1, 20) if i % 2 == 0]

print("Odd: ")
print(', '.join(str(x) for x in odd_numbers))
print("Even: ")
print(', '.join(str(x) for x in even_numbers))

print("This is an experiment from feature Branch")
