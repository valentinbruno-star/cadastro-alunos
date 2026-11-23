
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2


alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")

    while True:
        try:
            nota1 = float(input("Digite a primeira nota (0 a 10): "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("Nota invalida! Digite de 0 a 10.")
        except ValueError:
            print("Digite um numero valido.")

    while True:
        try:
            nota2 = float(input("Digite a segunda nota (0 a 10): "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("Nota invalida! Digite de 0 a 10.")
        except ValueError:
            print("Digite um numero valido.")

    aluno = Aluno(nome, nota1, nota2)
    alunos.append(aluno)

    salvar_alunos()
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- LISTA DE ALUNOS ---")

        for aluno in alunos:
            print(f"Nome: {aluno.nome}")
            print(f"Nota 1: {aluno.nota1}")
            print(f"Nota 2: {aluno.nota2}")
            print(f"Media: {aluno.media():.2f}")

            if aluno.media() >= 6:
                print("Situacao: Aprovado")
            else:
                print("Situacao: Recuperacao")

            print("----------------------")


def buscar_aluno():
    nome_busca = input("Digite o nome do aluno: ")

    encontrado = False

    for aluno in alunos:
        if aluno.nome.lower() == nome_busca.lower():
            print(f"\nNome: {aluno.nome}")
            print(f"Nota 1: {aluno.nota1}")
            print(f"Nota 2: {aluno.nota2}")
            print(f"Media: {aluno.media():.2f}")

            if aluno.media() >= 6:
                print("Situacao: Aprovado")
            else:
                print("Situacao: Recuperacao")

            encontrado = True

    if not encontrado:
        print("Aluno nao encontrado.")


def salvar_alunos():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno.nome};{aluno.nota1};{aluno.nota2}\n")


def carregar_alunos():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) == 3:
                    nome = dados[0]
                    nota1 = float(dados[1])
                    nota2 = float(dados[2])

                    aluno = Aluno(nome, nota1, nota2)
                    alunos.append(aluno)

    except FileNotFoundError:
        pass


carregar_alunos()


while True:
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opcao invalida!")
