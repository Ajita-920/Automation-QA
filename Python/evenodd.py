#Even odd number

#num=int(input("Enter a number: "))
#if num%2==0:
   # print("The number is even.")
#else:
 #   print("The number is odd.")


marks=int(input("Enter your marks: "))
if marks>=90:
    if marks>=100:
        print("Invalid marks")
    else: 
        print("Distinction")
elif marks>=80:
    print("First Division")
elif marks>=50:
    print("Second Division")
elif marks>=40:
    print("Third Division") 
else:
    print("Fail")