import matplotlib.pyplot as plt
import numpy as np


def exponencial_menu():
    while True:
        print("\n==========================\n")

        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))

        print(f"\nFunção a ser trabalhada: f(x) = {a}x + {b}")

        print("\n==========================\n")
        print("OPÇÕES PARA FUNÇÃO LINEAR:\n1: Verificar se é crescente ou decrescente\n2: Calcular a função em um valor de x\n3: Gerar gráfico\n4: Voltar")
        print("\n==========================\n")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            verificar_crescimento(a, b)
        elif choice == "2":
            calcular_funcao(a, b)
        elif choice == "3":
            gerar_grafico(a, b)
        elif choice == "4":
            break
        else:
            print("\nOpção inválida, insira um número de 1 a 4\n")


def verificar_crescimento(a, b):
    if a > 0:
        print("A função é crescente.")
    elif a < 0:
        print("A função é decrescente.")
    else:
        print("A função é constante.")


def calcular_funcao(a, b):
    x = float(input("Digite o valor de x: "))
    resultado = a * x + b
    print(f"f({x}) = {resultado}")


def gerar_grafico(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Gráfico da função f(x) = {a}x + {b}")
    plt.grid(True)
    plt.show()
