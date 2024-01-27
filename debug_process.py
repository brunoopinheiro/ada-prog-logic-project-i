import pandas as pd
from utils import championship_parser as cp
from utils import coach_handler as ch
import matplotlib.pyplot as plt


if __name__ == "__main__":
    input_json = pd.read_json("./input_files/brasileirao-2019.json").to_dict()
    tabela_brasileirao = cp.championship_parser(input_json)

    list_coachs = ch.coachs_list(tabela_brasileirao)
    x = [c["matches"] for c in list_coachs]
    y = [c["points_obtained"] for c in list_coachs]

    plt.figure(figsize=(8, 6))
    plt.title("Campeonato Brasileiro 2019 - Pontuação/Partidas no Comando")

    plt.scatter(x, y, alpha=0.5, c=y)
    plt.xlabel("Partidas no Comando do Time")
    plt.ylabel("Pontuação Obtida no Time")
    plt.xscale("linear")
    plt.show()
    # for i, coach in enumerate(list_coachs):
    #     print(f"{i + 1} - {coach}")
    # for i, team in enumerate(tabela_brasileirao):
    #     print(f"{i} - {team["name"]}:")
    #     print("Técnicos:")
    #     for coach in team["coachs"]:
    #         print(coach)
    #     print("------")
