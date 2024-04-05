import re
txt="the rain in india"
x=re.search("^the.*india$",txt)
if x:
    print("yes,we have a match!")
else:
    print("no match")
