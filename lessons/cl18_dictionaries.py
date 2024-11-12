"""EXAMPLES OF DICTIONARY SYNTAX WITH ICE CREAM SHOP ORDER TALLIES"""

# LIST OF ICE CREAM FAVLORS, WITH TALLIES (KEY: VALUE,)
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 4}

# Len evaluates to the num of entries
print(len(ice_cream))  # prints 3

# Add key-value entry by directly assigning a key
ice_cream["mint"] = 3

# Access entries by their key
print(ice_cream["chocolate"])  # prints 12

# Test if "pbj" is a key in ice_cream
las_pbj: bool = "pbj" in ice_cream
# Will evaluate to true of false, can add if when loop to do things if true or false

# Remove, we use pop method and give it a key
ice_cream.pop("strawberry")

# To iterate over every key in a loop, use FOR IN
for flavor in ice_cream:
    tally: int = ice_cream[flavor]  # will add up the # of flavors (like the tallies)
    print(f"{flavor} has {tally} orders")
