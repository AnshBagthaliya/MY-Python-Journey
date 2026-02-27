p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

massage = input("Enter Your Massage :")

if((p1 in massage) or (p2 in massage) or (p3 in massage)):
    print("This massage is a spam")

else:
    print("This massage is not a spam")