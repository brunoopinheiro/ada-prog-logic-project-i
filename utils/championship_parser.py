from utils import match_analysis as ma
from utils import table_list as tl


# Deve ser a funcao base que vai ler o input e retornar a tabela do campeonato
def championship_parser(input_json: dict):
    """
    Função principal do projeto.
    Recebe o dict de input do campeonato,
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
            # Temporario
            tl.table_list(home, output_table)
            tl.table_list(away, output_table)

    return output_table
