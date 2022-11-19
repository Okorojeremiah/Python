# String method
a = "Cisco Switch"
print(a.index("C"))
print(a.count("i"))
print(a.find("sco"))
print(a.lower())
print(a.upper())
print(a)
print(a.startswith("a"))
print(a.endswith("h"))

b = "  Cisco Switch  "
print(b.strip())

c = "$$Cisco Switch$$"
print(c.strip("$"))

print(b.replace(" ", ""))

d = "Cisco,Juniper,HP,Avaya,Nortel"
print(d.split(","))

print("_".join(a))

x = "Cisco"
y = "Cisco"
print((x * 3))

print("o" in x)
print("b" not in x)

print("Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4))
print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4))
print("Cisco model: {2}, {1} WAN slots, IOS {0}".format("2600XM", 2, 12.4))

# format using f-strings
model = "2600XM"
slots = 4
ios = 12.3

print(f"Cisco model: {model}, {slots} WAN slots, IOS {ios}")
print(f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}")

# Slicing strings

String1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(String1[5: 15])
print(String1[5: 14])
print(String1[5:])
print(String1[: 10])
print(String1[:])
print(String1[-1])
print(String1[-9: -1])
print(String1[-5:])
print(String1[: -5])
print(String1[::2])
print(String1[::1])
print(String1[::-1])

String = "08101558612"

print(String[1::2])
print(String[::2])
