"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"

Solution approach:
We treat every character in the string as a potential center of a palindrome. We expand outwards from this center to the left and right, checking if the characters match.

Since palindromes can have an odd length (e.g., in "aba", the center is "b") or an even length (e.g., in "abba", the center is the gap between "bb"), 
we must check both cases. For an odd length, l=r=i. For an even length, l=i and r=i+1.
"""
def isPalindrome(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left-=1
        right+=1
    return s[left+1:right]

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    for idx in range(len(s)-1):
        even = isPalindrome(s, idx,idx+1)
        odd = isPalindrome(s, idx, idx)
        if len(res) < len(even):
            res = even
        if len(res) < len(odd):
            res = odd
    return res
    

s = "cbbd"
expected = "bb"
print("test case 1:")
res = longestPalindrome(s)
print(f"Input: {s} | Expected: {expected} | Actual: {res} | Results: ", "Pass" if res == expected else "Fail" )

s = "babad"
expected = "bab"
print("test case 2:")
res = longestPalindrome(s)
print(f"Input: {s} | Expected: {expected} | Actual: {res} | Results: ", "Pass" if res == expected else "Fail" )