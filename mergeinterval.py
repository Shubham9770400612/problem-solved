class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if(len(intervals)<=1):
            return intervals
        intervals.sort(key=lambda x:x[0])
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            current_element=intervals[i]
            top_element=stack[-1]
            if(top_element[1]>=current_element[0]):
                stack[-1][1]=max(top_element[1],current_element[1])
            else:
                stack.append(current_element)
        return stack
        
