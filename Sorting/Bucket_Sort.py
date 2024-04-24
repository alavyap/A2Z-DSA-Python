# Bucket Sort is used when we have to count the frequency of the elements.


def bucket_sort(l):
    
    bucket = [[] for _ in range(len(l))]  # Initialize empty buckets

    
    # First adding the elements in the bucket 
    # for i in range (len(l)):
    #     bucket.append(i)
        
        
    # Placing the elements at the 
    for j in l :
        index = int(10 *j)
        bucket[index].append(j)
        
    for k in range (len(l)):
        bucket[k] = sorted(bucket[k])
        
        
    a = 0 
    
    for b in range (len(l)):
        for c in range (len(bucket[b])):
            l[a] = bucket[b][c]
            a += 1 
    return l


# Test Run 
l1 = [0.42, 0.32 ,0.23, 0.52,0.25,0.47,0.51]
res = bucket_sort(l1)
print (res)