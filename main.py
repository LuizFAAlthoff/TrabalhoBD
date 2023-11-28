import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

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

#####################################################################################################
#####################################################################################################
#####################################################################################################

# Inserir dados paciente:
import mysql.connector

# Supondo que você já tenha uma conexão 'conn' e um cursor 'cursor' configurados

def inserir_dados_paciente():
    id_convenio = input("Digite o id do convenio: ")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o cpf do paciente (com pontuação) [Ex: 123.456.789-00]: ")
    idade = int(input("Digite a idade do paciente, em anos inteiros [Ex: 23]: "))  # Convertendo para inteiro
    genero = input("Digite o gênero do paciente [Ex: M]: ")

    sql = "INSERT INTO Paciente (id_convenio, nome, cpf, idade, genero) VALUES (%s, %s, %s, %s, %s)"
    values = (id_convenio, nome, cpf, idade, genero)

    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Chame a função inserir_dados_paciente() onde for necessário no seu código.
1

# Inserir dados convenio:
def inserir_dados_convenio():
    nome = input("Digite o nome do convenio: ")
    cnpj = input("Digite o cnpj do convenio (com pontuação) [Ex: 12.345.678/0001-99]: ")
    
    sql = "INSERT INTO Convenio (nome, cnpj) VALUES (%s, %s)"
    values = (nome, cnpj)

    cursor.execute(sql, values)
    conn.commit()
    print("Dados inseridos com sucesso!")

# Inserir dados clinica:
def inserir_dados_clinica():
    nome = input("Digite o nome da clínica: ")
    cnpj = input("Digite o cnpj da clínica (com pontuação) [Ex: 12.345.678/0001-99]: ")
    uf = input("Digite a UF da clínica: ")
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
    crm = input("Digite o crm do médico (cinco números): ")
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
    data = datetime.now().strftime('%Y-%m-%d')  # Converter para string no formato YYYY-MM-DD

    sql = "INSERT INTO Consulta (id_medico, id_paciente, data) VALUES (%s, %s, %s)"
    values = (id_medico, id_paciente, data)

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

# Atualizar dados paciente:
def atualizar_dados_paciente():
    id_paciente = input("Digite o id do paciente a ser alterado: ")
    id_convenio = input("Digite o id do convenio: ")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o cpf do paciente (com pontuação)  [Ex: 123.456.789-00]: ")
    idade = input("Digite a idade do paciente, em anos inteiros [Ex: 23]: ")
    genero = input("Digite o genero do paciente (M/F) [Ex: M]: ")
    
    sql = "UPDATE Paciente SET id_convenio = %s, nome = %s, cpf = %s, idade = %s, genero = %s WHERE id_paciente = %s"
    values = (id_convenio, nome, cpf, idade, genero, id_paciente)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados convenio:
def atualizar_dados_convenio():
    id_convenio = input("Digite o id do convenio a ser alterado: ")
    nome = input("Digite o nome do convenio: ")
    cnpj = input("Digite o cnpj do convenio (com pontuação) [Ex: 12.345.678/0001-99]: ")
    
    sql = "UPDATE Convenio SET nome = %s, cnpj = %s WHERE id_convenio = %s"
    values = (nome, cnpj, id_convenio)
    cursor.execute(sql, values)
    conn.commit()
    print("Dados atualizados com sucesso!")

# Atualizar dados clinica:
def atualizar_dados_clinica():
    id_clinica = input("Digite o id da clínica a ser alterada: ")
    nome = input("Digite o nome da clínica: ")
    cnpj = input("Digite o cnpj da clínica (com pontuação) [Ex: 12.345.678/0001-99]: ")
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
    crm = input("Digite o crm do médico (cinco números): ")
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
def listar_dados_parcerias():
    query = """
    SELECT P.id_parceria, C.nome AS nome_clinica, C.id_clinica, CO.nome AS nome_convenio, CO.id_convenio
    FROM Parceria AS P
    INNER JOIN Clinica AS C ON P.id_clinica = C.id_clinica
    INNER JOIN Convenio AS CO ON P.id_convenio = CO.id_convenio;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

# Listar dados medico:
def listar_dados_medico():
    sql = "SELECT * FROM Medico"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)

# Listar dados consulta:
def listar_dados_consultas():
    query = """
    SELECT C.id_consulta, M.nome AS nome_medico, M.id_medico, P.nome AS nome_paciente, P.id_paciente, C.data
    FROM Consulta AS C
    INNER JOIN Medico AS M ON C.id_medico = M.id_medico
    INNER JOIN Paciente AS P ON C.id_paciente = P.id_paciente;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

# Listar dados prescricao:
def listar_dados_prescricao():
    query = """
    SELECT PR.id_prescricao, P.nome AS nome_paciente, M.nome AS nome_medicamento, PR.dose
    FROM Prescricao AS PR
    INNER JOIN Consulta AS C ON PR.id_consulta = C.id_consulta
    INNER JOIN Paciente AS P ON C.id_paciente = P.id_paciente
    INNER JOIN Medicamento AS M ON PR.id_medicamento = M.id_medicamento;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
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

# Queries especiais

# Top 3 Convenios com mais pacientes
def consultar_top_convenios(cursor):
    query = """
    SELECT CO.nome AS nome_convenio, COUNT(P.id_paciente) AS num_pacientes
    FROM Convenio AS CO
    LEFT JOIN Paciente AS P ON CO.id_convenio = P.id_convenio
    GROUP BY CO.id_convenio
    ORDER BY num_pacientes DESC
    LIMIT 3;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)
    

