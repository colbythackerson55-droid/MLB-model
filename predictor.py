team_ratings = {
    "Los Angeles Dodgers": 96,
    "Philadelphia Phillies": 94,
    "New York Yankees": 92,
    "Detroit Tigers": 90,
    "Houston Astros": 89,
    "Chicago Cubs": 88,
    "New York Mets": 88,
    "Milwaukee Brewers": 87,
    "Seattle Mariners": 86,
    "San Diego Padres": 86,
    "Toronto Blue Jays": 84,
    "Texas Rangers": 84,
    "Tampa Bay Rays": 83,
    "Boston Red Sox": 83,
    "San Francisco Giants": 82,
    "Cincinnati Reds": 81,
    "St. Louis Cardinals": 81,
    "Minnesota Twins": 80,
    "Kansas City Royals": 80,
    "Cleveland Guardians": 80,
    "Arizona Diamondbacks": 79,
    "Los Angeles Angels": 75,
    "Washington Nationals": 74,
    "Pittsburgh Pirates": 73,
    "Miami Marlins": 72,
    "Athletics": 71,
    "Baltimore Orioles": 70,
    "Atlanta Braves": 70,
    "Chicago White Sox": 65,
    "Colorado Rockies": 60
}

def predict_game(home_team, away_team):
    home_rating = team_ratings.get(home_team, 75) + 3  # Home-field advantage
    away_rating = team_ratings.get(away_team, 75)

    total = home_rating + away_rating

    home_pct = round(home_rating / total * 100, 1)
    away_pct = round(away_rating / total * 100, 1)

    winner = home_team if home_pct >= away_pct else away_team
    confidence = round(abs(home_pct - away_pct) / 5 + 5, 1)

    reasons = []

    if home_rating > away_rating:
        reasons.append("Better overall team rating")
        reasons.append("Home-field advantage")
    else:
        reasons.append("Stronger overall team")

    return {
        "winner": winner,
        "home_pct": home_pct,
        "away_pct": away_pct,
        "confidence": min(confidence, 10),
        "reasons": reasons
    }
