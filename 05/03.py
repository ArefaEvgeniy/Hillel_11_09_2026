a = "  I nike like PyTHIon      "

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a)
print(a.strip())
print(a.strip("oI n"))
print(a.replace("Ion      ", "", 1))

b = a.strip()
print(b.split())
print(b.split("i"))
