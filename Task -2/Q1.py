n = int(input()) 
scores = list(map(int, input().split()))  
max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

Secondmax = max(scores)
print(Secondmax)


