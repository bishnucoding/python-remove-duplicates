def remove_dups(input):
    map = {}
    for i in input:
        map[i] = True

    return map.keys()

input = [1,2,3,4,5,4,4,4,4,56,65,4,3,2,3,43,2,1,11,2,3334,4,5,43,2,2,2,3,4]    
result = remove_dups(input)

print(result)

#Time complexity: O(n): Because we are looping the input once. Insert time to map is constant.
#Space Complexity: O(n): we are using additional map. Which can take space upto n. 
