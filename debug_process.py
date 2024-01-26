import pandas as pd
from utils import championship_parser as cp


if __name__ == "__main__":
    input_json = pd.read_json("./input_files/brasileirao-2019.json").to_dict()
    tabela_brasileirao = cp.championship_parser(input_json)
    print(tabela_brasileirao)
