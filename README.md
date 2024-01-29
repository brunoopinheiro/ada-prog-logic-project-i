# ada-prog-logic-project-i
Repositório para solução do projeto 1 de Lógica de Programação II do Santander Coders 2023.2 | Data Science pela Ada Tech

## Como executar o projeto

### Requisitos
Para executar o projeto localmente, você vai precisar garantir que tem as seguintes instalações feitas corretamente:
- Python 3.8 ou superior
- Pip 21 ou superior

### Instalação

**Mas pra quê isso tudo??**

Você pode executar todo o projeto, desde que tenha tanto o **Python**, quanto o **Pandas** e o **Matplot.lib** instalados na sua máquina. Para garantir que você não precise se preocupar com buscar essas dependências, instalar e talvez esquecer que elas estão ocupando espaço no disco da sua máquina, você pode usar um ambiente virtual, como explicado no tópico abaixo.
Quando se trabalha em projetos **Python**, é comum lidar com diferentes versões de bibliotecas e dependências. Para garantir um ambiente de desenvolvimento limpo e organizado, o **Python** oferece uma ferramenta integrada chamada **venv**, que permite criar ambientes virtuais isolados. Dessa forma, todas as dependências são instaladas na pasta `.venv`. Uma vez que você exclua o projeto da sua máquina, essas instalações são excluidas junto.

[**Mais informações!**](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/)

_Usando Powershell ou bash_
- Clone o repositório
- Na pasta raiz do projeto, crie um ambiente virtual para instalação das dependências com o comando `python -m venv .venv`
- Ative o ambiente virtual com o comando `.\venv\Scripts\activate.ps1`
  - Esse comando pode ter algumas diferenças dependendo do terminal utilizado para isso.
- Instale as dependências do `pandas` com o comando `pip install -r requirements.txt`

### Execução
O notebook chamado `projeto_brasileirao.ipynb` contem todo o passo a passo, desde a apresentação do problema, até a solução do projeto.

Por uma questão de organização, as bases de dados em `.json` estão contidas na pasta `./input_files`. Da mesma forma, as funções criadas para lidar com os dados, utilizadas no _notebook_ estão organizadas na pasta `./utils`.

Caso queira utilizar uma base de dados diferente da que está importada inicialmente no projeto, altere o caminho do arquivo e o ano referente ao campeonato na primeira célula de código do notebook, nas variáveis `input_file_path`, `year_championship`.
