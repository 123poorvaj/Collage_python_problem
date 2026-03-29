'''Array Rotation
Problem: Rotate an array to the right by k steps.

Solution: Rotate the array using slicing technique.
'''
a=[1,2,3,4,5]
k=5
k=k%len(a)
print( a[-k:]+a[:-k])