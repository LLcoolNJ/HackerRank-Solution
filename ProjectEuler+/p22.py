names = []
for i in xrange(input()):
    names.append(raw_input().strip())
names = sorted(names)
for i in xrange(input()):
    out = 0
    s = raw_input().strip()
    for j in xrange(len(s)):
        if ord(s[j])-64 > 27:
            out += ord(s[j]) - 96
        else:
            out += ord(s[j]) - 64
    print s*(names.index(s)+1)
