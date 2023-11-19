mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(mylist[-1])

print(mylist[2:5])

print(mylist[:4])

print(mylist[2:])

print(mylist[-4:-1])

if ("apple" in mylist):
    print("Yes, apple is available")

mylist[1:3] = ["blackcurrant"]

mylist.append("Guava")

mylist.insert(1, "wood apple")

print(mylist)

mylist.remove("wood apple")

mylist.pop(2)

del mylist[0]

print(mylist)

for x in mylist:
    print(x)

print("\n")

for i in range(len(mylist)):
    print(i)


[print(x) for x in mylist]


newList = [x for x in mylist if "a" in x]

print(newList)

newList.sort(key=str.lower)

print(newList)

newList.sort(reverse = True)

print(newList)


numbers = [100, 40, 30, 55, 51, 200, 70]

def near50(n):
    return abs(n-50)

numbers.sort(key=near50)

print(numbers)

anotherNumbers = numbers.copy()

print("another numbers", anotherNumbers)


combinedList = newList + numbers


print("combined", combinedList)

newList.extend(numbers);

print("combined 2", newList)
