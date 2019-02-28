##### Week1: Problem 3
s = 'xeyihttx'
chk = ''

for i in range(len(s)):
    order = i
    com = s[order]
    while order < len(s)-1:
        if s[order] <= s[order + 1]:
            com += s[order + 1]
            order += 1
            if order == len(s)-1 and len(chk) < len(com):
                chk = com
        else:
            if len(chk) < len(com):
                chk = com
            break

print("Longest substring in alphabetical order is: "+chk)