"""Creating and using strings, input, and variables."""
# We know how to print out strings:
print("Hello, Sanchit, welcome to Python.")

# But we can also store strings in a variable, so that we can use them later
welcomeMsg = "Hello, Sanchit, welcome to Python."

# A variable is a box with a name, we can get the contents of the box by using
# its name. This prints the same thing as line 2.
print(welcomeMsg)

# We can also join strings together, using a + character.
longerMsg = welcomeMsg + "I hope you enjoy yourself."

print(longerMsg)
# ==> Hello, James, welcome to Python.I hope you enjoy yourself

# Hmmm, that doesn't have a space between the sentences. Let's add a space.
# Now we're joining three strings together.
longerMsg = welcomeMsg + " " + "I hope you enjoy yourself."

print(longerMsg)
# ==> Hello, James, welcome to Python. I hope you enjoy yourself.

# You could also do this by adding a space at the start of the second string
longerMsg = welcomeMsg + " I hope you enjoy yourself."


# Q: Why is this all printing on a line single?
# A: Because the strings are joined together _before_ being passed to print
#    you get a newline after each print statement, one statement, one newline.

# So now we output variables, but what about taking some input?
yourName = input("What's your name, then? ")
# ==> What's your name, then? *waits for you to type*

# When you press enter whatever you typed is put into the yourName variable.
# now you can personalize the message:
print("Hello " + yourName + ", welcome to Python.")

yourDesigner = input("What designer are you wearing today? ")

print("That's a lovely outfit, " + yourDesigner + " is so fetch.")
