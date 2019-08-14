"""Complete the countApplesAndOranges function in the editor below.
It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
Input Format

The first line contains two space-separated integers denoting the respective values of S and T. 
The second line contains two space-separated integers denoting the respective values of A and B. 
The third line contains two space-separated integers denoting the respective values of M and N. 
The fourth line contains M space-separated integers denoting the respective distances that each apple falls from point A. 
The fifth line contains N space-separated integers denoting the respective distances that each orange falls from point B.


Print two integers on two different lines:

The first integer: the number of apples that fall on Sam's house.
The second integer: the number of oranges that fall on Sam's house.

This is a HackerRank exercise, you can find it in the following link:

https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ta=0
    to=0
    i=0
    j=0
    while(i<len(apples)):
        apples[i]+=a
        if(apples[i]>=s and apples[i]<=t):
            ta+=1
        i+=1
    while (j<len(oranges)):
        oranges[j]+=b
        if(oranges[j]>=s and oranges[j]<=t):
            to+=1
        j+=1
    print(ta)
    print(to)

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
