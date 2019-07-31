"""
You have a non-empty set , and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format

The first line contains integer N, the number of elements in the set . 
The second line contains N space separated elements of set S.
All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format

Print the sum of the elements of set S on a single line.

"""
"""
This is a HackerRank exercise. You can find it in the following link:

https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

"""

n = int(input())
s = set(map(int, input().split()))
num=int(input())
l=[]
for i in range (num):
    l.append(input())
for j in range(len(l)):
    le=l[j].split(" ")
    if(len(le)>1):
        eval("s.{}({})".format(le[0],le[1]))
    else:
        eval("s.{}()".format(le[0]))

print(sum(s))
