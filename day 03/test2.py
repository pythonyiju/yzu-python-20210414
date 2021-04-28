x = True
y = False
Z = False
if not x or y:
    print(1)
elif not x or not y and Z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
    

