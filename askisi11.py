n1=eval(input("Enter first number: "))
n2=eval(input("Enter second number: "))
n3=eval(input("Enter third number: "))
n4=eval(input("Enter fourth number: "))
n5=eval(input("Enter fifth number: "))
n6=eval(input("Enter sixth number: "))
pinakas=[n1,n2,n3,n4,n5,n6]
print(pinakas)
firstlist=[1,3,4,5]
 if (n1==firstlist[0]) and (n2==firstlist[1]) and (n3==firstlist[2]) and (n4==firstlist[3]):
    print(n1,n2,n3,n4)
 elif  (n1==firstlist[0]) and (n2==firstlist[1]) and (n3==firstlist[2]) and (n5==firstlist[3]):
    print(n1,n2,n3,n5)
 elif  (n1==firstlist[0]) and (n2==firstlist[1]) and (n3==firstlist[2]) and (n6==firstlist[3]):
    print(n1,n2,n3,n6)
 elif  (n1==firstlist[0]) and (n3==firstlist[1]) and (n4==firstlist[2]) and (n5==firstlist[3]):
    print(n1,n3,n4,n5)
 elif  (n1==firstlist[0]) and (n3==firstlist[1]) and (n4==firstlist[2]) and (n6==firstlist[3]):
    print(n1,n3,n4,n6)
 elif  (n1==firstlist[0]) and (n3==firstlist[1]) and (n5==firstlist[2]) and (n6==firstlist[3]):
    print(n1,n3,n5,n6)
 elif  (n2==firstlist[0]) and (n3==firstlist[1]) and (n4==firstlist[2]) and (n5==firstlist[3]): 
    print(n2,n3,n4,n5)
 elif  (n2==firstlist[0]) and (n3==firstlist[1]) and (n4==firstlist[2]) and (n6==firstlist[3]): 
    print(n2,n3,n4,n6)
 elif  (n2==firstlist[0]) and (n3==firstlist[1]) and (n5==firstlist[2]) and (n6==firstlist[3]): 
    print(n2,n3,n5,n6)
 elif  (n3==firstlist[0]) and (n4==firstlist[1]) and (n5==firstlist[2]) and (n6==firstlist[3]): 
    print(n3,n4,n5,n6)
 else:
    print("There aren't any numbers") 
