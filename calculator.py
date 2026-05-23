#calculator -- it can (+,-,*,/,%,** and gives factorial for one positive number) it can get two numbers as input each time we use

 
while True:
  num1=float(input("enter a number: "))
  operator=input("enter operator (+,-,*,/,%,**,!):")
  
  if operator=="!":
    
            if num1>0:
                fact=1
                temp=num1
                while (temp>0):
                    fact=fact*temp
                    temp=temp-1
                print(fact)
            else:
                print("factorial not works for nagative numbers")
            again=input("calculate again(y/n):")
            if again=="n":
                print("closed.")
       
  else:
            num2=float(input("enter a number: "))
 
 
            if operator=="+":
                add=num1+num2
                print(add) 

            elif operator=="-":
                sub=num1-num2
                print(sub)

            elif operator=="*":
                mul=num1*num2
                print(mul)

            elif operator=="/":
                if num2!=0:
                    div=num1/num2
                    print(div)
                else :
                    print ("zero division error!")

            elif operator=="%":
                mod=num1%num2
                print(mod) 

            elif operator=="**":
                pow=num1**num2
                print(pow)

            else:
                print("invalid operator!")  

                again=input("calculate again(y/n): ")
                if again=="n":
                    print ("closed.")
                break
     


