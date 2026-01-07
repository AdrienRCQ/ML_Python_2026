import numpy as np

def beginner_arrays():
    A = np.array([1, 2, 3])
    print("\n Array A : \n", A)
    print("dimension : ", A.ndim," / shape : ", A.shape," / size : ", A.size)

    B = np.zeros((3, 2)) # Création d'un tableau de dimension 2 remplie de 0
    print("\n Array B : \n", B)
    print("dimension : ", B.ndim," / shape : ", B.shape," / size : ", B.size)

    C = np.ones((3, 4)) # Création d'un tableau de dimension 2 remplie de 0
    print("\n Array C : \n", C)
    print("dimension : ", C.ndim," / shape : ", C.shape," / size : ", C.size)

    D = np.full((3, 2), 9) # Création d'un tableau de dimension 2 remplie de 9
    print("\n Array D : \n", D)
    print("dimension : ", D.ndim," / shape : ", D.shape," / size : ", D.size)

    E = np.random.randn(3, 4)
    print("\n Array E : \n", E)
    print("dimension : ", E.ndim," / shape : ", E.shape," / size : ", E.size)

    F = np.eye(4) # Création d'une matrice identité de shape 4
    print("\n Array F : \n", F)
    print("dimension : ", F.ndim," / shape : ", F.shape," / size : ", F.size)

    G = np.linspace(0, 10, 20)
    print("\n linspace : \n", G)
    print("dimension : ", G.ndim," / shape : ", G.shape," / size : ", G.size)

    H = np.arange(0, 10, 0.5)
    print("\n arrange : \n", H)
    print("dimension : ", H.ndim," / shape : ", H.shape," / size : ", H.size)

def manipulations_array():
    Array_A = np.zeros((3, 2))
    print("\n arrange : \n", Array_A)
    print("dimension : ", Array_A.ndim," / shape : ", Array_A.shape," / size : ", Array_A.size)

    Array_B = np.ones((3, 2))
    print("\n arrange : \n", Array_B)
    print("dimension : ", Array_B.ndim," / shape : ", Array_B.shape," / size : ", Array_B.size)

    C = np.hstack((Array_A, Array_B))
    print("\n Horizontal stack : \n", C)
    print("dimension : ", C.ndim," / shape : ", C.shape," / size : ", C.size)

    D = np.vstack((Array_A, Array_B))
    print("\n Vertical stack : \n", D)
    print("dimension : ", D.ndim," / shape : ", D.shape," / size : ", D.size)

# beginner_arrays()
manipulations_array()