# Lists and dicts are groups of variables.  Think of them like a pillbox broken up into
# slots for different days (or a filling cabinet with folders).
# You can put things into each slot.
# Each slot either has # numbered position (in a List) or a name (in a Dict).

courseList = ["Introductory Zoology", "Zoology Lab", "Penguin Studies"]

# We can access the parts of the list using this syntax:
print("My second course is " + courseList[1])  # ==> Zoology Lab

# Wait ... what now?  courseList[1] shows the 2nd item? Why is that not courseList[2]?
# The answer is because we start counting from 0, so courseList[0] is the 1st item.
# Why? It's about offsets in memory, see https://en.wikipedia.org/wiki/Zero-based_numbering
# But really it's just one of those things.  list[0] is the first item.
# The number is called the "index".

# courseList[0] = "GnuMath"
# print("My first course is " + courseList[0])
courseList.append("GnuMath")
print("My fourth course is " + courseList[3])
print(courseList)
#
# Dicts are the same as Lists except that instead of numbers as indexes they have words.
# They use curly braces instead of square ones. The word indexes are called "keys".
# Each key points to a "value".
#
courseDict = { "101c": "Intoductory Zoology",
	           "210c": "Zoology Lab",
	           "315p": "Penguin Studies" }

# The keys have to be unique, but the values don't have to be unique.
# Unlike Lists, Dicts don't have any order (you can't say that an item is 2nd in a Dict)
# even if it was defined 2nd in the list (the reason, if you are interested,
#  is because the key is stored as a hash: https://en.wikipedia.org/wiki/Hash_function)

print("One of my courses is " + courseDict["210c"])

row2 = {"day" : "Wednesday", "count" : 45}
row3 = {"day" : "Tuesday", "count" : 34}

sheet = [row2, row3]

print(sheet)

# Adding things works in a very similar way, but you have to provide a key (Python
# can't guess, as it can with adding items to a List

# courseDict["325m"] = "GnuMath"

# There are good examples for Lists and Dicts at:
# http://learnpythonthehardway.org/book/ex39.html
# (don't worry about the "Make your own Dictionary Module" part
