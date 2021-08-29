import linearalgebra as LA
import numpy as np
import os

f=open("instruction.txt","r")
print(f.read())
print("\n")

arrs=[]

for file in os.listdir():
    if file.endswith(".csv"):
        LA.loadarr(arrs,file)
print("\n")

LA.display(arrs)
print("\n")

while 0==0:
    operator=input("Enter command:")
    if operator=="+":
        arr1=arrs[int(input("Enter the number of first array:"))]
        arr2=arrs[int(input("Enter the number of second array:"))]
        ANS=LA.add(arr1,arr2)
        print(str(arr1)+"\n+\n"+str(arr2)+"\n=\n"+str(ANS))
        operator=input("Enter s to save the result:")
        if operator=="s":
            LA.save(arrs,ANS)
    elif operator=="-":
        arr1=arrs[int(input("Enter the number of first array:"))]
        arr2=arrs[int(input("Enter the number of second array:"))]
        ANS=LA.difference(arr1,arr2)
        print(str(arr1)+"\n-\n"+str(arr2)+"\n=\n"+str(ANS))
        operator=input("Enter s to save the result:")
        if operator=="s":
            LA.save(arrs,ANS)
    elif operator=="kA":
        arr=arrs[int(input("Enter the number of array:"))]
        scalar=float(input("Enter the scalar."))
        ANS=LA.scalar_product(arr,scalar)
        print(str(arr)+"\n*\n"+str(scalar)+"\n=\n"+str(ANS))
        operator=input("Enter s to save the result:")
        if operator=="s":
            LA.save(arrs,ANS)
    elif operator=="*":
        arr1=arrs[int(input("Enter the number of first array:"))]
        arr2=arrs[int(input("Enter the number of second array:"))]
        ANS=LA.product(arr1,arr2)
        print(str(arr1)+"\n*\n"+str(arr2)+"\n=\n"+str(ANS))
        operator=input("Enter s to save the result:")
        if operator=="s":
            LA.save(arrs,ANS)
    elif operator=="t":
        LA.display(arrs)
        arr=arrs[int(input("Enter the number of array:"))]
        ANS=np.transpose(arr)
        print("t"+"\n"+str(arr)+"\n=\n"+str(ANS))
        operator=input("Enter s to save the result:")
        if operator=="s":
            LA.save(arrs,ANS)
    elif operator=="-1":
        LA.display(arrs)
        arr=arrs[int(input("Enter the number of array:"))]
        LA.regular_matrix(arr)
    elif operator=="d":
        LA.display(arrs)
    elif operator=="v":
        file=input("Enter the file name:")
        LA.loadarr(arrs,file)
        print("Array "+ str(len(arrs)-1))
        print(arrs[-1])
    elif operator=="x":
        LA.display(arrs)
        operator=int(input("Enter the number of array to delete:"))
        arrs.pop(operator)
        LA.display(arrs)
    elif operator=="n":
        LA.display(arrs)
        arr=arrs[int(input("Enter the number of array to export:"))]
        LA.export(arr)
    elif operator=="help":
        print("\n")
        f=open("instruction.txt","r")
        print(f.read())
    elif operator=="exit":
        operator=input("Enter y to end the program:")
        if operator=="y":
            exit()
    print("\n")

