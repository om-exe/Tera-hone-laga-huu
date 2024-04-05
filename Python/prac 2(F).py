import re
patterns="to"
text="i will go to mumbai to meet my friend to tell something"
for m in re.find all(pattern,text):
    print("found",m)
for m in re.find iter(pattern,text):
    s=m.start()
    e=m.end()
    print("found",m.re.pattern,s,"from",e)

