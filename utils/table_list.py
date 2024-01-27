from utils import coach_handler as ch
from functools import reduce


def apply_sorting(champ_table: list[dict], rule):
    return sorted(champ_table, key=rule, reverse=True)


def championship_result(champ_table: list[dict]):
    """
    Recebe a lista final do campeonato,
    ordena de acordo com os critérios estabelecidos:
    [pontos > nº vitorias > saldo de gols > gols pro]
    Retorna lista ordenada.
    """
    sorting_criteria = [
        lambda team: team["goals"],
        lambda team: team["goals_difference"],
        lambda team: team["wins"],
        lambda team: team["points"],
    ]
    sorted_table = reduce(apply_sorting, sorting_criteria, champ_table)
    return sorted_table


def table_list(team_update: dict, team_list: list = []):
    """
    Recebe as informações de um time pós partida,
    e uma lista de times.
    Atualiza a lista, garantindo a unicidade de cada time.
    """
    if len(team_list) == 0:
        team = ch.coach_handler(
            team_update, team_update["current_coach"], team_update["points"]
        )
        team_list.append(team)
        return team_list

    team_names = [team["name"] for team in team_list]
    if team_update["name"] in team_names:
        team_index = team_names.index(team_update["name"])
        team_to_update = team_list[team_index]
        team_to_update["points"] += team_update["points"]
        team_to_update["goals"] += team_update["goals"]
        team_to_update["goals_taken"] += team_update["goals_taken"]
        team_to_update["wins"] += team_update["wins"]
        team = ch.coach_handler(
            team_to_update, team_update["current_coach"], team_update["points"]
        )
        team_list[team_index] = team
        return team_list
    else:
        team = ch.coach_handler(
            team_update, team_update["current_coach"], team_update["points"]
        )
        team_list.append(team_update)
        return team_list


def goals_difference(team: dict):
    """
    Recebe o dict de um time,
    e calcula o saldo de gols de cada time,
    adicionando ao dict correspondente.
    """
    difference = team["goals"] - team["goals_taken"]
    team["goals_difference"] = difference
    return team
