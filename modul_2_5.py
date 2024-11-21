
n = input("количество строк")
m = input("количество столбцов")
valye = input("значения")
print(n,m,valye)
def get_matrix(n, m, valye):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(valye)
        print(matrix)











