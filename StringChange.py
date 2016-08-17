a = raw_input()
str = ""

for i in range(len(a)):
    if a[i].islower():
        str += a[i].upper()
    else:
                        str += a[i].lower()
print str
