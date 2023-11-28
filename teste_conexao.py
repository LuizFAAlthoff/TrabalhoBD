import mysql.connector

# Conectar ao servidor MySQL
conexao = mysql.connector.connect(
    host='localhost',  # host onde o MySQL está sendo executado
    user='root',  # nome de usuário do MySQL
    password='d4nibd1',  # senha do MySQL
    database='saude'  # nome do banco de dados
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Exemplo de consulta (seleção)
cursor.execute("SELECT * FROM saude.Consulta")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

# Exemplo de inserção
# cursor.execute("INSERT INTO nome_da_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
# conexao.commit()

# Exemplo de atualização
# cursor.execute("UPDATE nome_da_tabela SET coluna1 = %s WHERE coluna2 = %s", (novo_valor, condicao))
# conexao.commit()

# Exemplo de exclusão
# cursor.execute("DELETE FROM nome_da_tabela WHERE coluna = %s", (valor,))
# conexao.commit()

# Fechar cursor e conexão
cursor.close()
conexao.close()
