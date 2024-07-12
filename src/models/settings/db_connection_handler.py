#gerente de conexão do banco de dados
import sqlite3 
#para se conetar ao banco SQLite
from sqlite3 import Connection

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        #String de conexão com o SQLite(coloca o caminho do banco, mas como o nosso já está na raiz do projeto é só colocar o nome)
        self.__conn = None
        #vai mudar com o tempo pois vamos adicionar a conexão aqui

    def connect(self) -> None:
        # -> None: mostra que a gente não vai retornar nada
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        #check_same_thread=False:para usar a conexão em varios lugares do projeto
        self.__conn = conn
    
    def get_connection(self) -> Connection:
        #-> Connection: mostra que vou retorar um elemento do tipo connection
        return self.__conn
        
db_connection_handler = DbConnectionHandler()
