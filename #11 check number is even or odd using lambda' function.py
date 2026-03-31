num=int(input("Enter the number>>> "))

check=lambda num:"Even" if(num%2==0) else "Odd"
print(check(num))