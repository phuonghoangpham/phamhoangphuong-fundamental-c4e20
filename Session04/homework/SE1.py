name=input("Your full name: ")

newname=name.lower().title()

import re
str = newname
newname=re.sub(" +", " ", str)

print(newname)







