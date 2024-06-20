class Solution:
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        lo = 1
        hi = (position[-1] - position[0]) // (m - 1)
        ans = 1
        while lo <= hi:
            mid = (hi + lo) // 2
            print(mid)
            if self.canWePlace(position, mid, m):
                ans = mid
                lo = mid + 1
                print("in if")
                print(mid)
                print(hi)
            else:
                hi = mid - 1
                print("in else")
                print(mid)
        return ans

    def canWePlace(self, arr, dist, cows):
        """
        :type arr: List[int]
        :type dist: int
        :type cows: int
        :rtype: bool
        """
        cntCows = 1
        last = arr[0]
        for i in range(1, len(arr)):  # Start loop from 1 instead of 0
            if arr[i] - last >= dist:
                cntCows += 1
                last = arr[i]
            if cntCows >= cows:
                return True
        return False

# Example usage:
solution = Solution()
position = [5, 4, 3, 2, 1, 1000000000]
m = 2
result = solution.maxDistance(position, m)
print(result)  # Outputs the result