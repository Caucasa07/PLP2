import psycopg2
from psycopg2 import sql

class GerenciadorFilmes:
    def __init__(self):
        self.conexao = self.conectar_bd()

    def conectar_bd(self):
        # Altere as informações de conexão conforme necessário
        return psycopg2.connect(
            database="seu_banco_de_dados",
            user="seu_usuario",
            password="sua_senha",
            host="localhost",
            port="5432"
        )

class Vendedor:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def cadastrar_vendedor(self):
        nome = input("Digite o nome do vendedor: ")
        salario = float(input("Digite o salário do vendedor: "))

        with GerenciadorFilmes().conexao as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO vendedores (nome, salario) VALUES (%s, %s)", (nome, salario))
                conexao.commit()

        print(f"Vendedor {nome} cadastrado com sucesso!")

    def listar_vendedores(self):
        with GerenciadorFilmes().conexao as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM vendedores")
                vendedores = cursor.fetchall()

                print("Lista de Vendedores:")
                for vendedor in vendedores:
                    print(f"ID: {vendedor[0]}, Nome: {vendedor[1]}, Salário: {vendedor[2]}")

class Cliente:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        email = input("Digite o email do cliente: ")

        # Lógica para cadastrar o cliente no banco de dados

        print(f"Cliente {nome} cadastrado com sucesso!")

    def listar_clientes(self):
        # Lógica para listar todos os clientes no banco de dados
        # e exibir as informações

        print("Lista de Clientes:")

class Transacao:
    def __init__(self, id_filme, id_cliente, id_vendedor, data_aluguel):
        self.id_filme = id_filme
        self.id_cliente = id_cliente
        self.id_vendedor = id_vendedor
        self.data_aluguel = data_aluguel

    def realizar_transacao(self):
        id_filme = int(input("Digite o ID do filme a ser alugado: "))
        id_cliente = int(input("Digite o ID do cliente: "))
        id_vendedor = int(input("Digite o ID do vendedor: "))
        data_aluguel = input("Digite a data do aluguel (AAAA-MM-DD): ")

        # Lógica para registrar a transação no banco de dados

        print("Transação realizada com sucesso!")

class Filme:
    def __init__(self, nome, genero, ano, status, data_registro=None):
        self.nome = nome
        self.genero = genero
        self.ano = ano
        self.status = status
        self.data_registro = data_registro

class Estoque:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)
        print(f"Filme {filme.nome} adicionado ao estoque.")

    def listar_filmes(self):
        print("Lista de Filmes no Estoque:")
        for filme in self.filmes:
            print(f"Nome: {filme.nome}, Gênero: {filme.genero}, Ano: {filme.ano}, Status: {filme.status}")

# Exemplo de uso das novas classes
estoque = Estoque()
filme1 = Filme("Filme A", "Ação", 2021, 1, "2023-11-30")
filme2 = Filme("Filme B", "Comédia", 2022, 0)

estoque.adicionar_filme(filme1)
estoque.adicionar_filme(filme2)
estoque.listar_filmes()