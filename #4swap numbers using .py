'''whrite a program to swap 2 numbers '''
'''with the help of temp'''
'''with the help of arithmetic opearter'''
'''with using bit'''
'''any another aproch excluding'''

a=int(input("enter the first number>> "))
b=int(input("enter the second number>> "))
print(f"Before swaping: a={a} and b={b}")
#using #3rd variable
'''temp=a
a=b
b=temp'''
# using arithmentic operaters
'''a=a+b
b=a-b
a=a-b'''

#using bit operater
# 
a=a^b
b=a^b
a=a^b

#another aproch
'''a,b=b,a'''




print(f"After Swaping: a={a} and b={b}")







