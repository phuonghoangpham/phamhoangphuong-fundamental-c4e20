# Given the following dictionary:
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
# Try to do the followings:
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.

inventory={
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = 'seashell', 'strange berry', 'lint'

if 'dagger' in inventory['backpack']:
    del inventory['backpack'][inventory['backpack'].index('dagger')]

inventory['gold'] +=50

print(inventory)