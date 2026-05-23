#check and remove square brackets from the input string

inputstr = input()

if inputstr.startswith('[') and inputstr.endswith(']'):
    inputstr = inputstr[1:-1]

numbers = inputstr.split()

arr = []

for num in numbers:
    arr.append(int(num)) 

print("".join(map(str,arr)))