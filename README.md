# ada-prog-logic-project-i
Repositório para solução do projeto 1 de Lógica de Programação II do Santander Coders 2023.2 | Data Science pela Ada Tech

## Como executar o projeto

### Requisitos
Para executar o projeto localmente, você vai precisar garantir que tem as seguintes instalações feitas corretamente:
- Python 3.8 ou superior
- Pip 21 ou superior

### Instalação
_Usando Powershell ou bash_
- Clone o repositório
- Na pasta raiz do projeto, crie um ambiente virtual para instalação das dependências com o comando `python -m venv .venv`
- Ative o ambiente virtual com o comando `.\venv\Scripts\activate.ps1`
  - Esse comando pode ter algumas diferenças dependendo do terminal utilizado para isso.
- Instale as dependências do `pandas` com o comando `pip install -r requirements.txt`

### Execução
O notebook chamado `projeto_brasileirao.ipynb` contem todo o passo a passo, desde a apresentação do problema, até a solução do projeto.

Por uma questão de organização, as bases de dados em `.json` estão contidas na pasta `./input_files`. Da mesma forma, as funções criadas para lidar com os dados, utilizadas no _notebook_ estão organizadas na pasta `./utils`.
