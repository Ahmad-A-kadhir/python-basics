#collection--list,tuple,set,dictionaries
#  -list[]= > allows duplicate,can store any data type,can modifiable
#            list.append(),list.insert(),list.pop(),list.extend()
#  -tuple()= > allows duplicate,can store any data type,but can't modify,tuple=list()


a=(1,2,3,4,5,6,7)
b=list(a)
b.pop(6)
print(b)