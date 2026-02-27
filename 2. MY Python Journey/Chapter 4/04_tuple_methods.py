a = (1,3,4,566,7007,"Ansh","Kairav",566)
print(a)

no = a.count(566)
print(no)

i = a.index(7007)
print(i)

# Concatenation of tuple
b = (1,2,3,4,5)
c = (6,7,8,9,10)
d = b + c
print(d)

# repetatin of tuple 
my_tuple = (7,0,0,7)
repeated = my_tuple*3
print(repeated)

# elements are available in my tuple or not 
print(7 in my_tuple)
print(8 in my_tuple)

# length of tuple
print(len(my_tuple))

z = (1,2,3,4,5)
# sliced = z[1:4]
# print(sliced)
print(z[1:4])