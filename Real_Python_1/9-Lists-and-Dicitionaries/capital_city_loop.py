from capitals import capitals_dict
import random


def capital_guess(state, capital):
        tries = 0
        while tries < 3:
            guess = raw_input("The capital of \'{}\'?".format(state.lower()))
            if guess == "exit":
                    print "The capital of {} is {}".format(state.upper(),
                                                           capital)
                    print "Goodbye"
                    break
            elif guess == capital.lower() or capital.capitalize():
                    print "Correct"
                    break
            else:
                    print "Try again"
                    tries += 1

state = random.choice(capitals_dict.keys())
capital = capitals_dict[state]
capital_guess(state, capital)
