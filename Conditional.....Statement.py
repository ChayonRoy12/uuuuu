
age=int(input("enter your age"))
print("your age:" ,age)

if(age>=18):
    
    print("you can vote")
    if(age>=18 and age<=30):
       print("youth")

    elif(age>30 and age<60):
       print("middle aged")  
    
    else:
       print("senior citizen")


elif (age<18 and age>0):
    print("you can't vote")

else:
   print("please type a valid age")