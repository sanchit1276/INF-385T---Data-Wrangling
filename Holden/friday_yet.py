"""A short script to demonstrate branching."""
# No branching

destination = "home"

print("Done with work, I'm off {}".format(destination))

##############
# One branch
#############

day = "Friday"

# Is it Friday yet?
if (day == "Friday"):
    destination = "bar"
else:
    destination = "gym"

print("Done with work, I'm off {}".format(destination))

##########
# Two branches
##########

day = "Wednesday"

# Is it Friday yet?
if (day == "Friday"):
    destination = "bar"
else:
    if (day == "Wednesday"):
        destination = "Park"
    else:
        destination = "gym"

print("Done with work, I'm off {}".format(destination))

day = "Tuesday"

# Is it Friday yet?
if (day == "Friday"):
    destination = "bar"
else:
    if (day == "Wednesday"):
        destination = "Park"
    else:
        if (day == "Tuesday"):
        destination = "Sleep"
        else:
        destination = "gym"

print("Done with work, I'm off {}".format(destination))

##########
# Two branches, a little less indentation, using "elif"
##########

day = "Wednesday"

# Is it Friday yet?
if (day == "Friday"):
    destination = "bar"
elif (day == "Wednesday"):
    destination = "Park"
else:
    destination = "gym"

print("Done with work, I'm off {}".format(destination))
