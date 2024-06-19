class Solution(object):
    def bloomed(self,bloomDay,m,k):
        n=len(bloomDay)
        if(m*k>n):
            return -1
        def checkbloom(bloomDay,m,k,day):
            total_bloom=0
            tatal_booke=0
            for bloom in bloomDay:
                if(day>=bloom):
                    total_bloom+=1
                    if(total_bloom==k):
                        tatal_booke+=1
                        total_bloom=0
                else:
                    total_bloom=0
            if(tatal_booke>=m):
                return True     
            return False
        
        low,high=0,max(bloomDay)
        while low<high:
            mid=(low+high)//2
            if(checkbloom(bloomDay,m,k,mid)):
                high=mid-1
            else:
                low=mid
        return low


object=Solution()

bloomDay = [1,10,3,10,2]
m=3
k=1
result=object.bloomed(bloomDay,m,k)
print("final answer",result)


# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, , , , ]   // we can only make one bouquet.
# After day 2: [x, , , _, x]   // we can only make two bouquets.
# After day 3: [x, , x, , x]   // we can make 3 bouquets. The answer is 3.
# Example 2:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
# Example 3:

# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.


























