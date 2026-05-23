#for loops
x = int(input())        
y = int(input())
z = int(input())
n = int(input())
a=[]
p=0
for i in range(1,x):
    p=p+i
    a.append(p)
b=[]
q=0    
for j in range(1,y):
    q=q+j
    b.append(q)
c=[] 
r=0   
for k in range(1,z):
    r=r+k
    c.append(r) 
       
print(a,",",b,",",c)        
        