''' Write a program to find out whether a student has passed or faild if it requires a total of 40% and at least 33% in each subject to pass. 
Assume 3 subjects and take marks as input frome the user '''

mark1 = int (input("Enter Mark 1:"))
mark2 = int (input("Enter Mark 2:"))
mark3 = int (input("Enter Mark 3:"))

# Check total Percentage
total_percentage = (100*(mark1 + mark2 + mark3))/300

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are Passed:",total_percentage)


else:
    print("You are Failed ,Try Best next time ! :",total_percentage)