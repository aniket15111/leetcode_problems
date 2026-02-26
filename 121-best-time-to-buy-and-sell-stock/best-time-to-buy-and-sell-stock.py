class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy=prices[0]
        mp=0
        for i in range(len(prices)):
            if best_buy<prices[i] :
                mp=max(mp,prices[i]-best_buy)
            best_buy=min(best_buy,prices[i])
                    
        return mp