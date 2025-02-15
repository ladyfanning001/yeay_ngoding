from collections import Counter
#jumlah karakter sama dan karakternya sama
#ex t : anagram  s : nagaram = true

#bisa pake hashmap or array

class Solution :
    def isAnagram(self, s: str, t: str) -> bool : #using hashmap
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]]= countS.get(s[i], 0) + 1
            countT[s[i]]= countT.get(s[i], 0) + 1
            
        for c in countS :
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
    def isAnagram2(self, s: str, t: str) -> bool : #using counter
        return Counter(s) == Counter(t)
    
    def isAnagram3(self, s: str, t: str) -> bool : #using soted (dont need extra memory but not that efficient)
        return sorted(s) == sorted(t)
    