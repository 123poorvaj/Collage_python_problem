#reverse a  number using while loop  or whit out any type casting  
n=int(input("Enter a number>>"))
a=n
rev=0
while(n>0):
    rimander=n%10
    rev=rev*10+rimander
    n=n//10

print(f"revers of {a} is :{rev}")

