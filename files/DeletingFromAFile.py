f = open("files.txt", "r+")
f.truncate()

f = open("files.txt", "w+")
f.write("Something new is about to happen")

f.seek(0)
print(len(f.read()))

f.truncate(10)
f.close()

