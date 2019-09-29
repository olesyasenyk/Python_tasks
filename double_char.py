def double_char(s):
    s=list(s)
    for x in range(len(s)):
        s[x]=s[x]*2
    return ''.join(s)
    