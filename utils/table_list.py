from utils import coach_handler as ch


def table_list(team_update: dict, team_list: list = []):
    """
    Recebe as informações de um time,
    e uma lista de times.
    Atualiza a lista, garantindo a unicidade de cada time.
    """
    if len(team_list) == 0:
        team = ch.coach_handler(team_update, team_update["current_coach"])
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
        team = ch.coach_handler(team_to_update, team_update["current_coach"])
        team_list[team_index] = team
        return team_list
    else:
        team = ch.coach_handler(team_update, team_update["current_coach"])
        team_list.append(team_update)
        return team_list
