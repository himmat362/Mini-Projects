email=input("Enter Email- ")
#stripping the email of any spaces
email=email.strip()
#counting number of @ and . in the username
z=email.count('@')
y=email.count('.')
if z!=1 and y!=1:
    print("Email Invalid")
else:
    print("Email Valid")