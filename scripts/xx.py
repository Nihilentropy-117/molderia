with open("x") as x:
    lines = x.readlines()

authors = []
for line in lines:
    if line.startswith("-"):
        authors.append(line.replace("-",""))

for author in set(authors): print(author)