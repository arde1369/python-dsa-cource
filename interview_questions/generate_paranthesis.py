"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
def dfs(left,right,ans,s):
    if right < left:
        return
    if not left and not right:
        ans.append(s)
    if left:
        dfs(left-1,right,ans,s+"(")
    if right:
        dfs(left,right-1,ans,s+")")

def generateParenthesis(n):
    ans = []
    if n > 0:
        dfs(n,n,ans,"")
    return ans

print("Test Case 1:")
input = 3
output = generateParenthesis(input)
expected = ["((()))","(()())","(())()","()(())","()()()"]
print(f"Input: {input} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

print("Test Case 2:")
input = 1
output = generateParenthesis(input)
expected = ["()"]
print(f"Input: {input} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )