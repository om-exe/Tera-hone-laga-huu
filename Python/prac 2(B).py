import re
txt="python is widely used language"
x=re.search("\s",txt)
print("the first white-space character is located in position:",x.start())

