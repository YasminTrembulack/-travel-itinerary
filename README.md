Banco de dados(SQLlite)
https://dbeaver.io/download/

User Guide:
https://virtualenv.pypa.io/en/latest/user_guide.html

pip install virtualenv
python -m venv venv 
    Estamos nomeando o venv como "venv"
    Essa pasta venv serve para fazer intalar coisas que seram utilizadas sem necessariamente instalar na maquina, dessa forma deixando menos poluido

.\venv\Scripts\Activate
    trabalhar com diferentes locais de python

Framework Flask
https://pypi.org/project/Flask/

pip3 install Flask
    como estamos no ambiente virtual venv, quando instalamos, por exemplo o Flask ele na verdade está sendo instaladp dentro da pasta venv 

*** Quando criamos uma pasta em python criar um arquino __init__.py que possibilitara a importação e exportação de arquivos (ex de import: from src.main.server.server import app)

Dentro da pasta src/main/server etaram as configurações de servidor

### Para rodar o servidor:
python run.py

Configuro minha pasta .vscode no arquivo settings.json para tornar "invissivel" todos aqueles arquivos que estariam poluindo visualmente meu projeto