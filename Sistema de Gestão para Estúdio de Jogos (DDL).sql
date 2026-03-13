CREATE TABLE MOTOR_GRAFICO (
    ID_Motor INTEGER PRIMARY KEY,
    Nome_Motor VARCHAR(255),
    Versao INTEGER
);

CREATE TABLE JOGO (
    ID_Jogo INTEGER PRIMARY KEY,
    Nome_Jogo VARCHAR(255),
    Genero_Jogo VARCHAR(255),
    Data_Lancamento TIMESTAMP,
    FK_MOTOR_GRAFICO_ID_Motor INTEGER,
    FOREIGN KEY (FK_MOTOR_GRAFICO_ID_Motor)
        REFERENCES MOTOR_GRAFICO (ID_Motor)
);

CREATE TABLE PLATAFORMA (
    ID_Plataforma INTEGER PRIMARY KEY,
    Nome_Plataforma VARCHAR(255)
);

CREATE TABLE ITEM (
    ID_Item INTEGER PRIMARY KEY,
    Nome_Item VARCHAR(255),
    Raridade VARCHAR(255),
    Pontos_Oferecidos INTEGER
);

CREATE TABLE ESPECIALIDADE (
    ID_Especialidade INTEGER PRIMARY KEY,
    Nome_Especialidade VARCHAR(255)
);

CREATE TABLE DESENVOLVEDOR (
    ID_Desenvolvedor INTEGER PRIMARY KEY,
    Nome_Desenvolvedor VARCHAR(255),
    Data_Contratacao TIMESTAMP,
    ID_Supervisor INTEGER
);

CREATE TABLE FASE (
    ID_Fase INTEGER PRIMARY KEY,
    Nome_Fase VARCHAR(255),
    Dificuldade_Fase VARCHAR(255),
    FK_JOGO_ID_Jogo INTEGER,
    FOREIGN KEY (FK_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

CREATE TABLE JOGADOR (
    ID_Jogador INTEGER PRIMARY KEY,
    Nickname VARCHAR(255),
    Email VARCHAR(255),
    Data_Cadastro TIMESTAMP
);

CREATE TABLE LOJA (
    ID_Loja INTEGER PRIMARY KEY,
    Nome_Loja VARCHAR(255)
);

CREATE TABLE MARCADOR (
    ID_Marcador INTEGER PRIMARY KEY,
    Nome_Marcador VARCHAR(255)
);

CREATE TABLE Supervisao (
    fk_DESENVOLVEDOR_ID_Desenvolvedor INTEGER,
    fk_DESENVOLVEDOR_ID_Desenvolvedor_ INTEGER,
    PRIMARY KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor_, fk_DESENVOLVEDOR_ID_Desenvolvedor),
    FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor),
    FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor_)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor)
);

CREATE TABLE Lancamento (
    fk_PLATAFORMA_ID_Plataforma INTEGER,
    fk_JOGO_ID_Jogo INTEGER,
    PRIMARY KEY (fk_JOGO_ID_Jogo, fk_PLATAFORMA_ID_Plataforma),
    FOREIGN KEY (fk_PLATAFORMA_ID_Plataforma)
        REFERENCES PLATAFORMA (ID_Plataforma),
    FOREIGN KEY (fk_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

CREATE TABLE Especialidade_Desenvolvedor (
    fk_ESPECIALIDADE_ID_Especialidade INTEGER,
    fk_DESENVOLVEDOR_ID_Desenvolvedor INTEGER,
    PRIMARY KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor, fk_ESPECIALIDADE_ID_Especialidade),
    FOREIGN KEY (fk_ESPECIALIDADE_ID_Especialidade)
        REFERENCES ESPECIALIDADE (ID_Especialidade),
    FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor)
);

CREATE TABLE Fase_Item (
    fk_FASE_ID_Fase INTEGER,
    fk_ITEM_ID_Item INTEGER,
	PRIMARY KEY (fk_FASE_ID_Fase, fk_ITEM_ID_Item),
    FOREIGN KEY (fk_FASE_ID_Fase)
        REFERENCES FASE (ID_Fase),
    FOREIGN KEY (fk_ITEM_ID_Item)
        REFERENCES ITEM (ID_Item)
);

CREATE TABLE Jogo_Desenvolvedor (
    fk_DESENVOLVEDOR_ID_Desenvolvedor INTEGER,
    fk_JOGO_ID_Jogo INTEGER,
    Funcao_no_Projeto VARCHAR(255),
    PRIMARY KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor, fk_JOGO_ID_Jogo),
    FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor),
    FOREIGN KEY (fk_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

CREATE TABLE Venda (
    ID_Venda INTEGER,
    Data_Venda TIMESTAMP,
    Valor_Venda INTEGER,
    fk_LOJA_ID_Loja INTEGER,
    fk_JOGADOR_ID_Jogador INTEGER,
    fk_JOGO_ID_Jogo INTEGER,
    PRIMARY KEY (Data_Venda, ID_Venda),
    FOREIGN KEY (fk_LOJA_ID_Loja)
        REFERENCES LOJA (ID_Loja),
    FOREIGN KEY (fk_JOGADOR_ID_Jogador)
        REFERENCES JOGADOR (ID_Jogador),
    FOREIGN KEY (fk_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

CREATE TABLE Avaliacao (
    ID_Avaliacao INTEGER PRIMARY KEY,
    fk_JOGADOR_ID_Jogador INTEGER,
    fk_JOGO_ID_Jogo INTEGER,
    Data_Avaliacao TIMESTAMP,
    Comentario TEXT,
    Nota INTEGER,
    FOREIGN KEY (fk_JOGADOR_ID_Jogador)
        REFERENCES JOGADOR (ID_Jogador),
    FOREIGN KEY (fk_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

CREATE TABLE Tarefa (
    Data_Tarefa TIMESTAMP PRIMARY KEY,
    fk_DESENVOLVEDOR_ID_Desenvolvedor INTEGER,
    fk_FASE_ID_Fase INTEGER,
    Descricao_Tarefa TEXT,
    Status_Tarefa VARCHAR(255),
    FOREIGN KEY (fk_DESENVOLVEDOR_ID_Desenvolvedor)
        REFERENCES DESENVOLVEDOR (ID_Desenvolvedor),
    FOREIGN KEY (fk_FASE_ID_Fase)
        REFERENCES FASE (ID_Fase)
);

CREATE TABLE Marcador_Jogo (
    fk_MARCADOR_ID_Marcador INTEGER,
    fk_JOGO_ID_Jogo INTEGER,
    PRIMARY KEY (fk_MARCADOR_ID_Marcador, fk_JOGO_ID_Jogo),
    FOREIGN KEY (fk_MARCADOR_ID_Marcador)
        REFERENCES MARCADOR (ID_Marcador),
    FOREIGN KEY (fk_JOGO_ID_Jogo)
        REFERENCES JOGO (ID_Jogo)
);

drop table Marcador_Jogo; 
drop table Tarefa; 
drop table Avaliacao; 
drop table Venda; 
drop table Jogo_Desenvolvedor; 
drop table Fase_Item; 
drop table Especialidade_Desenvolvedor; 
drop table Lancamento; 
drop table Supervisao;
drop table MARCADOR; 
drop table LOJA; 
drop table JOGADOR; 
drop table FASE; 
drop table DESENVOLVEDOR; 
drop table ESPECIALIDADE; 
drop table ITEM; 
drop table PLATAFORMA; 
drop table JOGO; 
drop table MOTOR_GRAFICO; 