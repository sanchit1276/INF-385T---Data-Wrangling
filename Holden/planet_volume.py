planets_and_volume = {"mercury": 0.0562,
                      "venus": 0.857,
                      "earth": 1,
                      "mars": 0.151,
                      "jupiter": 1321,
                      "saturn": 764,
                      "uranus": 63.1,
                      "neptune": 57.7,
                      "pluto": 0.0066
                      }
                      
# Iterate over the dictionary.

for planet in planets_and_volume:
  print("Planet {} has volume {}".format(planet, 
                                         planets_and_volume[planet]
                                        )
        )

# add all keys to the justKeys by iterating over the dictionary
justKeys = [] #

for planet in planets_and_volume:
  justKeys.append(planet)

print(justKeys)

# sort justKeys in alphabetical order.
alphaKeys = sorted(justKeys)

# output in alpha order
for planet in alphaKeys:
  print("Planet {} has volume {}".format(planet, 
                                         planets_and_volume[planet]
                                        )
        )