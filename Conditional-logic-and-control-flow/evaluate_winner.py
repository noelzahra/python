#Evaluate winner in two different sports

sport = "Golf"
scores = {
    "p1_score": 10,
    "p2_score" : 9
}

def sport_name(sport, player_scores):
    sport_str = None
    if sport.lower() == "golf":
        winner = min(player_scores)
        sport_str = f"In {sport.capitalize()}, winner is {winner}"
    elif sport.lower() == "basketball":
        winner = max(player_scores)
        sport_str = f"In {sport.capitalize()}, winner is {winner}"
    else:
        sport_str = "Not listed"
    return sport_str
    
sports = ["Golf", "BasketBall", "Sailing"]


for sport in sports:
    print(sport_name(sport, scores))