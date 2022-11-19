import re

arp = "22.22.22.1   0     b4:a9:a5:ff:c8:45  VLAN#222       L"

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w)*", arp)

# bap = "Okorojeremiah91@gmail.com"
#
# b = re.search(r"(.+)", bap)
# print(b.group(1))

# using findAll method

a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)

# To replace an element with a search element

a = re.sub(r"\d", "7", arp)
print(a)
