year=int(input("Enter any one year:"))

if year % 4 == 0 and year % 100 !=0:
 print(year,"is a leap year")
elif year % 100 ==0:
 print(year,"is not a leap year")
elif year % 400 ==0:
 print(year,"is a leap year")
else:
 print(year,"is not a leap year")
n=int(input("Enter any one number:"))
f=1
for i in range(1,n+1):
 f=f*i
 print("Factorial of ",n,"is", f)