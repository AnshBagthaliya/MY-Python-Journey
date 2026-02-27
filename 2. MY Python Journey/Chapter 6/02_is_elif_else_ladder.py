a = int(input("Enter Your Age :"))

# If elif else ladder
if(a>18):
    print("You are able to vote")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entring 0 wich is not a valid age ")
    
else:
    print("You are not able to vote")

print("End of program")