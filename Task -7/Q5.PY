# New 21 Game leetcode 

n = int(input())
k = int(input())
maxPts = int(input())

def new21Game(n, k, maxPts):
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0.0] * (n + 1) #storing probs.
    dp[0] = 1.0  

    window_sum = 1.0 # ده هيخزن مجموع الاحتمالات عشان بعدين اقسمها علي ماكس
    result = 0.0

    for i in range(1, n + 1):
        dp[i] = window_sum / maxPts #sliding window 

        if i < k:
            window_sum += dp[i]  
        else:
            result += dp[i] 

        if i - maxPts >= 0:
            window_sum -= dp[i - maxPts]  

    return result


probability = new21Game(n, k, maxPts)
print(f"{probability:.5f}")
