def findTheSubArrayAndDegree(arr):
    left= {}
    right={}
    count={}
    for i, x in enumerate(arr):
        if x not in left: 
            left[x] = i
        if x in right:
            if right[x]==left[x]:
                right[x] = i
        else:
            right[x] = i
        count[x] = count.get(x, 0) + 1
     
    length = len(arr)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            length = min(length, right[x] - left[x] + 1)   
    return length
    
arr = [5,1,2,2,3,1]
p = findTheSubArrayAndDegree(arr)
print(p)