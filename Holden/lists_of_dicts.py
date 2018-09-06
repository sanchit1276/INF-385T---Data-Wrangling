# Think about a mySQL table, an excel table with column names or a typical csv.  
# We have columns with names and rows that have data in them
# This setup is called a "rectangular table" or often just a table.

# e.g., 

# Venues
# 
# id,name,capacity
# 1,AMD,700
# 8,Bud Light,2000


# In python we don't work directly with tables.  Rather, we represent
# tables as lists of dicts. Here's the same data:

# A list of dicts.

venues = [
           {'capacity': 700, 'id': 1, 'name': 'AMD'},
           {'id': 8, 'capacity': 2000,  'name': 'Bud Light'},
           {'capacity': 2300, 'id': 3, 'name': 'Austin Kiddie'},
           {'id': 4, 'capacity': 2000,  'name': 'Austin Ventures'} 
          ]

# This is the data structure that we'll get from mysql queries return in Python3.
# Notice that the column names become keys in the dict; they are repeated
# each time.  One thing you loose is the order of the columns (Remember that 
# dicts don't have original order) We'll revisit that later.

# Most of the time, you want to process each item in the list (the dict) together,
# without iterating over the row dict.  That way you can tie the elements in the dict
# together into something semantically relevant.

#print("Done output direct access")

for row in venues:
    # Now we can access the elements in the row dict directly.
   # print("The {} venue can hold {} people".format(row["name"],row["capacity"]))
#    print("The {name} venue can hold {capacity} people".format(row))
    
print("*" * 20)

for row in venues:
    if ( row["capacity"] > 800 ):
      # Now we can access the elements in the row dict directly.
      print("The {} venue can hold {} people".format(row["name"],row["capacity"]))


# print("Done output direct access")
# 
# # only print out venue with capacity greater than 800.
# # Sometimes, though, you also want to iterate through the items in each dict
# 
# print("Processing venues")
# 
# for row in venues:
#     # now we have the first item in the list (for AMD)
#     # that item is a dict, so to see the things inside
#     # we have to iterate through the dict items.  
#     # That's just like in the foreach screencast, except 
#     # that this time we're inside the for loop for venues.
#     # (Here we're using the for key,venue .items() form for iterating through dicts)
#     
#     for columnHeader, fieldValue in row.items():
#         print("{}: {}".format(columnHeader, fieldValue))
# 
# print("Done processing venues")
# 
# # If you want to control the order in which fields output then you
# # can declare the order of the fields manually. 
# 
# print("Processing venues with manual order")
# 
# # the column headers are identical in each dict, so you can get them from the first
# # item in the overall list
columnHeaders = [ "id", "capacity", "name" ]

for row in venues:
    # Now iterate through the headers (not the row dict)
    for header in columnHeaders:
        # Use the header to get the value from the row dict
        fieldValue = row[header] 
        print("{}: {}".format(header, fieldValue))
#         
# 
# print("Done processing venues with manual order")
# 
# 
# 
# # It is possible to get the column headers out of the dicts in the list
# # and then sort them and use that (so you don't have to manually declare
# # them). This seems nifty, but honestly it doesn't come up much, since 
# # you are almost always processing results that you want to do something
# # semantically useful with.
# 
# # the headers are the same in each dict, so you can just get them from the
# # first item in the list (venues[0]).  I always think I should be getting a list
# # of column headers with the call to .keys() but in python3 it's a slightly different
# # object (ie not a simple list, rather something of type dict_keys), 
# # so you can't call .sort(), you have to call sorted(). if you see the error
# # "dict_keys' object has no attribute 'sort'" that's what has happened.
# 
# columnHeaders = venues[0].keys()
# 
# # Now sort them in some way that you'd like:
# columnHeaders = sorted(columnHeaders)
# 
# print("Done processing venues with sorted order")
# 
# for row in venues:
#     # Now iterate through the headers (not the row dict)
#     for header in columnHeaders:
#         # Use the header to get the value from the row dict
#         fieldValue = row[header] 
#         print("{}: {}".format(header, fieldValue))
#         
# 
# print("Done processing venues with sorted order")

