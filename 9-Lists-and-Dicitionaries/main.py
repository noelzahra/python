from capitals import capitals_dict

for state in capitals_dict:
    city = capitals_dict.get(state)
    
    print(f"{city} is city of {state}")
    
    '''time python bash command
        time python main.py
    '''