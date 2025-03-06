s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(f"{s1} {s2}")
print(s1, s2)
print(3 * (s1 + " "))
print(s1, len(s1))
print(3 * s2, len(3 * s2))
for c in s2:
    print(c)

new = ""
for c in s1:
    new += (4 * c)

for c in s2:
    print(4 * c, end="")

# in can be used to check if one string is in another
print("h" in s1)
print("d" in s2)
print(s1 in s1)

counter = 0
 for i in counter:
     if s1[counter] = s2[counter]:
         print("same")
     else:
         print(f"s"")

         s = "Hello"
         print(s)
         s2 = 'World'
         print(s2)
         s3 = ('And she said: "Hello!"')
         s4 = (""""Both single" and 'double'""")
         print("\"Both single\" and 'double'")
         print(s[2])
         print(s[-1])

         s = "abcdefghijklmnop"
         print(s)
         print(s[1:4], s[6:9])
         print(s[:4], s[6:])
         print(s[1:10:2])
         print(s[::-1])

         s = "cat"
         s = "r" + s[1:]
         print(s)

         s = "seven"
         s = s[:2] + "7" + s[3:]
         print(s)

         print(dir(str))
         print(help("hi".capitalize))
         print("hello".center(50, "*"))
         print("gmail.com".find("."))
         s = "I see a cat who likes to cat while I cat on a cat"
         # Find all occurrences
         position = 0
         while True:
             position = s.find("cat", position)
             if position == -1:
                 break
             print(f"Found cat in position {position}")
             position += 1

         s = "I SEE A LOT OF THINGS"
         print(s.lower())

         s = "I see a lot of things"
         print(s.title())

         s = "I see a cat"
         print(s.replace("cat", "dog"))

         s = "I like to go shopping"
         print(s.split())
