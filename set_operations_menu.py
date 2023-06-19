def set_operations_menu():
    while True:
        print("\n==========================\n")

        set_a_input = input("Conjunto A (separe os elementos por vírgula): ")
        set_b_input = input("Conjunto B (separe os elementos por vírgula): ")

        if not set_a_input.isdigit() or not set_b_input.isdigit():
            print("\nErro de entrada. Certifique-se de digitar apenas números.")
            continue

        set_a = set(map(int, set_a_input.split(",")))
        set_b = set(map(int, set_b_input.split(",")))
        
        print("\n==========================\n")
        print("OPÇÕES PARA OPERAÇÕES COM CONJUNTOS:\n1: Verificar se A é subconjunto próprio de B\n2: Realizar operação de União\n3: Calcular interseção\n4: Calcular diferença\n5: Voltar")
        print("\n==========================\n")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                check_subset(set_a, set_b)
            case "2":
                union(set_a, set_b)
            case "3":
                intersection(set_a, set_b)
            case "4":
                difference(set_a, set_b)
            case "5":
                break
            case _:
                print("\nOpção inválida, insira um número de 1 a 5\n")


def check_subset(set_a, set_b):
    if set_a.issubset(set_b):
        if set_a == set_b:
            print("A é igual a B")

            return
        
        print("A é subconjunto próprio de B")
        
        return

    print("A não é subconjunto de B")


def union(set_a, set_b):
    set_union = set_a.union(set_b)
    print(f"A união de A e B é: {set_union}")


def intersection(set_a, set_b):
    set_intersection = set_a.intersection(set_b)
    print(f"A interseção de A e B é: {set_intersection}")


def difference(set_a, set_b):
    set_difference = set_a.difference(set_b)
    print(f"A diferença entre A e B é: {set_difference}")
