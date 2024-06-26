def max_draws(t, test_cases):
    results = []
    for case in test_cases:
        p1, p2, p3 = case
        S = p1 + p2 + p3
        
        # Basic checks
        if S % 2 != 0 or p3 > p1 + p2:
            results.append(-1)
            continue
        
        max_possible_draws = min(p1, p2, (p1 + p2 + p3) // 3)
        results.append(max_possible_draws)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
test_cases = [tuple(map(int, data[3*i+1:3*i+4])) for i in range(t)]

# Calculate and print the results
results = max_draws(t, test_cases)
for res in results:
    print(res)
