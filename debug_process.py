import pandas as pd
from utils import championship_parser as cp
from utils import coach_handler as ch


if __name__ == "__main__":
    input_json = pd.read_json("./input_files/brasileirao-2019.json").to_dict()
    tabela_br = cp.championship_parser(input_json)

    coaches = [ch.lasting_coach(club) for club in tabela_br]
    print(coaches)
    # for team in tabela_br:
    #     print(team)
    #     print("----")
