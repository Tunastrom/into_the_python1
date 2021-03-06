class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname='박'

print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))