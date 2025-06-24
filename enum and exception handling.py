# s={1,2,3,4}
# for i in (s):
#     print(i)

#Enumeration

# l=["a","b","c"]
# for i,value in enumerate(l):
#     print(i,value)

#to print list in tuple with (index and value)
# l=["apple","mango","banana"]
# e=enumerate(l)
# for i in range(len(l)):
#     print(e.__next__())

#exeption handling
#sys.exc_info() defines what is the error

# import sys
# try:
#     c=a+b
# except:
#     print("unexpected error",sys.exc_info())    


try:
    c=a+b[c]
except NameError as e:
    print("name error",)
    print(e)   
    
except IndexError as e:
    print("index error {}",format(e)) 

else:
    print("all good")

finally:
    print("whatever the case is,i will work")   
 