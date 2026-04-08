class Solution:
    def minMaxDist(self, stations, k):
        low = 0
        high = stations[-1] - stations[0]
        
        while (high - low > 1e-7):
            mid = (low + high) / 2.0
            if self.isPossible(stations, mid, k):
                high = mid
            else:
                low = mid
                
        return high    
                
    def isPossible(self, stations, max_dist, k):
        cnt = 0
        for i in range(1, len(stations)):
            gap = stations[i] - stations[i-1]
            cnt += int(gap / max_dist)
            if gap % max_dist == 0:
                cnt -= 1
                
        return cnt <= k