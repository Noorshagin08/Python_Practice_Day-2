#to check odd or even

# num=int(input("Enter number:"))
# if (num%2 == 0):
#     print(num," ia an Even number")
# else:
#     print(num," ia an odd number")   

# list=[1,2,3,4,5]
# for i in list:
#     if (i%2 == 0):
#         print(i," ia an Even number")
#     else:
#         print(i," ia an odd number")     


# for a in range(3):
#     i=int(input("Enter Number:"))
#     if (i%2 == 0):
#         print(i," ia an Even number")
#     else:
#         print(i," ia an odd number")     

    
# num=[]
# a=1
# while(a <= 3):
#     i=int(input("Enter Number:"))
#     num.append(i)
#     a+=1
# print(num)
# for n in num:
#     if (n%2 == 0):
#         print(n," ia an Even number")
#     else:
#         print(n," ia an odd number")     




#To check the given input is palindrome
# a=input("Enter num or word:") 
# b=(a[::-1])
# if (a==b):
#     print(a, " is palindrome")
# else: 
#     print(a, " is not palindrome")   


#Another Method for Palindrome
# s = input("Enter a string: ")
# is_palindrome = True

# for i in range(len(s) // 2):
#     if s[i] != s[-(i + 1)]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")






#Factorial
# a=3
# num=1
# for i in range(1,a+1):
#     b=i*num
#     num=b
# print(b)   



#Fibonacci =>0 1 1 2 3 5 8 

# num=int(input("Enter Number:"))
# a=0
# b=1
# sum=0
# for i in range(num):
#     sum=sum+a #0  1 2 4
#     a,b=b,a+b #1,1 1,2  2,3 3,5
# print(sum)
  
total=0
j=0 

while True: 
 n=int(input("Enter no of item :"))
 
 for i in range(n):
   item=input("Enter amount of item {} :".format(j+1))
   j=j+1 
   

   if item == "":
    item="0"
    j=j-1
   total=total+float(item)
 print("Total",total) 

 x=input("do you want to continue ? 'yes' : 'no'")
 if x=="yes":
  continue
 else:
  print("Total no of product",j)
  print("Total Amount:",total)
  print("Thanks for shopping")
  break

  

   
   
  


    






