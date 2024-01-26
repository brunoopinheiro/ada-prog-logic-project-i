def match_analysis(match: dict):
    """
    Recebe um dict da partida.
    Retorna uma tupla com o resultado da partida.
    """
    home_club = {"name": match["clubs"]["home"]}
    away_club = {"name": match["clubs"]["away"]}

    return (home_club, away_club)
    ...
