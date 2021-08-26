string = input("Enter a string")
sub = input("Enter a substring")
if(string.find(sub) == -1):
    print("substring is not found in a given string")
else:
    print("substring is found in a given string")
