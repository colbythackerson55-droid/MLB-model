import requests
def get_team_stats():
    url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104"
    data = requests.get(url).json()

    teams = {}

    for record in data["records"]:
        for team in record["teamRecords"]:

            name = team["team"]["name"]

            wins = team["wins"]
            losses = team["losses"]
            win_pct = float(team["winningPercentage"])

            runs_scored = team["runsScored"]
            runs_allowed = team["runsAllowed"]

            run_diff = runs_scored - runs_allowed

            teams[name] = {
                "win_pct": win_pct,
                "run_diff": run_diff,
                "wins": wins,
                "losses": losses
            }

    return teams


def predict_game(home_team, away_team):

    teams = get_team_stats()

  home = None
away = None

for name in teams:
    if home_team.lower() in name.lower():
        home = teams[name]

    if away_team.lower() in name.lower():
        away = teams[name] 

    if not home or not away:
        return {
            "error": "Team not found in live MLB data"
        }

    home_score = home["win_pct"] + (home["run_diff"] * 0.001)
    away_score = away["win_pct"] + (away["run_diff"] * 0.001)

    # home field advantage
    home_score += 0.02

    total = home_score + away_score

    home_pct = round((home_score / total) * 100, 1)
    away_pct = round((away_score / total) * 100, 1)

    if home_pct > away_pct:
        winner = home_team
    else:
        winner = away_team

    confidence = round(abs(home_pct - away_pct) / 10, 1)

    reasons = []

    if home["win_pct"] > away["win_pct"]:
        reasons.append("Better win percentage")
    else:
        reasons.append("Underdog advantage for away team")

    if home["run_diff"] > away["run_diff"]:
        reasons.append("Better run differential")

    if home_score > away_score:
        reasons.append("Overall statistical edge")

    return {
        "winner": winner,
        "home_pct": home_pct,
        "away_pct": away_pct,
        "confidence": min(confidence, 10),
        "reasons": reasons
    }
