# Space Separted Values  (String to Integers)

inputstr= input()
numbers = inputstr.split()

#converting string into integers

arr = []                                                                    #append - to add elements one by one
for num in numbers:
    arr.append(int(num)) #convert a number or string to integer

print(" ".join(map(str,arr)))     #join all strings using "" (space)
