from capitals import capitals_dict
import random


def capital_guess(state, capital):
        tries = 0
        while tries < 3:
            guess = input(f"The capital of {state}?")
            if guess == "exit":
                    print (f"The capital of {state.upper()} is {capital}")
                    print ("Goodbye")
                    break
            elif guess == capital.lower() or capital.capitalize():
                    print ("Correct")
                    break
            else:
                    print ("Try again")
                    tries += 1

state = random.choice(list(capitals_dict.items()))
capital = capitals_dict.get(state)
capital_guess(state, capital)

