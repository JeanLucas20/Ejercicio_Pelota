



# Input
h= int(input("Ingrese la altura inicial: "))

b= h/5
n= 0

# Processing
while  h>b:
    
    h= h-(0.1*h)
    n= n+1

# Output
    print ("Dio", str(n), " rebotes hasta llegar a su quinta parte de altura, y su altura fue de ", str(h))


