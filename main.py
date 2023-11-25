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
# Inserir dados paciente:
def inserir_dados_paciente():
    id_convenio = input("Digite o id do convenio: ")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o cpf do paciente (com pontuação): ")
    idade = input("Digite a idade do paciente, em anos inteiros: ")
    genero = input("Digite o genero do paciente (M/F): ")
    
    sql = "INSERT INTO Paciente (id_convenio, nome, cpf, idade, genero) VALUES (%s, %s, %s, %s, %s)"
    values = (id_convenio, nome, cpf, idade, genero)

    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados convenio:
def inserir_dados_convenio():
    nome = input("Digite o nome do convenio: ")
    cnpj = input("Digite o cnpj do convenio (com pontuação): ")
    
    sql = "INSERT INTO Convenio (nome, cnpj) VALUES (%s, %s)"
    values = (nome, cnpj)

    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados medico:
def inserir_dados_clinica():
    nome = input("Digite o nome da clínica: ")
    cnpj = input("Digite o cnpj da clínica (com pontuação): ")
    uf = input("Digite a uf da clínica: ")
    cidade = input("Digite a cidade da clínica: ")
    bairro = input("Digite o bairro da clínica: ")
    
    sql = "INSERT INTO Clinica (nome, cnpj, uf, cidade, bairro) VALUES (%s, %s, %s, %s, %s)"
    values = (nome, cnpj, uf, cidade, bairro)
    
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados parceria:
def inserir_dados_parceria():
    id_clinica = input("Digite o id da clínica: ")
    id_convenio = input("Digite o id do convênio: ")
    
    sql = "INSERT INTO Parceria (id_clinica, id_convenio) VALUES (%s, %s)"
    values = (id_clinica, id_convenio)
    
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados medico:
def inserir_dados_medico():
    id_clinica = input("Digite o id da clínica: ")
    nome = input("Digite o nome do médico: ")
    crm = input("Digite o crm do médico (com pontuação): ")
    especialidade = input("Digite a especialidade do médico: ")
    
    sql = "INSERT INTO Medico (id_clinica, nome, crm, especialidade) VALUES (%s, %s, %s, %s)"
    values = (id_clinica, nome, crm, especialidade)
    
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados consulta:
def inserir_dados_consulta():
    id_medico = input("Digite o id do médico: ")
    id_paciente = input("Digite o id do paciente: ")
    # data = datenow()

    sql = "INSERT INTO Consulta (id_medico, id_paciente) VALUES (%s, %s)"
    value = (id_medico, id_paciente)
    
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados prescricao:
def inserir_dados_prescricao():
    id_consulta = input("Digite o id da consulta: ")
    id_medicamento = input("Digite o id do medicamento: ")
    dose = input("Digite a dose do medicamento: ")

    sql = "INSERT INTO Prescricao (id_consulta, id_medicamento, dose) VALUES (%s, %s, %s)"
    values = (id_consulta, id_medicamento, dose)
    
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados medicamento:
def inserir_dados_medicamento():
    nome = input("Digite o nome do medicamento: ")
    tipo = input("Digite o tipo do medicamento: ")
    
    sql = "INSERT INTO Medicamento (nome, tipo) VALUES (%s, %s)"
    values = (nome, tipo)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

#####################################################################################################
#####################################################################################################
#####################################################################################################

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
