from utils import match_analysis as ma
from utils import table_list as tl


# Deve ser a funcao base que vai ler o input e retornar a tabela do campeonato
def championship_parser(input_json: dict):
    """
    Função principal do projeto.
    Recebe o dataframe de input do campeonato,
    e monta a tabela final com a classificação dos times.
    Output ordenado seguindo os critérios de classificação do campeonato.
    """
    output_table = []
    rodadas = input_json.keys()
    for rodada in rodadas:
        partidas: dict = input_json[rodada]
        chave_partidas = partidas.keys()
        for partida in chave_partidas:
            partida_atual = partidas[partida]
            home, away = ma.match_analysis(partida_atual)
            tl.table_list(home, output_table)
            tl.table_list(away, output_table)

    complete_table = [tl.goals_difference(team) for team in output_table]
    ordered_table = tl.championship_result(complete_table)

    return ordered_table