# Remeios mais prescritos
def consultar_remedios_mais_prescritos(cursor):
    query = """
    SELECT M.nome AS nome_remedio, COUNT(PR.id_medicamento) AS vezes_prescrito
    FROM Medicamento AS M
    LEFT JOIN Prescricao AS PR ON M.id_medicamento = PR.id_medicamento
    GROUP BY M.id_medicamento
    ORDER BY vezes_prescrito DESC;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

# Médicos com mais atendimentos e a clínica onde trabalham com data da consulta
def consultar_medicos_mais_consultas(cursor):
    query = """
    SELECT COUNT(C.id_consulta) AS total_consultas, M.nome AS nome_medico, CL.nome AS nome_clinica
    FROM Medico AS M
    LEFT JOIN Consulta AS C ON M.id_medico = C.id_medico
    LEFT JOIN Clinica AS CL ON M.id_clinica = CL.id_clinica
    GROUP BY M.id_medico
    ORDER BY total_consultas DESC;
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

# Interface
while True:
    print("1 - Inserir dados")
    print("2 - Atualizar dados")
    print("3 - Listar dados")
    print("4 - Excluir dados")
    print("5 - [Query] Top 3 convênios que possuem um maior número de clientes (pacientes)")
    print("6 - [Query] Remédios mais prescritos, retornando o nome do remédio e a quantidade de vezes prescrito")
    print("7 - [Query] Médicos que realizaram mais consultas, ordenando do maior para o menor, retornando o total de consultas realizadas, o nome do médico, o nome da clínica e a data da consulta realizada")
    print("8 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("1 - Inserir dados paciente")
        print("2 - Inserir dados convenio")
        print("3 - Inserir dados clinica")
        print("4 - Inserir dados parceria")
        print("5 - Inserir dados medico")
        print("6 - Inserir dados consulta")
        print("7 - Inserir dados prescricao")
        print("8 - Inserir dados medicamento")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            inserir_dados_paciente()
        elif opcao == "2":
            inserir_dados_convenio()
        elif opcao == "3":
            inserir_dados_clinica()
        elif opcao == "4":
            inserir_dados_parceria()
        elif opcao == "5":
            inserir_dados_medico()
        elif opcao == "6":
            inserir_dados_consulta()
        elif opcao == "7":
            inserir_dados_prescricao()
        elif opcao == "8":
            inserir_dados_medicamento()
        else:
            print("Opção inválida!")
    elif opcao == "2":
        print("1 - Atualizar dados paciente")
        print("2 - Atualizar dados convenio")
        print("3 - Atualizar dados clinica")
        print("4 - Atualizar dados parceria")
        print("5 - Atualizar dados medico")
        print("6 - Atualizar dados consulta")
        print("7 - Atualizar dados prescricao")
        print("8 - Atualizar dados medicamento")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            atualizar_dados_paciente()
        elif opcao == "2":
            atualizar_dados_convenio()
        elif opcao == "3":
            atualizar_dados_clinica()
        elif opcao == "4":
            atualizar_dados_parceria()
        elif opcao == "5":
            atualizar_dados_medico()
        elif opcao == "6":
            atualizar_dados_consulta()
        elif opcao == "7":
            atualizar_dados_prescricao()
        elif opcao == "8":
            atualizar_dados_medicamento()
        else:
            print("Opção inválida!")
    elif opcao == "3":
        print("1 - Listar dados paciente")
        print("2 - Listar dados convenio")
        print("3 - Listar dados clinica")
        print("4 - Listar dados parceria")
        print("5 - Listar dados medico")
        print("6 - Listar dados consulta")
        print("7 - Listar dados prescricao")
        print("8 - Listar dados medicamento")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            listar_dados_paciente()
        elif opcao == "2":
            listar_dados_convenio()
        elif opcao == "3":
            listar_dados_clinica()
        elif opcao == "4":
            listar_dados_parcerias()
        elif opcao == "5":
            listar_dados_medico()
        elif opcao == "6":
            listar_dados_consultas()
        elif opcao == "7":
            listar_dados_prescricao()
        elif opcao == "8":
            listar_dados_medicamento()
        else:
            print("Opção inválida!")
    elif opcao == "4":
        print("1 - Excluir dados paciente")
        print("2 - Excluir dados convenio")
        print("3 - Excluir dados clinica")
        print("4 - Excluir dados parceria")
        print("5 - Excluir dados medico")
        print("6 - Excluir dados consulta")
        print("7 - Excluir dados prescricao")
        print("8 - Excluir dados medicamento")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            excluir_paciente()
        elif opcao == "2":
            excluir_convenio()
        elif opcao == "3":
            excluir_clinica()
        elif opcao == "4":
            excluir_parceria()
        elif opcao == "5":
            excluir_medico()
        elif opcao == "6":
            excluir_consulta()
        elif opcao == "7":
            excluir_prescricao()
        elif opcao == "8":
            excluir_medicamento()
        else:
            print("Opção inválida!")
    elif opcao == "5":
        consultar_top_convenios(cursor)
    elif opcao == "6":
        consultar_remedios_mais_prescritos(cursor)
    elif opcao == "7":
        consultar_medicos_mais_consultas(cursor)
    elif opcao == "8":
        break

# Fecha o cursor e a conexão
cursor.close()
conn.close()
