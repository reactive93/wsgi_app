


# arr = [1, 3, 2]
# arr = [1, 3, 2, 1]
# arr = [1, 2, 3, 4]
arr = [40, 50, 60, 10, 20, 30]
count2 = 0
i=0
j=1
while i< len(arr)-1 and j<=len(arr)-1:
    if arr[i] <= arr[j]:
        i+=1
        j+=1
    else:
        j+=1
        count2+=1
    # if count2>=2:
    #     break

print(count2<=1)   
# print(count-count2)
# print(count)
# print(count2)