total=0
j=0


while True:
 n=int(input("Enter no of item:"))


 for i in range(n):
   item=input("Enter the amt of item {}:".format(j+1))
   j=j+1
   if item=="":
    item=0
    j=j-1
 
   total=total+float(item)
 print("Total:",total)
 
 x=input("do you want to continue?'yes':'no'")
 if x=="yes": 
  continue
 else:
  print("Total amt",total)
  print("No Of Product ",j)
  print("thanks for shopping")
  break



 

  

    

