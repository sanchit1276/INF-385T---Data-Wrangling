# Solution to Michael Finegan

print("There once was a man named Michael Finnegan,")
print("He had whiskers on his chinnegan,")
print("The wind came up and blew them in ag'in,")
print("Poor old Michael Finnegan (begin ag'in)")


#########
# Using + (string concatenation)
#########

name = "James Howison"

print("There once was a man named " + name + ",")
print("He had whiskers on his chinnegan,")
print("The wind came up and blew them in ag'in,")
print("Poor old " + name + " (begin ag'in)")

########
# Using .format
########

print("There once was a man named {},".format(name))
print("He had whiskers on his chinnegan,")
print("The wind came up and blew them in ag'in,")
print("Poor old {} (begin ag'in)".format(name))

##########
# using .format and \n
#########

# define the lines using a {} placeholder
line1 = "There once was a man named {},"
line2 = "He had whiskers on his chinnegan,"
line3 = "The wind came up and blew them in ag'in,"
line4 = "Poor old {} (begin ag'in)"

# separate them with \n
full_poem = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

# Now replace the {} placeholders using .format
# name is there twice because we have 2 to replace
print(full_poem.format(name, name))

##########
# using .format and a multiline string (three quotes)
# multiline strings the newlines and indenting become
# part of the string
#########

full_poem = """
There once was a man named {},
He had whiskers on his chinnegan,
The wind came up and blew them in ag'in,
Poor old {} (begin ag'in)
"""

print(full_poem.format(name, name))

##########
# using input to define name
# note that it doesn't matter what printing technique you use.
#########

name = input("Name to customize with? ")

print("There once was a man named " + name + ",")
print("He had whiskers on his chinnegan,")
print("The wind came up and blew them in ag'in,")
print("Poor old " + name + " (begin ag'in)")
