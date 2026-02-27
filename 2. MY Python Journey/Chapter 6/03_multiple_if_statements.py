a = int(input("Enter Your Age :"))

# If satatement 1
if(a%2 == 0):
    print("a is even")
# End of If statement 1

# If satatement 2
if(a>18):
    print("You are able to vote")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entring 0 wich is not a valid age ")
    
else:
    print("You are not able to vote")
# End of If statement 2

print("End of program")