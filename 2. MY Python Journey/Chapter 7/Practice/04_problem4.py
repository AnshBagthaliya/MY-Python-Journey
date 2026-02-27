n  = int(input("Enter Number :"))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is Not Prime")
        break
else:
    print("Number is Prime")

# 👉 These numbers cannot be divided evenly by any other number except 1 and themselves.