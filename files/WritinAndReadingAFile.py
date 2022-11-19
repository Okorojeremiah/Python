f = open("latest.txt", "w+")
f.write("Another thing")

f.seek(0)

print(f.read())
f.close()


