def coach_handler(team: dict, coach_name: str):
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

    else:
        team["coachs"].append({"name": coach_name, "matches": 1})

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
