#Take Input using string

n = int(input())
arr = list(map(int,input().split()))
                                                #split - splits the string using spaces
                                                #map - applies function to all elements 
for num in arr:
    print(num, end=" ")

