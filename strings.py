print("Hello")
print('Hello')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


b = "Hello, world!"
print(len(b))



for x in b:
    print(x)


txt = "Free life is better than rich life."
print("Free" in txt)

if ("Free" in txt):
    print("Free exist")

if ("free" not in txt):
    print("free does not exist")


print("slicing string...")

print(b[0:3])

print(b[:5])

print(b[2:])

print(b.upper())

print(b.lower())

print(b.strip())

print(b.replace("H", "J"))

print(b.split(", "))


