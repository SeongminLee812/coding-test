string = input()

result = ''
diff = ord('Z') - ord('A') + 1

for s in string:
    if ord(s) - 3 < ord('A'):
        result += chr(ord(s) - 3 + diff)
    else:
        result += chr(ord(s) - 3)

print(result)