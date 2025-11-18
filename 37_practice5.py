# Replace for a list of words to be censored
words=["donkey","monkey","kaddu"]
with open("hello.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"$$$$")
with open ("hello.txt","w") as f:
    f.write(content)