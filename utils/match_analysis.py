def match_analysis(match: dict):
    """
    Recebe um dict da partida.
    Retorna uma tupla com o resultado da partida.
    """
    home_club = {
        "name": match["clubs"]["home"],
        "points": 0,
        "goals": int(match["goals"]["home"]),
        "current_coach": match["coach"]["home"],
        "coachs": [],
        "goals_taken": int(match["goals"]["away"]),
        "wins": 0,
    }
    away_club = {
        "name": match["clubs"]["away"],
        "points": 0,
        "goals": int(match["goals"]["away"]),
        "current_coach": match["coach"]["away"],
        "coachs": [],
        "goals_taken": int(match["goals"]["home"]),
        "wins": 0,
    }

    if home_club["goals"] > away_club["goals"]:
        home_club["points"] = 3
        home_club["wins"] = 1
    elif home_club["goals"] < away_club["goals"]:
        away_club["points"] = 3
        away_club["wins"] = 1
    else:
        home_club["points"] = 1
        away_club["points"] = 1

    return (home_club, away_club)
    ...
