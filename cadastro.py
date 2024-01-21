def cadastrar(pessoas):
    cpf = input("Digite seu cpf: ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    pessoas.append((cpf, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"nome: {nome}, idade: {idade} e cpf: {cpf}")

def exibirMenu():
    print('''\n Escolha uma opção:
    1: Cadastrar pessoa
    2: Listar pessoa
    3: Sair''')

def main():
    pessoas = []
    flag = True
    while flag:
        exibirMenu()
        try:
            opcao = int(input("Digite a opcao: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag =  False
            else:
                print("Opcao Invalida")
        except ValueError:
            print("Digite somente numeros")

main()

