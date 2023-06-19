def print_matrix(matrix):
    for row in matrix:
        print(row)


def get_matrix_input():
    num_rows = int(input("Informe o número de linhas da matriz: "))
    num_cols = int(input("Informe o número de colunas da matriz: "))

    matrix = []
    for _ in range(num_rows):
        row = []

        for _ in range(num_cols):
            element = float(input("Informe um elemento da matriz: "))
            row.append(element)

        matrix.append(row)

    return matrix


def determinant(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows == num_cols:
        det = None

        if num_rows == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        elif num_rows == 3:
            det = (
                matrix[0][0] * matrix[1][1] * matrix[2][2]
                + matrix[0][1] * matrix[1][2] * matrix[2][0]
                + matrix[0][2] * matrix[1][0] * matrix[2][1]
                - matrix[0][2] * matrix[1][1] * matrix[2][0]
                - matrix[0][0] * matrix[1][2] * matrix[2][1]
                - matrix[0][1] * matrix[1][0] * matrix[2][2]
            )

        else:
            print("Apenas matrizes 2x2 e 3x3 são suportadas para cálculo de determinante.")
        
        return det
    
    print("A matriz não é quadrada. O determinante só pode ser calculado para matrizes quadradas.")

    return None


def matrix_multiplication(matrix1, matrix2):
    num_cols1 = len(matrix1[0])
    num_rows2 = len(matrix2)

    if num_cols1 == num_rows2:
        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result
    
    print("A multiplicação de matrizes não é possível. O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

    return None


def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed = [[matrix[j][i] for j in range(num_rows)] for i in range(num_cols)]

    return transposed


def matrix_menu():
    while True:
        print("\n==========================\n")
        matrix = get_matrix_input()
        print("\n==========================\n")
        print("OPÇÕES PARA OPERAÇÕES COM MATRIZES:")
        print("1: Imprimir matriz")
        print("2: Calcular determinante")
        print("3: Realizar multiplicação de matrizes")
        print("4: Calcular matriz transposta")
        print("5: Voltar")
        print("\n==========================\n")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                print("Matriz:")
                print_matrix(matrix)
            case "2":
                det = determinant(matrix)
                if det is not None:
                    print("O determinante da matriz é:", det)
            case "3":
                matrix2 = get_matrix_input()
                print("Resultado da multiplicação:")
                result = matrix_multiplication(matrix, matrix2)
                if result is not None:
                    print_matrix(result)
            case "4":
                transposed = transpose(matrix)
                print("Matriz transposta:")
                print_matrix(transposed)
            case "5":
                break
            case _:
                print("\nOpção inválida, insira um número de 1 a 5\n")


