# animals = ["cat", 'dog', 'canary']
# pet = animals
# pet.append('pig')
# animals.append("crow")
# print(animals)
# print(pet)
# pet2 = animals[:]
# pet2.append("bull")
# print(pet2)
# animals2 = ["cow", "monkey"]
# animals.extend(animals2)
# print(animals.index("dog"))
# animals.insert(5, "snake")
# print(animals)
# pets3 = "sheep", "sds"
# print(pets3)
# pets3 = animals.pop(0)
# print(pets3)
# print(animals)
# animals.remove("pig")
# print(animals)
# print(sorted(animals))

# print(list(reversed(animals)))
# animals.sort()
# print(animals)
# animals.reverse()
# print(animals)
"""Create a list a which contains the first three odd positive integers and a list b which contains the first three even positive integers.
Create a new list c which combines the numbers from both lists(order is unimportant).
Create a new list d which is a sorted copy of c, leaving c unchanged.
Reverse d in-place.
Set the fourth element of c to 42.
Append 10 to the end of d.
Append 7, 8 and 9 to the end of c.
Print the first three elements of c.
Print the last element of d without using its length.
Print the length of d."""

# a = [1, 2, 3]
# b = [-1, -2, -3]
# c = a + b

# d = sorted(c)
# print(d)
# d.reverse()

# c.insert(4, 42)
# print(c)
# d.append(10)
# print(d)
# c.extend([7, 8, 9])
# print(c)
# print(c[:3])
# print(d[-1])
# print(len(d))
"""Create a tuple a which contains the first four positive integers and a tuple b which contains the next four positive integers.
    Create a tuple c which combines all the numbers from a and b in any order.
    Create a tuple d which is a sorted copy of c.
    Print the third element of d.
    Print the last three elements of d without using its length.
    Print the length of d. """
# A = [1, 2, 3, 4]
# B = [5, 6, 7, 8]
# C = A + B
# D = sorted(C)
# print(D[:3])
# print(D[-3:])
# print(len(D))
# a = list(range(0, 20))
# b = range(3, 13)
# c = list(range(2, 50, 3))
# print(c)
# print(a)
# print(b)
# d = range(2, 5)
# print(d)
# print(range(2, 7))
# x = "blablabla"
# y = ["bla", "bla", 'bla']
# print(x.count("b"))
# print(y.count("bla"))
# directory = {"Jane Doe": +275555367, 'John Smith': +
#              275556254, 'Bob Stone': +275555689}
# print(directory)
# directory["Jane Doe"] = +275551024
# print(directory)
# print(directory.get('Bob Stone'))
# print(directory)
# print(directory.keys())
# print(directory.values())
# directory.update({"Adi": 764078644})
# print(directory)
# print(directory["Bob Stone"])
# print(directory.items())
# directory_set = set(directory.items())
# print(directory_set)
'''Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.
Convert a to a list b. Print its length.
Convert b to a set c. Print its length.
Convert c to a list d. Print its length.
Create a range which starts at 1 and ends at 10. Convert it to a list e.
Create the directory dict from the previous example. Create a list t which contains all the key-value pairs from the dictionary as tuples.
Create a list v of all the values in the dictionary.
Create a list k of all the keys in he dictionary.
Create a string s which contains the word "antidisestablishmentarianism". Use the sorted function on it. What is the output type? Concatenate the letters in the output to a string s2.
Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.'''
# lista = [1, 1, 2, 3, 3]
# a = tuple(lista)
# print(a)
# b = list(a)
# print(len(b))
# c = set(b)
# print(len(c))
# d = list(c)
# print(len(d))
# e = list(range(1, 10))
# directory = {"Jane Doe": +275555367, 'John Smith': +
#              275556254, 'Bob Stone': +275555689}

# t = tuple(directory.items())
# print(t)
# v = list(directory.keys())
# print(v)
# k = list(directory.values())
# s = 'antidisestablishmentarianism'
# s2 = " ".join(s)
# print(s2)
# w = "the quick brown fox jumped over the lazy dog".split()
# print(w)
a = [
    (1,),
    (2, 2),
    (3, 3, 3),
]

print(a[1][1])

b = [
    list(range(10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
]

print(b[0][1:-1])
