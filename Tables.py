import mysql.connector
from mysql.connector import errorcode

table = {

    'MOTOR_GRAFICO': (
        """CREATE TABLE MOTOR_GRAFICO (
        ID_Motor INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Motor VARCHAR(255),
        Versao INTEGER
        )ENGINE=InnoDB"""),

    'PLATAFORMA': (
        """CREATE TABLE PLATAFORMA (
        ID_Plataforma INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Plataforma VARCHAR(255)
        )ENGINE=InnoDB"""),

    'ITEM': (
        """CREATE TABLE ITEM (
        ID_Item INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Item VARCHAR(255),
        Raridade VARCHAR(255),
        Pontos_Oferecidos INTEGER
        )ENGINE=InnoDB"""),

    'ESPECIALIDADE': (
        """CREATE TABLE ESPECIALIDADE (
        ID_Especialidade INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Especialidade VARCHAR(255)
        )ENGINE=InnoDB"""),

    'DESENVOLVEDOR': (
        """CREATE TABLE DESENVOLVEDOR (
        ID_Desenvolvedor INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Desenvolvedor VARCHAR(255),
        Data_Contratacao TIMESTAMP,
        ID_Supervisor INTEGER,
        FOREIGN KEY (ID_Supervisor) 
            REFERENCES DESENVOLVEDOR(ID_Desenvolvedor)
            ON DELETE SET NULL
        )ENGINE=InnoDB"""),

    'JOGADOR': (
        """CREATE TABLE JOGADOR (
        ID_Jogador INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nickname VARCHAR(255),
        Email VARCHAR(255),
        Data_Cadastro TIMESTAMP
        )ENGINE=InnoDB"""),

    'LOJA': (
        """CREATE TABLE LOJA (
        ID_Loja INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Loja VARCHAR(255)
        )ENGINE=InnoDB"""),

    'MARCADOR': (
        """CREATE TABLE MARCADOR (
        ID_Marcador INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Marcador VARCHAR(255)
        )ENGINE=InnoDB"""),

    'JOGO': (
        """CREATE TABLE JOGO (
        ID_Jogo INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Jogo VARCHAR(255),
        Genero_Jogo VARCHAR(255),
        Data_Lancamento TIMESTAMP,
        FK_MOTOR_GRAFICO_ID_Motor INTEGER,
        FOREIGN KEY (FK_MOTOR_GRAFICO_ID_Motor)
            REFERENCES MOTOR_GRAFICO (ID_Motor)
            ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'FASE': (
        """CREATE TABLE FASE (
        ID_Fase INTEGER AUTO_INCREMENT PRIMARY KEY,
        Nome_Fase VARCHAR(255),
        Dificuldade_Fase VARCHAR(255),
        FK_JOGO_ID_Jogo INTEGER,
        FOREIGN KEY (FK_JOGO_ID_Jogo)
            REFERENCES JOGO (ID_Jogo)
            ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Supervisao' : (
        """CREATE TABLE Supervisao (
        fk_DESENVOLVEDOR_ID_Desenvolvedor INTEGER,
        fk_DESENVOLVEDOR_ID_Desenvolvedor_ INTEGER,
        PRIMARY KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor_, fk_DESENVOLVEDOR_ID_Desenvolvedor),
        FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor),
        FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor_)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor)
        )ENGINE=InnoDB"""),

    'Lancamento': (
        """CREATE TABLE Lancamento (
        fk_JOGO_ID_Jogo INT,
        fk_PLATAFORMA_ID_Plataforma INT,
        PRIMARY KEY (fk_JOGO_ID_Jogo, fk_PLATAFORMA_ID_Plataforma),
        FOREIGN KEY (fk_JOGO_ID_Jogo) REFERENCES JOGO(ID_Jogo) ON DELETE CASCADE,
        FOREIGN KEY (fk_PLATAFORMA_ID_Plataforma) REFERENCES PLATAFORMA(ID_Plataforma) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Especialidade_Desenvolvedor': (
        """CREATE TABLE Especialidade_Desenvolvedor (
        fk_ESPECIALIDADE_ID_Especialidade INT,
        fk_DESENVOLVEDOR_ID_Desenvolvedor INT,
        PRIMARY KEY (fk_ESPECIALIDADE_ID_Especialidade, fk_DESENVOLVEDOR_ID_Desenvolvedor),
        FOREIGN KEY (fk_ESPECIALIDADE_ID_Especialidade) REFERENCES ESPECIALIDADE(ID_Especialidade) ON DELETE CASCADE,
        FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor) REFERENCES DESENVOLVEDOR(ID_Desenvolvedor) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Fase_Item': (
        """CREATE TABLE Fase_Item (
        fk_FASE_ID_Fase INT,
        fk_ITEM_ID_Item INT,
        PRIMARY KEY (fk_FASE_ID_Fase, fk_ITEM_ID_Item),
        FOREIGN KEY (fk_FASE_ID_Fase) REFERENCES FASE(ID_Fase) ON DELETE CASCADE,
        FOREIGN KEY (fk_ITEM_ID_Item) REFERENCES ITEM(ID_Item) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Jogo_Desenvolvedor': (
        """CREATE TABLE Jogo_Desenvolvedor (
        fk_DESENVOLVEDOR_ID_Desenvolvedor INT,
        fk_JOGO_ID_Jogo INT,
        Funcao_no_Projeto VARCHAR(100),
        PRIMARY KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor, fk_JOGO_ID_Jogo),
        FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor) REFERENCES DESENVOLVEDOR(ID_Desenvolvedor) ON DELETE CASCADE,
        FOREIGN KEY (fk_JOGO_ID_Jogo) REFERENCES JOGO(ID_Jogo) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Venda': (
        """CREATE TABLE Venda (
        ID_Venda INT AUTO_INCREMENT PRIMARY KEY,
        Data_Venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Valor_Venda DECIMAL(10, 2) NOT NULL,
        fk_LOJA_ID_Loja INT,
        fk_JOGADOR_ID_Jogador INT,
        fk_JOGO_ID_Jogo INT,
        FOREIGN KEY (fk_LOJA_ID_Loja) REFERENCES LOJA(ID_Loja) ON DELETE SET NULL,
        FOREIGN KEY (fk_JOGADOR_ID_Jogador) REFERENCES JOGADOR(ID_Jogador) ON DELETE CASCADE,
        FOREIGN KEY (fk_JOGO_ID_Jogo) REFERENCES JOGO(ID_Jogo) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Avaliacao': (
        """CREATE TABLE Avaliacao (
        ID_Avaliacao INT AUTO_INCREMENT PRIMARY KEY,
        fk_JOGADOR_ID_Jogador INT,
        fk_JOGO_ID_Jogo INT,
        Data_Avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Comentario TEXT,
        Nota SMALLINT,
        FOREIGN KEY (fk_JOGADOR_ID_Jogador) REFERENCES JOGADOR(ID_Jogador) ON DELETE CASCADE,
        FOREIGN KEY (fk_JOGO_ID_Jogo) REFERENCES JOGO(ID_Jogo) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Tarefa': (
        """CREATE TABLE Tarefa (
        ID_Tarefa INT AUTO_INCREMENT PRIMARY KEY,
        fk_DESENVOLVEDOR_ID_Desenvolvedor INT,
        fk_FASE_ID_Fase INT,
        Descricao_Tarefa TEXT,
        Status_Tarefa VARCHAR(30),
        Data_Tarefa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor) REFERENCES DESENVOLVEDOR(ID_Desenvolvedor) ON DELETE SET NULL,
        FOREIGN KEY (fk_FASE_ID_Fase) REFERENCES FASE(ID_Fase) ON DELETE CASCADE
        )ENGINE=InnoDB"""),

    'Marcador_Jogo': (
        """CREATE TABLE Marcador_Jogo (
        fk_MARCADOR_ID_Marcador INT,
        fk_JOGO_ID_Jogo INT,
        PRIMARY KEY (fk_MARCADOR_ID_Marcador, fk_JOGO_ID_Jogo),
        FOREIGN KEY (fk_MARCADOR_ID_Marcador) REFERENCES MARCADOR(ID_Marcador) ON DELETE CASCADE,
        FOREIGN KEY (fk_JOGO_ID_Jogo) REFERENCES JOGO(ID_Jogo) ON DELETE CASCADE
        )ENGINE=InnoDB"""),
}