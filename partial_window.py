# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1


# here is brute-force approach for above solution 
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        max_profit=0
        start=0
        last=start+minutes
        change_first=start
        change_last=last
        n=len(customers)
        result=0
        while last<=n:
            total_result=0
            for i in range(n):
                if(grumpy[i]==0):
                    total_result+=customers[i]
                else:
                    if(i>=start and i<last):
                        total_result+=customers[i]
            if(total_result>max_profit):
                max_profit=total_result
                            
            start+=1
            last+=1
        return max_profit  
    
#here is best approach for this one  

class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        total = 0
        ans = 0
        
        # Calculate total satisfied customers when not grumpy
        for i in range(len(customers)):
            total += (1 - grumpy[i]) * customers[i]
        
        window_all = 0
        partial_window = 0
        
        for i in range(len(customers)):
            window_all += customers[i]
            partial_window += (1 - grumpy[i]) * customers[i]
            
            if i + 1 >= minutes:
                ans = max(ans, total - partial_window + window_all)
                left = i - minutes + 1
                window_all -= customers[left]
                partial_window -= (1 - grumpy[left]) * customers[left]
        
        return ans

# Test case
sol = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
result = sol.maxSatisfied(customers, grumpy, minutes)
print("Result:", result)  # Expected output: 16
