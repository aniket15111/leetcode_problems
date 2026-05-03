class Solution:
    def trap(self, height: List[int]) -> int:        

        left=0
        right=len(height)-1
        ans=0
        leftmax=height[left]
        rightmax=height[right]
        while left<right:
            if height[left]<height[right]:
                if leftmax>height[left]:
                    ans+=leftmax-height[left]
                else:
                    leftmax=height[left]
                left+=1
            else:
 
                if rightmax>height[right]:
                    ans+=rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
                
        return ans  