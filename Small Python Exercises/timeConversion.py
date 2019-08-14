"""
Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in 12 hour format

This is a HackerRank exercise. You can find more information in the following link:

https://www.hackerrank.com/challenges/time-conversion/problem

"""
def timeConversion(s):
    res=list(s)
    res=res[:-2]
    num=int("".join(res[:2]))
    if(s[-2].upper()=="P" or num==12):
        if(num==12 and s[-2].upper()=="A"):
            num="00"
        else:
            if(num!=12):
                num+=12
        num=list(str(num))
        res[0]=num[0]
        res[1]=num[1]
    res="".join(res)
    return res

s = input("Insert a time: ")

result = timeConversion(s)

print(result)
