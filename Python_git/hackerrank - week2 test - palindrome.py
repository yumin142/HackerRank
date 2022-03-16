import math

                  
WORKS BUT TIMEOUT
def palindromeIndex(s):
    # Write your code here
    
    def ispalindrome(s1):
        half = int(len(s1)/2)
        if s1[0:half] == s1[-1:-half-1:-1]:
            return True
        else:
            return False            
                
    if ispalindrome(s) == True:
        return -1
    else:
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if ispalindrome(temp) == True:
                return i
        return -1
        
            
            
FINAL FINAL FINAL
def palindromeIndex(s):
    # Write your code here
    c = 0
    ans = -1
    i = 0
    j = len(s)-1
    for _ in range(len(s)):
        if s[i] == s[j]:
            i += 1
            j -= 1
            if i >= j:
                return ans
        elif s[i] != s[j] and c == 0:
            c += 1
            ans = i
            ans2 = j
            i += 1
        elif s[i] != s[j] and c == 1:
            c += 1
            i = ans
            j = ans2 - 1
            ans = ans2
        else: 
            return ans