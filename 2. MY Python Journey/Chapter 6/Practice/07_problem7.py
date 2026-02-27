post = input("Enter the Post :")

if("Ansh".lower() in post.lower()): # this fnction is compare a post(string) in lowercase also
    print("This post is talking about Ansh")

else:
    print("This post is not talking about Ansh")

'''  Outputs:

Enter the Post :Ansh is good boy
This post is talking about Ansh

Enter the Post :ansh is good boy
This post is talking about Ansh

Enter the Post :anSH is good boy
This post is talking about Ansh

'''