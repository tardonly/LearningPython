a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
x = range(a,b + 1)
count = 0
for i in x:
    if (i % c == 0):
        count += 1
print count
