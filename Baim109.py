def l2norm(matrix):
    hasil = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            hasil += matrix[i][j] ** 2
    return hasil ** 0.5


def transpose(matrix):
    baris = len(matrix)
    kolom = len(matrix[0])

    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matrix[i][j]
            
    return hasil

def tambah(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("Ukuran matriks tidak sama")

    hasil = []
    for i in range(len(matrix_1)):
        baris = []
        for j in range(len(matrix_1[0])):
            baris.append(matrix_1[i][j] + matrix_2[i][j])
        hasil.append(baris)
    return hasil