# Para a utilização do prgrama é necessario a insatalação de:
# pip install mysql-connector-python
# pip install pandas
# pip install matplotlib
# pip install google-generativeai
import matplotlib.pyplot
import mysql.connector
from mysql.connector import errorcode
import google.generativeai as genai
from datetime import date, datetime
import Tables
import Drop
import pandas

pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 1000)

# Funcoes axuiliares
# Conexao inicial ao banco
def connectDB():
    con = mysql.connector.connect(host='localhost', database='estudio_jogos_db', user='root', password='senha')
    if con.is_connected():
        db_info = con.server_info
        print("Conectado ao servidor MYSQL", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados", linha)
        cursor.close()
    return con


try:
    GEMINI_API_KEY = "AIzaSyBLFLksyHUoc3Pvom9ySTW7wSHcXKNsBBM"
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-2.5-flash')
    print("API do Gemini configurada com sucesso!")
except Exception as e:
    print(f"\nErro ao configurar a API do Gemini: {e}")
    gemini_model = None


# Sair do DB
def exit_db(connect):
    print("-- EXIT DB --")
    connect.close()
    print("Conexao encerrada!!")


def mostrar_colunas(connect, tabela):
    cursor = connect.cursor()  # Abre a conexão com o banco
    cursor.execute(f"SHOW COLUMNS FROM {tabela}")  # Obtem as informações das colunas da tabela
    resultado = cursor.fetchall()  # Pega todas as linhas e as transforma em tuplas
    print("Colunas da tabela", tabela)
    for coluna in resultado:
        print(coluna[0], "-", end=" ")
    print()
    cursor.close()


def mostrar_tabela(connect, tabela):
    querry = f"""select * from {tabela}"""
    df = pandas.read_sql(querry, con=connect)
    print(df)
    print()


def obter_colunas(connect, tabela):
    cursor = connect.cursor()  # Abre a conexão
    cursor.execute(f"SHOW COLUMNS FROM {tabela}")  # Obtem as informações das colunas da tabela
    resultado = cursor.fetchall()  # Pega todas as linhas e as transforma em tuplas
    colunas = [col[0] for col in resultado]
    cursor.close()
    return colunas


def insert_indv(connect):  # FUNCAO A IMPLEMENTAR # Opcao 1
    print("\n-- INSERT INDIVIDUAL --")
    cursor = connect.cursor()

    try:
        for table_name in Tables.table:
            print(f"- {table_name}")

        tabela_nome = input("Digite o nome da tabela para inserir: ")

        if tabela_nome not in Tables.table:
            print(f"Erro: Tabela '{tabela_nome}' desconhecida.")
            cursor.close()
            return

        mostrar_tabela(connect, tabela_nome)

        colunas = obter_colunas(connect, tabela_nome)

        colunas_inserir = [col for col in colunas if not col.startswith('ID_')]

        print(f"Você precisará fornecer valores para as seguintes colunas:")
        print(f"({', '.join(colunas_inserir)})")

        valores = []
        for col in colunas_inserir:
            val = input(f"Digite o valor para {col} (ou 'NULL' para nulo): ")
            if val.upper() == 'NULL':
                valores.append(None)
            else:
                valores.append(val)

        placeholders = ', '.join(['%s'] * len(valores))
        sql = f"INSERT INTO {tabela_nome} ({', '.join(colunas_inserir)}) VALUES ({placeholders})"

        cursor.execute(sql, valores)
        connect.commit()
        print(f"Nova linha inserida na tabela '{tabela_nome}' com ID: {cursor.lastrowid}")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir: {err}")
        print("DICA: Verifique se os valores (especialmente Chaves Estrangeiras) são válidos.")
        connect.rollback()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if cursor:
            cursor.close()


def atualizar(connect):  # Opcao 2
    print("-- UPDATE TABLE --")
    cursor = connect.cursor()

    for table_name in Tables.table:
        print("Nome: {} ".format(table_name))

    table_updade = input(str("Digite a tabela a ser alterada: "))

    for table_name in Tables.table:
        if table_name == table_updade:
            colunas = obter_colunas(connect, table_name)
            break

    coluna_id = colunas[0]

    mostrar_tabela(connect, table_name)

    valor_id = input(f"\nDigite o valor de {coluna_id} da linha que deseja alterar: ")

    coluna_alterar = input("\nQual coluna deseja alterar? ")

    if coluna_alterar not in colunas:
        print("Coluna inválida. \n")
        cursor.close()
        return

    novo_valor = input(f"Digite o novo valor para {coluna_alterar}: ")

    tupla_alt = f"UPDATE {table_name} SET {coluna_alterar} = %s WHERE {coluna_id} = %s"

    try:
        cursor.execute(tupla_alt, (novo_valor, valor_id))
        connect.commit()
        print("Linha atualizada com sucesso!")

    except  mysql.connector.Error as err:
        print(err.msg)

    cursor.close()


def delete(connect):  # FUNCAO A IMPLEMENTAR #Opcao 3
    print("\n-- DELETE LINHA --")
    cursor = connect.cursor()

    try:
        for table_name in Tables.table:
            print(f"- {table_name}")
        tabela_nome = input("Digite o nome da tabela para deletar: ")

        if tabela_nome not in Tables.table:
            print(f"Erro: Tabela '{tabela_nome}' desconhecida.")
            cursor.close()
            return

        colunas = obter_colunas(connect, tabela_nome)
        pk_coluna_nome = colunas[0]

        mostrar_tabela(connect, tabela_nome)

        print(f"A chave primária desta tabela é: {pk_coluna_nome}")
        pk_valor = input(f"Digite o ID (valor de {pk_coluna_nome}) da linha a ser deletada: ")

        sql = f"DELETE FROM {tabela_nome} WHERE {pk_coluna_nome} = %s"

        cursor.execute(f"SELECT 1 FROM {tabela_nome} WHERE {pk_coluna_nome} = %s", (pk_valor,))
        if not cursor.fetchone():
            print(f"Erro: Linha com {pk_coluna_nome} = {pk_valor} não encontrada.")
            cursor.close()
            return

        confirm = input(f"Tem certeza que deseja deletar a linha {pk_valor} da tabela '{tabela_nome}'? (s/n): ")
        if confirm.lower() != 's':
            print("Deleção cancelada.")
            cursor.close()
            return

        cursor.execute(sql, (pk_valor,))
        connect.commit()

        print(f"Linha {pk_valor} deletada com sucesso da tabela '{tabela_nome}'.")

    except mysql.connector.Error as err:
        print(f"Erro ao deletar: {err}")
        connect.rollback()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if cursor:
            cursor.close()


def consulta_1(connect):  # Opcao 4. Quatro tabelas, plataforma, venda, jogo e Lancamento
    try:
        cursor = connect.cursor()

        querry = """
        select plataforma.Nome_plataforma, count(venda.ID_Venda) as quantidade_venda, sum(venda.Valor_Venda) as total_arrecadado 
        from venda join jogo on venda.fk_JOGO_ID_Jogo = jogo.ID_Jogo join Lancamento on Lancamento.fk_JOGO_ID_Jogo = jogo.ID_Jogo join plataforma on plataforma.ID_Plataforma = Lancamento.fk_PLATAFORMA_ID_Plataforma
        group by plataforma.ID_Plataforma, plataforma.Nome_Plataforma
        order by total_arrecadado desc
        """
        print()  # para dar espaco
        cursor.execute(querry)
        my_result = cursor.fetchall()

        df = pandas.read_sql(querry, con=connect)
        df.plot(kind="bar", x="Nome_plataforma", y="total_arrecadado")
        print(df)
        matplotlib.pyplot.show()

        print()
    except mysql.connector.Error as error:
        print("Ocorreu um erro durante o processamento {}.".format(error))
    finally:
        if connect.is_connected():
            cursor.close()


def consulta_2(connect):  # Opcao 4. Seis tabelas, Jogador, Jogo, Item, Venda, Fase e Fase_Item
    try:
        cursor = connect.cursor()

        querry = """
        select jogador.Nickname, jogo.Nome_Jogo, count(ITEM.ID_Item) as total_Item
        from jogador join venda on jogador.ID_Jogador = venda.fk_JOGADOR_ID_Jogador join jogo on jogo.ID_Jogo = venda.fk_JOGO_ID_Jogo join fase on jogo.ID_Jogo = fase.fk_JOGO_ID_Jogo 
        join Fase_Item on Fase_Item.fk_FASE_ID_Fase = Fase.ID_Fase join Item on Item.ID_Item = Fase_Item.fk_ITEM_ID_Item
        group by jogador.ID_Jogador, jogador.Nickname, jogo.Nome_Jogo
        order by jogador.Nickname, total_Item desc
        """
        print()  # para dar espaco
        cursor.execute(querry)
        my_result = cursor.fetchall()

        df = pandas.read_sql(querry, con=connect)
        df.plot(kind="bar", x="Nickname", y=["total_Item"])
        print(df)
        matplotlib.pyplot.show()

        print()

    except mysql.connector.Error as error:
        print("Ocorreu um erro durante o processamento {}.".format(error))
    finally:
        if connect.is_connected():
            cursor.close()


def consulta_3(connect):  # Opcao 4. Tres tabelas, marcador, marcador_jogo e venda
    try:
        cursor = connect.cursor()

        querry = """
        select 	marcador.ID_Marcador, marcador.Nome_Marcador, count(*) as vezes_escolhido
        from venda join marcador_jogo on marcador_jogo.fk_JOGO_ID_Jogo = venda.fk_JOGO_ID_Jogo
        join marcador on marcador.ID_Marcador = marcador_jogo.fk_MARCADOR_ID_Marcador
        group by marcador.ID_Marcador, marcador.Nome_Marcador
        order by vezes_escolhido desc

        """
        print()  # para dar espaco
        cursor.execute(querry)
        my_result = cursor.fetchall()

        df = pandas.read_sql(querry, con=connect)
        df.plot(kind="bar", x="Nome_Marcador", y="vezes_escolhido")
        print(df)
        matplotlib.pyplot.show()

        print()
    except mysql.connector.Error as error:
        print("Ocorreu um erro durante o processamento {}.".format(error))
    finally:
        if connect.is_connected():
            cursor.close()

        # Cria todas as tabelas do db -- Opcao 5


def create_all(connect):
    print("\n-- CREATE TABLES --")
    cursor = connect.cursor()
    for table_name in Tables.table:
        table_description = Tables.table[table_name]
        try:
            print("Tabela Criada {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Tabela ja existe!")
            else:
                print(err.msg)
        else:
            print("OK")
    cursor.close()


# retira todas as tabelas do db -- Opcao 6
def drop_all(connect):
    print("\n-- DROP TABLES --")
    cursor = connect.cursor()
    for drop_name in Drop.drop:
        drop_description = Drop.drop[drop_name]
        try:
            print("Drop {}: ".format(drop_name), end='')
            cursor.execute(drop_description)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    cursor.close()


# falta o insert na tabela Supervisao
# Insere em todas as tabelas valores predeterminados -- Opcao 7
def insert_all(connect):
    print("\n-- INSERT ALL --")
    cursor = connect.cursor()
    file = open("insercao.txt")
    conteudo = file.read()

    linhas = [string.strip() for string in conteudo.split(';') if string.strip()]

    for inserir in linhas:

        try:
            print("Realizando: {}".format(inserir), end='')
            cursor.execute(inserir)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print(" OK")

    connect.commit()
    cursor.close()
    file.close()


# Mostra todas as tabelas -- Opcao 8
def show_all(connect):
    print("\n-- SHOW TABLES --")
    cursor = connect.cursor()
    for table_name in Tables.table:
        print("Nome: {} ".format(table_name))
    try:
        nome = input(str("\nDigite o nome da tabela a ser consultada: "))
        select = "select * from " + nome
        cursor.execute(select)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("Tabela {}".format(nome))
        my_result = cursor.fetchall()

        mostrar_tabela(connect, nome)

    cursor.close()


def IA(connect):  # opcao 9
    print("\n-- Assistente de IA: Análise de Avaliacoes de Jogo --")

    if not gemini_model:
        print("Erro: A API do Gemini não está configurada.")
        return

    cursor = connect.cursor()
    try:

        mostrar_tabela(connect, "JOGO")
        jogo_id = input("Digite o ID do JOGO para analisar as avaliações: ")

        cursor.execute("SELECT Nome_Jogo FROM JOGO WHERE ID_Jogo = %s", (jogo_id,))
        jogo_nome = cursor.fetchone()
        if not jogo_nome:
            print(f"Erro: Jogo com ID {jogo_id} não encontrado.")
            cursor.close()
            return

        cursor.execute("""
            SELECT Nota, Comentario FROM Avaliacao 
            WHERE fk_JOGO_ID_Jogo = %s AND Comentario IS NOT NULL AND Comentario != ''
        """, (jogo_id,))

        avaliacoes = cursor.fetchall()

        if not avaliacoes:
            print(f"Nenhuma avaliação com comentário encontrada para o jogo '{jogo_nome[0]}'.")
            cursor.close()
            return

        print(f"\nColetando {len(avaliacoes)} avaliações para '{jogo_nome[0]}'. Preparando para enviar à IA...")

        texto_avaliacoes = ""
        for nota, comentario in avaliacoes:
            comentario_limpo = str(comentario).replace('\n', ' ').replace('\r', ' ')
            texto_avaliacoes += f"- Nota: {nota}/5, Comentário: {comentario_limpo}\n"

        prompt = f"""
        Você é um analista de comunidade de um estúdio de jogos.
        Analise a seguinte lista de avaliações de jogadores para o jogo "{jogo_nome[0]}" e gere um resumo executivo conciso.

        Lista de Avaliações:
        {texto_avaliacoes}

        Seu resumo deve ser formatado exatamente assim:
        **Resumo Geral:** [Um parágrafo curto sobre o sentimento geral dos jogadores]
        **Pontos Positivos Comuns:**
        * [Principal elogio]
        * [Outro elogio comum]
        **Críticas e Pontos a Melhorar:**
        * [Principal crítica ou bug reportado]
        * [Outra crítica comum]
        """

        print("Enviando para o Gemini... (Isso pode levar alguns segundos)")
        response = gemini_model.generate_content(prompt)

        print(f"\n--- Análise de Avaliacoes da IA para: {jogo_nome[0]} ---")
        print(response.text)
        print("-----------------------------------------------------")

    except mysql.connector.Error as err:
        print(f"Erro de banco de dados: {err}")
    except Exception as e:
        print(f"Erro ao chamar a API do Gemini ou processar dados: {e}")
    finally:
        if cursor:
            cursor.close()


def menu():
    print("1 - Inserir")
    print("2 - Atualizar")
    print("3 - Deletar")
    print("4 - Consultar")
    print("5 - Criacao das tabelas")
    print("6 - Drop das tabelas")
    print("7 - Preencher as tabelas")
    print("8 - Consultar todas as tabelas")
    print("9 - Resumir avaliacoes usando IA")
    print("0 - Sair")


# MAIN
con = connectDB()

value = -1  # inicialização do valor

while value != 0:

    menu()

    try:
        value = int(input("Digite sua opção: "))

        if value == 1:
            # funcao para inserir2
            insert_indv(con)

        if value == 2:
            # funcao para atualizar
            atualizar(con)

        if value == 3:
            # funcao para deletar
            delete(con)

        if value == 4:
            # funcao para consultar
            print("1 - Verifica o total de vendas por plataforma")
            print("2 - Verifica o total de itens disponiveis para serem coletados por jogador")
            print("3 - Verifica qual eh o marcador mais polular entre os jogadores")
            escolha = int(input("Digite a sua escolha de consulta: "))
            if escolha == 1:
                consulta_1(con)
            if escolha == 2:
                consulta_2(con)
            if escolha == 3:
                consulta_3(con)

        if value == 5:
            # funcao para criar as tabelas
            create_all(con)

        if value == 6:
            # funcao para dropar as tabelas
            drop_all(con)

        if value == 7:
            # funcao para preencher as tabelas com dados
            insert_all(con)

        if value == 8:
            # Funcao para mostrar todas as tabelas
            show_all(con)

        if value == 9:
            # funcao para a IA
            IA(con)

        if value == 0:
            if con.is_connected():
                exit_db(con)
                print("Adeus!")
                break
            else:
                break

    except Exception as e:
        print(e)