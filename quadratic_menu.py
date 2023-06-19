import matplotlib.pyplot as plt
import numpy as np


def quadratic_menu():
    while True:
        print("\n==========================\n")

        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        c = float(input("Valor de c: "))

        print(f"\nFunção a ser trabalhada: y = {a}x^2 + {b}x + {c}")

        print("\n==========================\n")
        print("OPÇÕES PARA FUNÇÃO DE SEGUNDO GRAU:\n1: Determinar as raízes (zeros)\n2: Determinar o vértice\n3: Gerar o gráfico da função\n4: Voltar")
        print("\n==========================\n")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                determine_roots(a, b, c)
            case "2":
                determine_vertex(a, b, c)
            case "3":
                generate_graph(a, b, c)
            case "4":
                break
            case _:
                print("\nOpção inválida, insira um número de 1 a 4\n")


def determine_roots(a, b, c):

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("A função não possui raízes reais")
        return
    
    if delta == 0:
        r = -b / (2 * a)
        print(f"A função possui uma raiz real: {r}")
        return
    
    r1 = (-b + np.sqrt(delta)) / (2 * a)
    r2 = (-b - np.sqrt(delta)) / (2 * a)
    print(f"A função possui duas raízes reais: {r1} e {r2}")


def determine_vertex(a, b, c):
    xv = -b / (2 * a)
    yv = a * xv ** 2 + b * xv + c
    print(f"O vértice da função está em ({xv}, {yv})")


def generate_graph(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a * x ** 2 + b * x + c

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Gráfico da Função Quadrática: y = {a}x^2 + {b}x + {c}")
    plt.grid(True)
    plt.show()
