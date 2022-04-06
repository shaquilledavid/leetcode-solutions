def solution(a,b):
      #add digits
    
    shorter = a if len(a) < len(b) else b
    longer = a if len(a) > len(b) else b
    

    total = ''
    i = 0
    difference = len(longer) - len(shorter)
    shorter = ('0' * difference) + shorter
    
    while i < len(shorter):
        total = total + str(int(shorter[i]) + int(longer[i]))
        i += 1
        
    
    return total


def solution2(queries):
    built = [False] * len(queries)
    print(built)

    output = []
    i = 0
    while i < len(queries):
        built[queries[i]-1] = True
        print(built)
        output.append(longestContiguous(built))
        i += 1

    return output



def longestContiguous(housesBuilt):
    #return longest number of contiguous houses in the lot
    longest = 0
    i = 0
    count = 0
    while i < len(housesBuilt):
        if housesBuilt[i] == True:
            count += 1
            if count > longest:
                longest = count
            i += 1
        else:
            i += 1
            count = 0

    return longest
        
    
queries = [2, 1, 3]
