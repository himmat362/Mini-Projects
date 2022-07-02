#sorting list consisting of numbers and letters
L = ["Ram", 1, "Shyam", 2, "Aman", 3]
L_str=[]
L_int=[]
L_final=[]
for r in L:
    #if element is a string append to string list
    if isinstance(r,str):
        L_str.append(r)
    #else append to  integer list
    else:
        L_int.append(r)
#sorting the string list
L_str=sorted(L_str)
#sorting the integer list
L_int=sorted(L_int)
print(L_str)
print(L_int)
#appending the lists together
L_final=L_str+L_int
print(L_final)