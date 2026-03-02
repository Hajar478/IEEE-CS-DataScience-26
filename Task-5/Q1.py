n= int(input())
x= list(map(int, input().split()))
w= list(map(int, input().split()))

def weightedMean(x, w):

    xw_sum =0
    w_sum =0
    for i in range(len(x)):
        xw_sum += x[i] * w[i]
        w_sum += w[i]
    
    w_mean = xw_sum/w_sum
    print(f"{w_mean:.f1}")
     
weightedMean(x, w)