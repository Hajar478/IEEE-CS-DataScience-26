def sampleStats(count):
    total = sum(count)
    
    minimum = -1
    maximum = -1
    mode = 0
    max_count = 0
    total_sum = 0
    
   
    for i in range(256):
        if count[i] > 0:
            if minimum == -1:
                minimum = i
            maximum = i
            
            total_sum += i * count[i]
            
            if count[i] > max_count:
                max_count = count[i]
                mode = i
    
    mean = total_sum / total
    
    cumulative = 0
    
    if total % 2 == 1:  
        mid = total // 2 + 1
        for i in range(256):
            cumulative += count[i]
            if cumulative >= mid:
                median = float(i)
                break
    else:  
        mid1 = total // 2
        mid2 = total // 2 + 1
        
        median1 = None
        median2 = None
        
        for i in range(256):
            cumulative += count[i]
            
            if cumulative >= mid1 and median1 is None:
                median1 = i
            
            if cumulative >= mid2:
                median2 = i
                break
        
        median = (median1 + median2) / 2
    
    return [float(minimum), float(maximum), mean, median, float(mode)]

count = list(map(int, input().split()))
result = sampleStats(count)
print(result)


