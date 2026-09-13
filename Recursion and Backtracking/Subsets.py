# LeetCode 78: Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(ind,nums,ans,curr_sub):
            if(ind==len(nums)):
                ans.append(curr_sub.copy())
                return
            curr_sub.append(nums[ind])
            generate(ind+1,nums,ans,curr_sub)
            curr_sub.pop()
            generate(ind+1,nums,ans,curr_sub)

        ans,curr_sub=[],[]
        ind=0
        generate(ind,nums,ans,curr_sub)
        return ans
        
