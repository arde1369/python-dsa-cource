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

def isPalindrome(left,right,s):
    while left >= 0 and right < len(s)-1 and s[left] == s[right]:
        left-=1
        right +=1
    return s[left+1:right]

def longestPalindrome(s):
    if len(s) == 0:
        return 0
    longest = ""
    for idx in range(len(s)-1):
        even = isPalindrome(idx,idx+1,s)
        odd = isPalindrome(idx,idx,s)
        if len(longest) < len(even):
            longest = even
        if len(longest) < len(odd):
            longest = odd
    return longest

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