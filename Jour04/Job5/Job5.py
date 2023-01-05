def liste():
    L = [1, 2, 3, 4, 5]
    return L

def remplacer(L):
    L[3] = L[2] + L[4]

L = liste()
print(L[1])
remplacer(L)
print(L[-1])