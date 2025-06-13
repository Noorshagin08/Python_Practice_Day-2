# If Statement
#Write a program to check the given number is Even

n=int(input("Enter a Number:"))
if (n % 2 == 0):
    print(n," is an Even Number")

 #If Else Statement
 # Write a Program to check vote Eligibility by enter his/her name and age
  
Name=input("Enter your Name:") 
Age=int(input("Enter your Age:")) 
if Age>=18:
    print(Name, "age is" , Age ," Eligible for vote") 
else:
    print(Name, "age is" , Age ," Not Eligible for vote")  

#Elif Statement
days=int(input("Enter The Days : ")) 
if (days == 0):
    print("No Fine") 
elif(days >= 1 and days <= 5):
    print("Fine Amount :",days*0.5) 
elif(days > 5 and days <= 10):
    print("Fine Amount :",days*1) 
elif(days >= 10 and days <=30):
    print("Fine Amount :",days*5) 
else:
    print("MemberShip Cancel") 

#Nested If Statement
m1=int(input("Enter M1:"))
m2=int(input("Enter M2:"))
m3=int(input("Enter M3:"))
total=m1+m2+m3
avg=total/3.0
print("Totl :",total)
print("Average :",avg)
if m1 >= 35 and m2 >= 35 and m3 >= 35 :
   print("Result: pass")

   if avg >= 90 and avg <= 100 :
     print("Grade : A")
   elif avg >= 80 and avg <= 89 :
     print("Grade : B")
   elif avg >= 70 and avg <= 79 :
     print("Grade : C")
   else:
     print("Grade : D")

else:
      print("Result: Fail") 
      print("Grade : No Grade") 
    
    