mySet = {"apple", "banana", "cherry"}

anotherSet = set(("blueberry", "mulberry", "strawberry"))

anotherSet.add("orange")

mySet.update(anotherSet)


# you can update set with set, list, tuple, or dictionary


mySet.update(["lemon", "cucumber"])


mySet.discard("kakav")

#mySet.remove("kakav") # course error since kakav is not present

for x in mySet:
    print(x)


setForInteraction = {"lemon", "carrot"}


numberSet = {1, 2,3}

finalSet = mySet.union(numberSet)


mySet.intersection_update(setForInteraction)

print("final set", finalSet)


print("intersection set", mySet)