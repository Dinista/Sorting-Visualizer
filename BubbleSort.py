swapped = True

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def Bubble_Sort(A):
    if len(A) == 1:
        return
    global swapped;
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


#----------TESTES----------
#Como o retorno da função é um generator, para que possamos testar, percorremos até o ultimo interator (colocando em um vetor) para ver se é o resultado correto
def Test (Vetor):
    aux =[]
    for i in Bubble_Sort(Vetor): aux.append(i)
    return aux

assert Test([12, 2, 0, 1, 3, 6, 4, 9, 10])[9 - 1] == [0, 1, 2, 3, 4, 6, 9, 10, 12]
assert Test([15, 11, 7, 6, 8, 9, 0, 13, 21, 19, 34])[12 - 1] == [0, 6, 7, 8, 9, 11, 13, 15, 19, 21, 34]
assert Test([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])[15 - 1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
assert Test([2, 4, 6, 8, 10, 12, 14, 13, 11, 9, 7, 5, 3, 1])[14 - 1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
assert Test([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2])[20 - 1] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]