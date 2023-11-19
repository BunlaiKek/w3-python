myTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

anotherTuple = tuple(("KOI", "Betta", "Gipple"))

notTuple = ("apple")

print(myTuple)

print(len(myTuple))

print("type", type(notTuple))

print("another tuple", type(anotherTuple))

if "apple" in myTuple:
    print("Yes, apple is in the fruit TUPLE")

listedTuple = list(anotherTuple)

# To add or remove item in tuple, we must convert the tuple to list first


listedTuple.append("Guava")

listedTuple.remove("Betta")

newTuple = tuple(listedTuple)

partialTuple = ("WaterMelon",)


newTuple += partialTuple


(KOI, Betta, Gipple) = anotherTuple

print("Koi", KOI)

print(newTuple)