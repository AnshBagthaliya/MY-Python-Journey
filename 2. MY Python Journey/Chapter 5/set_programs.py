# Initial sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {1, 2}

print("Original set1:", set1)
print("Original set2:", set2)

# 1. add()
set1.add(6)
print("After add(6):", set1)

# 2. update()
set1.update([7, 8])
print("After update([7, 8]):", set1)

# 3. remove()
set1.remove(8)
print("After remove(8):", set1)

# 4. discard()
set1.discard(10)  # No error if not present
print("After discard(10):", set1)

# 5. pop()
popped = set1.pop()
print(f"After pop(): {popped} removed, set1 now:", set1)

# 6. clear()
temp_set = set1.copy()
temp_set.clear()
print("After clear():", temp_set)

# 7. union()
print("Union of set1 and set2:", set1.union(set2))

# 8. intersection()
print("Intersection of set1 and set2:", set1.intersection(set2))

# 9. difference()
print("Difference of set1 - set2:", set1.difference(set2))

# 10. symmetric_difference()
print("Symmetric difference of set1 and set2:", set1.symmetric_difference(set2))

# 11. issubset()
print("Is set3 subset of set1?:", set3.issubset(set1))

# 12. issuperset()
print("Is set1 superset of set3?:", set1.issuperset(set3))

# 13. isdisjoint()
print("Is set1 disjoint with {100, 200}?:", set1.isdisjoint({100, 200}))
