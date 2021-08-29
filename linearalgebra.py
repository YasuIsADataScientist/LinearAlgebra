import numpy as np
import sympy as sp

def loadarr(X,arrfile):
    with open(arrfile) as file_name:
        arr = np.loadtxt(file_name, delimiter=",")
        if len(arr.shape)==1:
            print(arrfile)
            print(arr)
            convert=input("Enter c to convert to column vector:")
            if convert=="c":
                arr=arr.reshape(arr.shape[0],1)
            else:
                arr=[arr.tolist()]
                arr=np.array(arr)
    X.append(arr)

def display(X):
    i=0
    for x in X:
        print("Array " + str(i))
        print(x)
        i=i+1

def add(A,B):
    S=[[A[j,i]+B[j,i] for i in range(A.shape[1])]
       for j in range(A.shape[0])]
    S=np.array(S)
    return S

def difference(A,B):
    D=[[A[j,i]-B[j,i] for i in range(A.shape[1])]
       for j in range(A.shape[0])]
    D=np.array(D)
    return D

def scalar_product(A,k):
    kA=[[A[j,i]*k for i in range(A.shape[1])]
       for j in range(A.shape[0])]
    kA=np.array(kA)
    return kA

def product(A,B):
    if A.shape[0]!=B.shape[1]:
        return "Column of A does not meet to row of B."
    else:
        def element(i,j):
            c=[A[i,k]*B[k,j] for k in range(A.shape[1])]
            return sum(c)
        AB=[[element(i,j)
             for j in range(B.shape[1])]
            for i in range(A.shape[0])]
        AB=np.array(AB)
        return AB

def regular_matrix(A):
    if A.shape[0]!=A.shape[1]:
        return "The matrix is not square."
    else:
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        B=[alphabet[x] for x in range(A.shape[0]*A.shape[1])]
        sp.var(x for x in B)
        B=np.array(B)
        B=B.reshape(A.shape[0],A.shape[1])
        print(B)
        sp.init_printing()


def save(X,A):
    X.append(A)
    print("Array "+ str(len(X)-1))
    print(X[-1])

def export(A):
    f_name=input("Enter the file name:")
    np.savetxt(f_name + ".csv", A, delimiter=',')