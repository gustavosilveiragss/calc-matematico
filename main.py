import set_operations_menu
import quadratic_menu
import exponential_menu
import matrix_menu

while True:
    print("Selecione uma opção:")
    print("1. Conjuntos numéricos")
    print("2. Funções do segundo grau")
    print("3. Funções exponenciais")
    print("4. Matriz")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")

    match escolha:
        case "1":
            set_operations_menu.set_operations_menu()
        case "2":
            quadratic_menu.quadratic_menu()
        case "3":
            exponential_menu.exponential_menu()
        case "4":
            matrix_menu.matrix_menu()
        case "5":
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
