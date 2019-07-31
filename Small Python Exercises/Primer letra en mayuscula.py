def solve(s):
    ss=list(s)
    if(ss[0].isalpha()==True):
         ss[0]=ss[0].capitalize()

    for i in range(len(ss)):
        if(ss[i]==" "):
            ss[i+1]=ss[i+1].upper()
    ss="".join(ss)
    return ss
if __name__ == '__main__':


    s = input()

    result = solve(s)

    print(result)