Eno = {
    "Utsav" : 29,
    "Ansh" : 7007,
    "Vansh" : 7004,
    22 : "Jeet"
}

print(Eno.items())
print(Eno.keys())
print(Eno.values())
Eno.update({"Ansh": 99, "Harsh": 99})
print(Eno)

print(Eno.get("Ansh2")) # Prints None
# print(Eno["Ansh2"]) # Return an Error
