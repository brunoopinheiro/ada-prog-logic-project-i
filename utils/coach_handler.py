def coach_handler(team: dict, coach_name: str, points_obtained: int = 0):
    """
    Recebe o dict equivalente ao time,
    e o nome do técnico da partida.
    Ajusta a lista de técnicos,
    contando o número de partidas que o técnico participou.
    """
    coachs_list = team["coachs"]
    coachs = [coach["name"] for coach in coachs_list]
    if coach_name in coachs:
        coach_index = coachs.index(coach_name)
        coachs_list[coach_index]["matches"] += 1
        coachs_list[coach_index]["points_obtained"] += points_obtained

    else:
        team["coachs"].append(
            {"name": coach_name, "matches": 1, "points_obtained": points_obtained}
        )

    return team


def lasting_coach(club: dict):
    """
    Recebe o dicionário que representa um time,
    Retorna o objeto com o técnico mais duradouro
    no comando da equipe.
    """
    coachs = [(coach["name"], coach["matches"]) for coach in club["coachs"]]
    lasting_index = 0
    for index, (_coach, matches) in enumerate(coachs):
        if matches > coachs[lasting_index][1]:
            lasting_index = index

    return coachs[lasting_index]


def coachs_list(champ_table: list[dict]):
    """
    Recebe a tabela final do campeonato,
    retorna a lista de técnicos que participaram
    do campeonato.
    """
    c_list = []
    for team in champ_table:
        c_list.extend(team["coachs"])

    return c_list
