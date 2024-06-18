# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
# Example 2:

# Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# Output: 0


def maxprofit(difficulty,profit,worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    total_profit = 0
    max_profit = 0
    i = 0
    for ability in worker:
        while i < len(jobs) and ability >= jobs[i][0]:
            max_profit = max(max_profit, jobs[i][1])
            # print(max_profit)
            i += 1
        total_profit += max_profit
    
    return total_profit
 
            
    
    
   
   
# difficulty, profit, worker = [2,4,6,8,10] ,[10,20,30,40,50],[4,5,6,7]
difficulty =[68,35,52,47,86]
profit =[67,17,1,81,3]
worker =[92,10,85,84,82]

result=maxprofit(difficulty,profit,worker)
print(result)