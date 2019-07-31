def count_substring(string, sub_string):
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))
a=input("String: ")
b=input("Substring")
func=count_substring(a,b)

print("{} aparece {} veces en la cadena.".format(b,func))