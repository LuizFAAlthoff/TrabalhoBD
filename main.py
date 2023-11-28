import mysql.connector
from mysql.connector import errorcode

# Estabelece a conexão com o servidor MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="d4nibd1",
        database="saude",
        port='3306'
        )
    print("Conectado ao servidor MySQL")
        
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro de acesso negado")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
    else:
        print(f"Erro ao conectar ao banco de dados: {e}")

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

#####################################################################################################
#####################################################################################################
#####################################################################################################

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
    
    cursor.execute(sql, value)
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

# Atualizar dados paciente:
def atualizar_dados_paciente():
    id_paciente = input("Digite o id do paciente a ser alterado: ")
    id_convenio = input("Digite o id do convenio: ")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o cpf do paciente (com pontuação): ")
    idade = input("Digite a idade do paciente, em anos inteiros: ")
    genero = input("Digite o genero do paciente (M/F): ")
    
    sql = "UPDATE Paciente SET id_convenio = %s, nome = %s, cpf = %s, idade = %s, genero = %s WHERE id_paciente = %s"
    values = (id_convenio, nome, cpf, idade, genero, id_paciente)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados convenio:
def atualizar_dados_convenio():
    id_convenio = input("Digite o id do convenio a ser alterado: ")
    nome = input("Digite o nome do convenio: ")
    cnpj = input("Digite o cnpj do convenio (com pontuação): ")
    
    sql = "UPDATE Convenio SET nome = %s, cnpj = %s WHERE id_convenio = %s"
    values = (nome, cnpj, id_convenio)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados clinica:
def atualizar_dados_clinica():
    id_clinica = input("Digite o id da clínica a ser alterada: ")
    nome = input("Digite o nome da clínica: ")
    cnpj = input("Digite o cnpj da clínica (com pontuação): ")
    uf = input("Digite a uf da clínica: ")
    cidade = input("Digite a cidade da clínica: ")
    bairro = input("Digite o bairro da clínica: ")
    
    sql = "UPDATE Clinica SET nome = %s, cnpj = %s, uf = %s, cidade = %s, bairro = %s WHERE id_clinica = %s"
    values = (nome, cnpj, uf, cidade, bairro, id_clinica)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados parceria:
def atualizar_dados_parceria():
    id_parceria = input("Digite o id da parceria a ser alterada: ")
    id_clinica = input("Digite o id da clínica: ")
    id_convenio = input("Digite o id do convênio: ")
    
    sql = "UPDATE Parceria SET id_clinica = %s, id_convenio = %s WHERE id_parceria = %s"
    values = (id_clinica, id_convenio, id_parceria)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados medico:
def atualizar_dados_medico():
    id_medico = input("Digite o id do médico a ser alterado: ")
    id_clinica = input("Digite o id da clínica: ")
    nome = input("Digite o nome do médico: ")
    crm = input("Digite o crm do médico (com pontuação): ")
    especialidade = input("Digite a especialidade do médico: ")
    
    sql = "UPDATE Medico SET id_clinica = %s, nome = %s, crm = %s, especialidade = %s WHERE id_medico = %s"
    values = (id_clinica, nome, crm, especialidade, id_medico)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados consulta:
def atualizar_dados_consulta():
    id_consulta = input("Digite o id da consulta a ser alterada: ")
    id_medico = input("Digite o id do médico: ")
    id_paciente = input("Digite o id do paciente: ")
    # data = datenow()

    sql = "UPDATE Consulta SET id_medico = %s, id_paciente = %s WHERE id_consulta = %s"
    values = (id_medico, id_paciente, id_consulta)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados prescricao:
def atualizar_dados_prescricao():
    id_prescricao = input("Digite o id da prescrição a ser alterada: ")
    id_consulta = input("Digite o id da consulta: ")
    id_medicamento = input("Digite o id do medicamento: ")
    dose = input("Digite a dose do medicamento: ")

    sql = "UPDATE Prescricao SET id_consulta = %s, id_medicamento = %s, dose = %s WHERE id_prescricao = %s"
    values = (id_consulta, id_medicamento, dose, id_prescricao)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados medicamento:
def atualizar_dados_medicamento():
    id_medicamento = input("Digite o id do medicamento a ser alterado: ")
    nome = input("Digite o nome do medicamento: ")
    tipo = input("Digite o tipo do medicamento: ")
    
    sql = "UPDATE Medicamento SET nome = %s, tipo = %s WHERE id_medicamento = %s"
    values = (nome, tipo, id_medicamento)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

#####################################################################################################
#####################################################################################################
#####################################################################################################

# Listar dados paciente:
def listar_dados_paciente():
    sql = "SELECT * FROM Paciente"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados convenio:
def listar_dados_convenio():
    sql = "SELECT * FROM Convenio"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados clinica:
def listar_dados_clinica():
    sql = "SELECT * FROM Clinica"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados parceria:
def listar_dados_parceria():
    sql = "SELECT * FROM Parceria"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados medico:
def listar_dados_medico():
    sql = "SELECT * FROM Medico"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados consulta:
def listar_dados_consulta():
    sql = "SELECT * FROM Consulta"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados prescricao:
def listar_dados_prescricao():
    sql = "SELECT * FROM Prescricao"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados medicamento:
def listar_dados_medicamento():
    sql = "SELECT * FROM Medicamento"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

#####################################################################################################
#####################################################################################################
#####################################################################################################

# Excluir dados paciente:
def excluir_paciente():
    id_paciente = input("Digite o id do paciente a ser excluído: ")
    sql = "DELETE FROM Paciente WHERE id_paciente = %s"
    value = (id_paciente)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados convenio:
def excluir_convenio():
    id_convenio = input("Digite o id do convenio a ser excluído: ")
    sql = "DELETE FROM Convenio WHERE id_convenio = %s"
    value = (id_convenio)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados clinica:
def excluir_clinica():
    id_clinica = input("Digite o id da clínica a ser excluída: ")
    sql = "DELETE FROM Clinica WHERE id_clinica = %s"
    value = (id_clinica)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados parceria:
def excluir_parceria():
    id_parceria = input("Digite o id da parceria a ser excluída: ")
    sql = "DELETE FROM Parceria WHERE id_parceria = %s"
    value = (id_parceria)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados medico:
def excluir_medico():
    id_medico = input("Digite o id do médico a ser excluído: ")
    sql = "DELETE FROM Medico WHERE id_medico = %s"
    value = (id_medico)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados consulta:
def excluir_consulta():
    id_consulta = input("Digite o id da consulta a ser excluída: ")
    sql = "DELETE FROM Consulta WHERE id_consulta = %s"
    value = (id_consulta)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados prescricao:
def excluir_prescricao():
    id_prescricao = input("Digite o id da prescrição a ser excluída: ")
    sql = "DELETE FROM Prescricao WHERE id_prescricao = %s"
    value = (id_prescricao)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

# Excluir dados medicamento:
def excluir_medicamento():
    id_medicamento = input("Digite o id do medicamento a ser excluído: ")
    sql = "DELETE FROM Medicamento WHERE id_medicamento = %s"
    value = (id_medicamento)
    cursor.execute(sql, value)
    conn.commit()
    print("Dados excluídos com sucesso!")

#####################################################################################################
#####################################################################################################
#####################################################################################################

# Fecha o cursor e a conexão
cursor.close()
conn.close()
