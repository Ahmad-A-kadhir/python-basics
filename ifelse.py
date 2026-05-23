#booleans= true ,false

a=int(input("maths : "))
b=int(input("science : "))
c=int(input("enlish : "))
d=int(input("ICT : "))
e=int(input("GK : "))

add=a+b+c+d+e
Avarage=add/5
print(Avarage)
if Avarage<35:
    print("additional class is requierd!")
else:
    print ("you are good to go!")