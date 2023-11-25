import mysql.connector
from mysql.connector import errorcode

# Estabelece a conexão com o servidor MySQL
def connect():
        try:
            conn = mysql.connector.connect(
                host="seu_host",
                user="seu_usuario",
                password="sua_senha",
                database="seu_banco_de_dados"
                port='3306'
            )
            print("Conectado ao servidor MySQL")
            return conn
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de acesso negado")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe")
            else:
                print(f"Erro ao conectar ao banco de dados: {e}")
            return None

# Cria um cursor para executar operações no banco de dados
cursor = conn.cursor()

# Exemplo de inserção de dados
def inserir_dados():
    sql = "INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3) VALUES (%s, %s, %s)"
    values = ("valor1", "valor2", "valor3")
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Exemplo de atualização de dados
def atualizar_dados():
    sql = "UPDATE nome_da_tabela SET coluna1 = %s WHERE coluna2 = %s"
    values = ("novo_valor", "valor_a_atualizar")
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Exemplo de exclusão de dados
def deletar_dados():
    sql = "DELETE FROM nome_da_tabela WHERE coluna1 = %s"
    values = ("valor_a_deletar",)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados deletados com sucesso!")

# Exemplo de pesquisa
def buscar_dados():
    sql = "SELECT * FROM nome_da_tabela WHERE coluna1 = %s"
    values = ("valor_a_buscar",)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Chamadas às funções de exemplo
inserir_dados()
atualizar_dados()
deletar_dados()
buscar_dados()

# Fecha o cursor e a conexão
cursor.close()
conn.close()
