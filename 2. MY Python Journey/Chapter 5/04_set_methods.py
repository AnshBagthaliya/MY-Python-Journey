a = {1,4,74,"Ansh"}

print(a , type(a))

a.add(707)
print(a , type(a))

s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

b = {1, 2}
b.update([3, 4], {5, 6})
print(b)  # {1, 2, 3, 4, 5, 6}

c = {1, 2, 3}
c.remove(2)
print(c)  # {1, 3}

e = {1, 2, 3}
e.discard(4) # Removes a specific element. No error if not found
print(e)  # Output: {1, 2, 3}

f = {1, 2, 3}
x = f.pop()
print(x)  # Output: Random element like 1
print(f)  # Output: Remaining set

g = {1, 2, 3}
g.clear() # Removes all elements from the set
print(g)  # Output: set()

y = {1, 2}
t = {2, 3}
print(y.union(t))  # Output: {1, 2, 3} # Returns a new set with all elements from both sets.

o = {1, 2, 3}
p = {2, 3, 4}
print(o.intersection(p))  # Output: {2, 3} # Returns common elements.


