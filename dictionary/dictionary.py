dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
dict2 = {1: "First element", 2: "Second element"}

print(dict2)
dict1["Vendor"] = "Microsoft"
dict1["RAM"] = "128"
print(dict1)
print(dict1.keys())
print(dict1.items())

# Converting dictionary keys into list

print(list(dict1.keys()))
print(list(dict1.items()))
print(list(dict1.values()))