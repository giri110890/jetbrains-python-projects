# Author giri110890
def add_matrices(k, l):
    temp = []
    for i in range(len(k)):
        tempa = []
        for j in range(len(k[0])):
            tempa.append(float(k[i][j]) + float(l[i][j]))
        temp.append(tempa)
    return temp


def multiply_matrix_by_constant(k, factor):
    temp = []
    for i in range(len(k)):
        tempa = []
        for j in range(len(k[0])):
            tempa.append(float(k[i][j]) * factor)
        temp.append(tempa)
    return temp


def multiply_matrices(k, l):
    temp = []
    for i in range(len(k)):
        tempa = []
        for j in range(len(l[0])):
            answer = 0
            for s in range(len(k[0])):
                answer += float(k[i][s]) * float(l[s][j])
            tempa.append(answer)
        temp.append(tempa)
    return temp


def create_matrix(p, q):
    a = []
    for _ in range(int(p)):
        a.append(input().split())
    return a


def main_diagonal(k):
    temp = []
    for i in range(len(k)):
        tempa = []
        for j in range(len(k[0])):
            tempa.append(float(k[j][i]))
        temp.append(tempa)
    return temp


def side_diagonal(k):
    temp = []
    for j in range(len(k) - 1, -1, -1):
        tempa = []
        for i in range(len(k[0]) - 1, -1, -1):
            tempa.append(float(k[i][j]))
        temp.append(tempa)
    return temp


def vertical_line(k):
    temp = []
    for i in range(len(k)):
        tempa = []
        for j in range(len(k[0]) - 1, -1, -1):
            tempa.append(float(k[i][j]))
        temp.append(tempa)
    return temp


def horizontal_line(k):
    temp = []
    for i in range(len(k) - 1, -1, -1):
        tempa = []
        for j in range(len(k[0])):
            tempa.append(float(k[i][j]))
        temp.append(tempa)
    return temp


def sub_matrix(i, j, matrix):
    minor = []
    for x in range(0, len(matrix)):
        if x != i:
            z = []
            for y in range(0, len(matrix[0])):
                if y != j:
                    z.append(matrix[x][y])
            minor.append(z)
    return minor


def calculate_determinant(matrix):
    if len(matrix) == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
    elif len(matrix) == 1:
        return float(matrix[0][0])
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += pow(-1, 0 + i) * float(matrix[0][i]) * calculate_determinant(sub_matrix(0, i, matrix))
    return determinant


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    print()


while 1:
    user_choice = input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:''')
    if user_choice == "1":
        m, n = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        matrix_1 = create_matrix(int(m), int(n))
        p, q = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        matrix_2 = create_matrix(int(p), int(q))
        if not m == p and not n == q:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(add_matrices(matrix_1, matrix_2))
    elif user_choice == "2":
        m, n = input("Enter size of matrix:").split()
        print("Enter matrix:")
        matrix_1 = create_matrix(int(m), int(n))
        multiplication_factor = float(input("Enter constant:"))
        print("The result is:")
        print_matrix(multiply_matrix_by_constant(matrix_1, multiplication_factor))
    elif user_choice == "3":
        m, n = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        matrix_1 = create_matrix(int(m), int(n))
        p, q = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        matrix_2 = create_matrix(int(p), int(q))
        if not n == p:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(multiply_matrices(matrix_1, matrix_2))
    elif user_choice == "4":
        choice = input('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:''')
        m, n = input("Enter matrix size:").split()
        print("Enter matrix:")
        matrix_1 = create_matrix(int(m), int(n))
        if choice == "1":
            print("The result is:")
            print_matrix(main_diagonal(matrix_1))
        elif choice == "2":
            print("The result is:")
            print_matrix(side_diagonal(matrix_1))
        elif choice == "3":
            print("The result is:")
            print_matrix(vertical_line(matrix_1))
        elif choice == "4":
            print("The result is:")
            print_matrix(horizontal_line(matrix_1))
    elif user_choice == "5":
        m, n = input("Enter matrix size:").split()
        if m != n:
            print("The operation cannot be performed.")
        else:
            print("Enter matrix:")
            matrix_1 = create_matrix(int(m), int(n))
            print("The result is:")
            print(calculate_determinant(matrix_1))
            print()
    elif user_choice == "6":
        m, n = input("Enter matrix size:").split()
        if m != n:
            print("The operation cannot be performed.")
        else:
            print("Enter matrix:")
            matrix_1 = create_matrix(int(m), int(n))
            if calculate_determinant(matrix_1) == 0:
                print("This matrix doesn't have an inverse")
                print()
            else:
                b = []
                for i in range(int(m)):
                    c = []
                    for j in range(int(n)):
                        c.append(pow(-1, i + j) * calculate_determinant(sub_matrix(i, j, matrix_1)))
                    b.append(c)
                multiplication_factor = 1 / calculate_determinant(matrix_1)
                b_transpose = main_diagonal(b)
                print("The result is:")
                print_matrix(multiply_matrix_by_constant(b_transpose, multiplication_factor))
    elif user_choice == "0":
        break
    else:
        print("The operation cannot be performed.")