import matplotlib.pyplot as plt
import numpy as np


def exponential_menu():
    while True:
        print("\n==========================\n")

        try:
            a = float(input("Valor de a: "))
        except ValueError:
            print("\nErro de entrada. Certifique-se de digitar apenas números.")
            continue

        if a <= 0:
            print("A função é inválida.")
            continue

        print(f"\nFunção a ser trabalhada: f(x) = {a}^x")

        print("\n==========================\n")
        print("OPÇÕES PARA FUNÇÃO EXPONENCIAL:\n1: Verificar se é crescente ou decrescente\n2: Calcular a função em um valor de x\n3: Gerar gráfico\n4: Voltar")
        print("\n==========================\n")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                check_growth(a)
            case "2":
                calc_fx(a)
            case "3":
                generate_graph(a)
            case "4":
                break
            case _:
                print("\nOpção inválida, insira um número de 1 a 4\n")


def check_growth(a):
    if 0 < a < 1:
        print("A função é decrescente.")
    elif a > 1:
        print("A função é crescente.")
    elif a == 1:
        print("A função é constante.")


def calc_fx(a):
    while True:
        try:
            x = float(input("Digite o valor de x: "))
            break
        except ValueError:
            print("\nErro de entrada. Certifique-se de digitar um número válido para x.")
    
    fx = a ** x
    print(f"f({x}) = {fx}")


def generate_graph(a):
    x = np.linspace(-10, 10, 100)
    y = a * np.exp(x)

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Gráfico da função f(x) = {a}^x")
    plt.grid(True)
    plt.show()