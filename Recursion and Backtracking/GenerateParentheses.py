# Leetcode 22 : Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(curr_str,o,c,ans,n):
            if(o+c==2*n and o==c):
                ans.append(curr_str)
                return
            if(o>n):
                return
            if(c>o):
                return
            generate(curr_str+"(",o+1,c,ans,n)
            generate(curr_str+")",o,c+1,ans,n)
        ans=[]
        curr_str=""
        o=0
        c=0
        generate(curr_str,o,c,ans,n)
        return ans
    
