'''For any sequence of numbers that are input by the user, we have to calculate the average of the input sequence numbers.

For example:

Case1: If the user input the sequence 1,2,3,4,5,6,7,8,9.

                        then the output should be 5.

Case2: If the user input the sequence 11,22,33,44,55,66,77,88,99.

                        then the output should be 55.'''

n=int(input("Enter the number Elements you want to enter: "))
arr=[]
sum=0
for i in range (0,n):
   elem=int(input(f"Enter the number {i+1} : "))
   arr.append(elem)
   sum=sum+elem

avarage=sum/n
print(f"avarage of the given numbers is : {"%.2f" %avarage}")