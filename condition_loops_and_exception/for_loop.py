vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for each_vendor in vendors:
    print(each_vendor)

my_String = "Cisco"

for letter in my_String:
    print(letter)
    print(letter * 2)

r = range(10)

for i in r:
    print(i * 2)

for elements in range(len(vendors)):
    print(vendors[elements])

# enumerate function helps us iterate through a sequence via the index and element

for index, elements in enumerate(vendors):
    print(index, elements)

for elements in vendors:
    print(elements)
else:
    print("The end of the list has been reached")