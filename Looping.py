#While Loop
'''i=1
while(i <= 10):
    print(i)
    i+=1
print("-----------") 
print("Even Number:")
i=0
while(i <= 20):
     print(i)
     i+=2

 #Continue Statement
 #to print odd number using continue statement
i=1
print("odd number:")
while(i <= 20):
     if (i%2 == 0):
        i+=1
        continue; 
     print(i)
     i+=1

#Break Statement
i=1
while(i<=10):
    if i==7:
     break
    print(i)
    i+=1

#Range
a=list(range(5))
print(a)
print(list(range(2,10)))
print("Even Number:")
print(list(range(0,21,2)))

#For Loop
for i in range(5):
    print(i)
print("Odd Number:") 
for i in range(1,10,2):
    print(i)

for i in range(3):
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a+b
    print(c)

#Nested For Loop
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")

print("----------")    

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("-----------")
for i in range(65,71,1):
    for j in range(65,71,1):
        print(chr(j),end="")
    print("")

#While Else 
i=1
while(i<=5):
    print(i)
    i+=1
else:
    print("Loop ended") 

print("--------") 
i=1
while(i<=5):
    if i==3:
        break
    print(i)
    i+=1
else:
    print("Loop ended") '''

#For Else
for i in range(5):
    print(i)
else:
    print("loop end")    




   







             
         
   