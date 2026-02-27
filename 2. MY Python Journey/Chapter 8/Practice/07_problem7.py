a = ['Ansh','Vansh','Utsav','ab']

def rem(a,word):
    for item in a:
        a.remove(word)
        return a

print(rem(a,'ab'))