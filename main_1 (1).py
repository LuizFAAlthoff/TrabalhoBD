import mysql.connector
from mysql.connector import errorcode


class Programa:
    def __init__(self):
        self.cpf = None

    # Função para conectar ao banco de dados
    def connect(self):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='root',
                host='localhost',
                database='Roomie',
                port='3306'
            )
            print("Conectado ao servidor MySQL")
            return connection
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de acesso negado")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe")
            else:
                print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    # Função para desconectar do banco de dados
    def disconnect(self, connection):
        if connection.is_connected():
            connection.close()
            print("Conexão ao MySQL foi encerrada")

    # Função para executar uma consulta SQL
    def execute_query(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Consulta executada com sucesso")
        except mysql.connector.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            connection.rollback()

    # Inserção na tabela "avaliacao"
    def insert_avaliacao(self, connection, nota, descricao, id_colega=None, id_imovel=None):
        if id_colega is not None:
            query = f"INSERT INTO avaliacao (nota, descricao, id_colega) VALUES ('{nota}', '{descricao}', '{id_colega}')"
        else:
            query = f"INSERT INTO avaliacao (nota, descricao, id_imovel) VALUES ('{nota}', '{descricao}', '{id_imovel}')"
        self.execute_query(connection, query)

    # Atualização na tabela "avaliacao"
    def update_avaliacao(self, connection, id_avaliacao, nota, descricao, id_colega=None, id_imovel=None):
        if id_colega is not None:
            query = f"UPDATE avaliacao SET nota = '{nota}', descricao = '{descricao}', id_colega = '{id_colega}' WHERE id_avaliacao = {id_avaliacao}"
        else:
            query = f"UPDATE avaliacao SET nota = '{nota}', descricao = '{descricao}', id_imovel = '{id_imovel}' WHERE id_avaliacao = {id_avaliacao}"
        self.execute_query(connection, query)

    # Exclusão na tabela "avaliacao"
    def delete_avaliacao(self, connection, id_avaliacao):
        query = f"DELETE FROM avaliacao WHERE id_avaliacao = {id_avaliacao}"
        self.execute_query(connection, query)



    # Inserção na tabela "endereco"
    def insert_endereco(self, connection, uf, cidade, bairro):
        query = f"INSERT INTO endereco (uf, cidade, bairro) VALUES ('{uf}', '{cidade}', '{bairro}')"
        self.execute_query(connection, query)

    # Atualização na tabela "endereco"
    def update_endereco(self, connection, id_endereco, uf, cidade, bairro):
        query = f"UPDATE endereco SET uf = '{uf}', cidade = '{cidade}', bairro = '{bairro}' WHERE id_endereco = {id_endereco}"
        self.execute_query(connection, query)

    # Exclusão na tabela "endereco"
    def delete_endereco(self, connection, id_endereco):
        query = f"DELETE FROM endereco WHERE id_endereco = {id_endereco}"
        self.execute_query(connection, query)

    # Inserção na tabela "colega"
    def insert_colega(self, connection, tipo):
        try:
            cursor = connection.cursor()
            query = f"INSERT INTO colega (tipo) VALUES ('{tipo}')"
            cursor.execute(query)
            cursor.execute(f"UPDATE usuario SET id_imovel = {cursor.lastrowid} WHERE cpf = {self.cpf}")
            connection.commit()
            print("Novo colega inserido na tabela 'colega' com sucesso")
        except mysql.connector.Error as e:
            print(f"Erro ao inserir na tabela 'colega': {e}")
            connection.rollback()

    # Atualização na tabela "colega"
    def update_colega(self, connection, id_colega, tipo):
        cursor = connection.cursor()
        query = f"UPDATE colega SET tipo = '{tipo}' WHERE id_colega = {id_colega}"
        self.execute_query(connection, query)

    # Exclusão na tabela "colega"
    def delete_colega(self, connection, id_colega):
        query = f"DELETE FROM colega WHERE id_colega = {id_colega}"
        self.execute_query(connection, query)

    # Inserção na tabela "imovel"
    def insert_imovel(self, connection, banheiros, preco, id_endereco):
        query = f"INSERT INTO imovel (banheiros, preco, id_endereco) VALUES ({banheiros}, {preco}, {id_endereco})"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.execute(f"UPDATE usuario SET id_imovel = {cursor.lastrowid} WHERE cpf = {self.cpf}")
            connection.commit()
            print("Consulta executada com sucesso")
        except mysql.connector.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            connection.rollback()

    # Atualização na tabela "imovel"
    def update_imovel(self, connection, id_imovel, banheiros, preco, id_endereco):
        query = f"UPDATE imovel SET banheiros = {banheiros}, preco = {preco}, id_endereco = {id_endereco} WHERE id_imovel = {id_imovel}"
        self.execute_query(connection, query)

    # Exclusão na tabela "imovel"
    def delete_imovel(self, connection, id_imovel):
        query = f"DELETE FROM imovel WHERE id_imovel = {id_imovel}"
        self.execute_query(connection, query)

    # Inserção na tabela "quarto"
    def insert_quarto(self, connection, tipo, tamanho, id_imovel):
        query = f"INSERT INTO quarto (tipo, tamanho, id_imovel) VALUES ('{tipo}', '{tamanho}', {id_imovel})"
        self.execute_query(connection, query)

    # Atualização na tabela "quarto"
    def update_quarto(self, connection, id_quarto, tipo, tamanho, id_imovel):
        query = f"UPDATE quarto SET tipo = {tipo}, tamanho = {tamanho}, id_imovel = {id_imovel} WHERE id_quarto = {id_quarto}"
        self.execute_query(connection, query)

    # Exclusão na tabela "quarto"
    def delete_quarto(self, connection, id_quarto):
        query = f"DELETE FROM quarto WHERE id_quarto = {id_quarto}"
        self.execute_query(connection, query)

    # Inserção na tabela "usuario"
    def insert_usuario(self, connection, cpf, nome, senha):
        query = f"INSERT INTO usuario (cpf, nome, senha) VALUES ('{cpf}','{nome}', '{senha}')"
        self.execute_query(connection, query)

    # Atualização na tabela "usuario"
    def update_usuario(self, connection, cpf, nome, senha):
        query = f"UPDATE usuario SET nome = '{nome}', senha = '{senha}' WHERE cpf = {cpf}"
        self.execute_query(connection, query)

    # Exclusão na tabela "usuario"
    def delete_usuario(self, connection, cpf):
        query = f"DELETE FROM usuario WHERE cpf = {cpf}"
        self.execute_query(connection, query)

    # Função para listar os valores das tabelas
    def listar_valores(self, connection):
        try:
            cursor = connection.cursor()

            # Consultar valores de todas as tabelas
            cursor.execute("SELECT * FROM endereco")
            enderecos = cursor.fetchall()

            cursor.execute("SELECT * FROM colega")
            colegas = cursor.fetchall()

            cursor.execute("SELECT * FROM imovel")
            imoveis = cursor.fetchall()

            cursor.execute("SELECT * FROM quarto")
            quartos = cursor.fetchall()

            cursor.execute("SELECT * FROM usuario")
            usuarios = cursor.fetchall()

            # Exibir valores de cada tabela
            print("Valores da tabela 'endereco':")
            for endereco in enderecos:
                print("bairro:", endereco[3])
                print("cidade:", endereco[2])
                print("uf:", endereco[1])
                print()

            cursor.execute("""
                        SELECT c.id_colega, c.tipo, u.nome
                        FROM colega c
                        LEFT JOIN usuario u ON u.id_colega = c.id_colega
                    """)
            colegas_com_usuario = cursor.fetchall()

            print("Valores da tabela 'colega':")
            for colega in colegas_com_usuario:
                print("id_colega:", colega[0])
                print("tipo:", colega[1])
                print("nome:", colega[2])
                cursor.execute(f"SELECT id_avaliacao, nota, descricao FROM avaliacao WHERE id_colega = {colega[0]}")
                avaliacoes = cursor.fetchall()
                for avaliacao in avaliacoes:
                    print('- - -')
                    print("id_avaliacao:", avaliacao[0])
                    print("nota:", avaliacao[1])
                    print("descrição:", avaliacao[2])
                print()

            print("Valores da tabela 'imovel':")
            for imovel in imoveis:
                print("id_imovel:", imovel[0])
                print("banheiros:", imovel[1])
                print("preco:", imovel[2])
                print("id_endereco:", imovel[3])
                cursor.execute(f"SELECT id_avaliacao, nota, descricao FROM avaliacao WHERE id_imovel = {imovel[0]}")
                avaliacoes = cursor.fetchall()
                for avaliacao in avaliacoes:
                    print('- - -')
                    print("id_avaliacao:", avaliacao[0])
                    print("nota:", avaliacao[1])
                    print("descrição:", avaliacao[2])
                print()

            print("Valores da tabela 'quarto':")
            for quarto in quartos:
                print("id_quarto:", quarto[0])
                print("tipo:", quarto[1])
                print("tamanho:", quarto[2])
                print("id_imovel:", quarto[3])
                print()

            print("Valores da tabela 'usuario':")
            for usuario in usuarios:
                print("cpf: ocultado")
                print("nome:", usuario[1])
                print("senha: ocultado")
                print()

        except mysql.connector.Error as e:
            print(f"Erro ao listar valores: {e}")

    def criar_conta(self, connection):
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        senha = input("Digite a senha: ")

        # Verificar se o CPF já está cadastrado
        query = f"SELECT * FROM usuario WHERE cpf = '{cpf}'"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        if result is not None:
            print("CPF já cadastrado. Tente fazer login.")
            return

        # Inserir novo usuário na tabela 'usuario'
        self.insert_usuario(connection, cpf, nome, senha)
        print("Conta criada com sucesso!")


    def fazer_login(self, connection):
        cpf = input("Digite o CPF: ")
        senha = input("Digite a senha: ")

        # Verificar se o CPF e a senha correspondem a um usuário válido
        query = f"SELECT * FROM usuario WHERE cpf = '{cpf}' AND senha = '{senha}'"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        if result is None:
            print("CPF ou senha incorretos. Tente novamente.")
            return False

        self.cpf = result[0]
        print("Login realizado com sucesso!")
        return True


    def consulta_01(self, connection):
        cursor = connection.cursor()
        cursor.execute("""
                            SELECT preco, AVG(tamanho)
                            FROM imovel
                            JOIN quarto ON imovel.id_imovel = quarto.id_imovel
                            GROUP BY preco
                            ORDER BY AVG(tamanho) DESC;
    
                        """)
        consulta = cursor.fetchall()

        print("Preços dos imóveis juntamente com a média do tamanho dos quartos correspondentes, em ordem decrescente de média de tamanho:")
        for resultado in consulta:
            print(resultado)


    def consulta_02(self, connection):
        cursor = connection.cursor()
        cursor.execute("""
                            SELECT imovel.preco, AVG(quarto.tamanho)
                            FROM imovel
                            LEFT JOIN quarto ON imovel.id_imovel = quarto.id_imovel
                            GROUP BY imovel.preco
                            ORDER BY AVG(quarto.tamanho) DESC;
                        """)
        consulta = cursor.fetchall()

        print("Preços dos imóveis de todos os registros da tabela imóvel mesmo que não haja correspondência na tabela quarto")

        for resultado in consulta:
            print(resultado)

    def consulta_03(self, connection):
            cursor = connection.cursor()
            cursor.execute("""
                                    SELECT e.bairro, AVG(i.preco / q.tamanho) AS preco_por_metro_quadrado
                                    FROM imovel i
                                    JOIN endereco e ON i.id_endereco = e.id_endereco
                                    JOIN quarto q ON i.id_imovel = q.id_imovel
                                    GROUP BY e.bairro
                                    ORDER BY preco_por_metro_quadrado DESC;
                                """)
            consulta = cursor.fetchall()

            print("Os bairros mais caros com base no preço por metro quadrado dos imóveis")

            for resultado in consulta:
                print(resultado)

    def menu_inicial(self, connection):
        while True:
            print("--- MENU INICIAL ---")
            print("1. Criar conta")
            print("2. Fazer login")
            print("3. Sair")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.criar_conta(connection)
            elif opcao == "2":
                if self.fazer_login(connection):
                    self.menu_principal(connection)
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_principal(self, connection):
        while True:
            print("\n--- MENU ---")
            print("1. Inserir dados")
            print("2. Atualizar dados")
            print("3. Excluir dados")
            print("4. Listar valores das tabelas")
            print("5. Consulta 01: preços dos imóveis")
            print("6. Consulta 02: preços dos imóveis com LEFT JOIN ")
            print("7. Consulta 03: os bairros mais caros por m2")
            print("8. Sair")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                # Submenu para inserção de dados
                print("\n--- INSERIR DADOS ---")
                print("1. Inserir Endereço")
                print("2. Inserir Colega")
                print("3. Inserir Imóvel")
                print("4. Inserir Quarto")
                print("5. Inserir Usuário")
                print("6. Inserir Avaliação Colega")
                print("7. Inserir Avaliação Imóvel")
                print("8. Voltar")

                sub_opcao = input("Selecione uma opção: ")

                if sub_opcao == "1":
                    print("\n--- Inserir Endereço ---")
                    uf = input("Digite a UF: ")
                    cidade = input("Digite a cidade: ")
                    bairro = input("Digite o bairro: ")
                    self.insert_endereco(connection, uf, cidade, bairro)
                elif sub_opcao == "2":
                    print("\n--- Inserir Colega ---")
                    tipo = input("Digite o tipo de colega: ")
                    self.insert_colega(connection, tipo)
                elif sub_opcao == "3":
                    print("\n--- Inserir Imóvel ---")
                    banheiros = int(input("Digite a quantidade de banheiros: "))
                    preco = float(input("Digite o preço: "))
                    id_endereco = int(input("Digite o ID do endereço: "))
                    self.insert_imovel(connection, banheiros, preco, id_endereco)
                elif sub_opcao == "4":
                    print("\n--- Inserir Quarto ---")
                    tipo = (input("Digite o tipo do quarto (individual/compartilhado): "))
                    tamanho = input("Qual o tamanho, em m2?  ")
                    id_imovel = int(input("Digite o ID do imóvel: "))
                    self.insert_quarto(connection, tipo, tamanho, id_imovel)
                elif sub_opcao == "5":
                    print("\n--- Inserir Usuário ---")
                    cpf = input("Digite o CPF:")
                    nome = input("Digite o nome: ")
                    senha = input("Digite senha: ")
                    self.insert_usuario(connection, cpf, nome, senha)
                elif sub_opcao == "6":
                    print("\n--- Inserir Avaliação Colega ---")
                    nota = input("Digite a nota: ")
                    descricao = input("Digite a descricao: ")
                    id_colega = input("Digite o ID do Colega: ")
                    self.insert_avaliacao(connection, nota, descricao, id_colega=id_colega)
                elif sub_opcao == "7":
                    print("\n--- Inserir Avaliação Imóvel ---")
                    nota = input("Digite a nota: ")
                    descricao = input("Digite a descricao: ")
                    id_imovel = input("Digite o ID do Imóvel: ")
                    self.insert_avaliacao(connection, nota, descricao, id_imovel=id_imovel)
                elif sub_opcao == "8":
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
            elif opcao == "2":
                # Submenu para atualização de dados
                print("\n--- ATUALIZAR DADOS ---")
                print("1. Atualizar Endereço")
                print("2. Atualizar Colega")
                print("3. Atualizar Imóvel")
                print("4. Atualizar Quarto")
                print("5. Atualizar Usuário")
                print("6. Atualizar Avaliação Colega")
                print("7. Atualizar Avaliação Imóvel")
                print("8. Voltar")

                sub_opcao = input("Selecione uma opção: ")

                if sub_opcao == "1":
                    print("\n--- Atualizar Endereço ---")
                    id_endereco = int(input("Digite o ID do endereço a ser atualizado: "))
                    uf = input("Digite a nova UF: ")
                    cidade = input("Digite a nova cidade: ")
                    bairro = input("Digite o novo bairro: ")
                    self.update_endereco(connection, id_endereco, uf, cidade, bairro)
                elif sub_opcao == "2":
                    print("\n--- Atualizar Colega ---")
                    id_colega = int(input("Digite o ID do colega a ser atualizado: "))
                    tipo = input("Digite o novo tipo de colega: ")
                    self.update_colega(connection, id_colega, tipo)
                elif sub_opcao == "3":
                    print("\n--- Atualizar Imóvel ---")
                    id_imovel = int(input("Digite o ID do imóvel a ser atualizado: "))
                    banheiros = int(input("Digite a nova quantidade de banheiros: "))
                    preco = float(input("Digite o novo preço: "))
                    id_endereco = int(input("Digite o novo ID do endereço: "))
                    self.update_imovel(connection, id_imovel, banheiros, preco, id_endereco)
                elif sub_opcao == "4":
                    print("\n--- Atualizar Quarto ---")
                    id_quarto = int(input("Digite o ID do quarto a ser atualizado: "))
                    tipo = float(input("Digite o novo tipo: "))
                    tamanho = input("Digite o novo tamanho: ")
                    id_imovel = int(input("Digite o novo ID do imóvel: "))
                    self.update_quarto(connection, id_quarto, tipo, tamanho, id_imovel)
                elif sub_opcao == "5":
                    print("\n--- Atualizar Usuário ---")
                    cpf = int(input("Digite o CPF do usuário a ser atualizado: "))
                    nome = input("Digite o novo nome: ")
                    senha = input("Digite nova senha: ")
                    self.update_usuario(connection, cpf, nome, senha)
                elif sub_opcao == "6":
                    print("\n--- Atualizar Avaliação de Colega ---")
                    id_avaliacao = int(input("Digite o ID da avaliação a ser atualizada: "))
                    nota = input("Digite a nova nota: ")
                    descricao = input("Digite a nova descricao: ")
                    id_colega = input("Digite o novo ID do Colega: ")
                    self.update_avaliacao(connection, id_avaliacao, nota, descricao, id_colega=id_colega)
                elif sub_opcao == "7":
                    print("\n--- Atualizar Avaliação de Imóvel ---")
                    id_avaliacao = int(input("Digite o ID da avaliação a ser atualizada: "))
                    nota = input("Digite a nova nota: ")
                    descricao = input("Digite a nova descricao: ")
                    id_imovel = input("Digite o novo ID do Imóvel: ")
                    self.update_avaliacao(connection, id_avaliacao, nota, descricao, id_imovel=id_imovel)
                elif sub_opcao == "8":
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
            elif opcao == "3":
                # Submenu para exclusão de dados
                print("\n--- EXCLUIR DADOS ---")
                print("1. Excluir Endereço")
                print("2. Excluir Colega")
                print("3. Excluir Imóvel")
                print("4. Excluir Quarto")
                print("5. Excluir Usuário")
                print("6. Excluir Avaliação")
                print("7. Voltar")

                sub_opcao = input("Selecione uma opção: ")

                if sub_opcao == "1":
                    print("\n--- Excluir Endereço ---")
                    id_endereco = int(input("Digite o ID do endereço a ser excluído: "))
                    self.delete_endereco(connection, id_endereco)
                elif sub_opcao == "2":
                    print("\n--- Excluir Colega ---")
                    id_colega = int(input("Digite o ID do colega a ser excluído: "))
                    self.delete_colega(connection, id_colega)
                elif sub_opcao == "3":
                    print("\n--- Excluir Imóvel ---")
                    id_imovel = int(input("Digite o ID do imóvel a ser excluído: "))
                    self.delete_imovel(connection, id_imovel)
                elif sub_opcao == "4":
                    print("\n--- Excluir Quarto ---")
                    id_quarto = int(input("Digite o ID do quarto a ser excluído: "))
                    self.delete_quarto(connection, id_quarto)
                elif sub_opcao == "5":
                    print("\n--- Excluir Usuário ---")
                    cpf = int(input("Digite o CPF do usuário a ser excluído: "))
                    self.delete_usuario(connection, cpf)
                elif sub_opcao == "6":
                    print("\n--- Excluir Avaliação ---")
                    id_avaliacao = int(input("Digite o ID da avaliação a ser excluída: "))
                    self.delete_avaliacao(connection, id_avaliacao)
                elif sub_opcao == "7":
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
            elif opcao == "4":
                print("\n--- LISTAR VALORES DAS TABELAS ---")
                self.listar_valores(connection)
            elif opcao == "5":
                self.consulta_01(connection)
            elif opcao == "6":
                self.consulta_02(connection)
            elif opcao == "7":
                self.consulta_03(connection)
            elif opcao == "8":
                break
            else:
                print("Opção inválida. Tente novamente.")


    # Função principal para realizar as operações
    def main(self):
        # Conectar ao banco de dados
        connection = self.connect()

        if connection is not None:
            self.menu_inicial(connection)
            # Fechar conexão com o banco de dados
            connection.close()
        else:
            print("Erro ao conectar ao banco de dados")

# Executar a função principal
if __name__ == "__main__":
    Programa().main()
