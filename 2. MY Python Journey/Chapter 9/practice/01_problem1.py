f = open("poem.txt")
content = f.read()

if('Mohobbat' in content):
    print("The word Mohobbat is Present in thr content")

else:
    print("The word Mohobbat is not Present in the content")

f.close()