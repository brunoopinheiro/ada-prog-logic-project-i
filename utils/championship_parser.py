from utils import match_analysis as ma


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
        partidas = input_json[rodada]
        n_partidas = partidas.keys()
        for partida in n_partidas:
            home, away = ma.match_analysis(n_partidas[partida])
            # Temporario
            output_table.append(home)
            output_table.append(away)

    return output_table
