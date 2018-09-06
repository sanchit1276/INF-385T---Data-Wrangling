"""first_while_loop.py Demonstrates a while loop.

In addition to branching with if, we can repeat parts of the code
multiple times, called a "loop".  Later this will be important for
processing lines of csv input files (where we want to do the same thing
over and over, once for each line

For now, though, we'll just do things a certain number of times.

This code celebrates with "hip, hip, hurray" but you can customize it
for greater anticipation (e.g., "hip, hip, hip, hip, hurray") by changing
todo.  The test on line 13 (todo > done) is repeated after each line 15.
"""
todo = 2
done = 0

while(todo > done):
    print("hip")
    done = done + 1

print("hurray")

# Q: why does this only print "hip" twice and not three times?
# Q: why does hurray only print once, regardless of what you number
# you set todo to?
