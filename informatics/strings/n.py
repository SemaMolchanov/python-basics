s = input()
c = ''
for i in range (len(s)):
    if i % 3 != 0:
        c += s[i]
print(c)