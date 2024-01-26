import pandas as pd
from utils import championship_parser as cp


if __name__ == "__main__":
    input_json = pd.read_json("./input_files/brasileirao-2019.json").to_dict()
    tabela_br = cp.championship_parser(input_json)
    tabela_ord = sorted(tabela_br, key=lambda time: time["points"], reverse=True)
    for team in tabela_ord:
        print(team)
