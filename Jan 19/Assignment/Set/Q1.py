'''
1. Write a Python program to create a set and demonstrate 7 methods that can be
    done with set datastructure.
'''

anime={"SAO","KIMI NO NAWA","GOLDEN TIME"}
anime.add("DBZ")
print(anime)

x=anime.copy()
print(anime)

y={"DBZ","NORAGAMI","NARUTO"}

f=x.union(y)
print(f)

z=x.intersection(y)
print(z)

y.pop()
print(z)

anime.clear()

print(anime)


anime.update(x)
print(anime)

