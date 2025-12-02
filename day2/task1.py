import re
f = open("input.txt")
data = []

RED = '\033[91m'   # Jasnoczerwony
END = '\033[0m'    # Resetowanie koloru

seq = r'^(\d+)\1$'

content = f.read().strip()
ranges = content.split(',')

sumOfInvalidIds = []

for range_str in ranges:
    splited = range_str.split('-')
    
    if len(splited) == 2:
        start = int(splited[0])
        end = int(splited[1])
        
        for i in range(start, end + 1):
            idStr = str(i)
            if re.fullmatch(seq, idStr) is not None:
                sumOfInvalidIds.append(i)

print("Niepoprawne ID:", sumOfInvalidIds)
print("Suma:", sum(sumOfInvalidIds))
f.close()