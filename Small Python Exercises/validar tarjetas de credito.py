"""You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics: 

► It must start with a 4, 5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of digits (0-9). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.

Input Format

The first line of input contains an integer N. 
The next N lines contain credit card numbers."""
"""
This is a HackerRank exercise. You can find it in the following link:

https://www.hackerrank.com/challenges/validating-credit-card-number/problem

"""
num=int(input("How many credit card numbers are you going to enter?\n"))
ll=[]
print("Enter the credit cards numbers:\n")
for o in range (num):
    ll.append(input(""))
for v in range(len(ll)):
    gi=0
    r=0
    try:
        n=list(ll[v])
        z=len(n)
        if("-" in n):
            z=len(n)-3
        if(z!=16 or " " in n):
            print("Invalid")
        else:
            if(n[0]=="4" or n[0]=="5" or n[0]=="6"):
                if("-" in n):
                    r="".join(n)
                    while("-" in n):
                        q,w,x,y=r.split("-")
                        n.remove("-")
                        gi+=1
                    if(gi!=3 or len(w)!=4 or len(x)!=4 or len(y)!=4 or len(q)!=4):
                        print("Invalid")
                    else:
                        n=int("".join(n))
                        z=list(str(n))
                        if(str(n).isalnum()==False):
                            print("Invalid")
                        else:
                            for i in range (len(z)):
                                if (i+1<len(z) and z[i]==z[i+1] and i+4<len(z)):
                                    if(z[i]==z[i+1]):
                                        if(z[i]==z[i+2]):
                                            if(z[i]==z[i+3]):
                                                raise ValueError
                            print("Valid")
                else:
                    n=int("".join(n))
                    z=list(str(n))
                    if(str(n).isalnum()==False):
                        print("Invalid")
                    for j in range (len(z)):
                        if (j+1<len(z) and z[j]==z[j+1] and j+4<len(z)):
                            if(z[j]==z[j+1]):
                                if(z[j]==z[j+2]):
                                    if(z[j]==z[j+3]):
                                        raise ValueError
                    print("Valid")
            else:
                print("Invalid")
    except ValueError:
        print("Invalid")
