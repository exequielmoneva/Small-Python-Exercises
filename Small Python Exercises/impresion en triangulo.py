#Calculate and print the number (without using strings) in order to create a triangle until N-1
for i in range(1,int(input("Insert the size of the triangle: "))):
    print((10**(i)//9)*i)#This is a way to get the number without the str()
    
"""
Explanation for (10**(i)//9)*i:
example for number 2:
10**2 = 100
100/22 = 11,11111111111111
but 100//22 = 11
and 11*2 = 22

"""
