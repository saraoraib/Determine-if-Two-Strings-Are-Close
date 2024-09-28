from collections import Counter

class Solution:
    def closeStrings(self, word1, word2):
        # If the two words don't have the same unique characters, return False
        if set(word1) != set(word2):
            return False
        
        # Count the frequency of each character in both words
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Compare the sorted lists of frequencies
        return sorted(count1.values()) == sorted(count2.values())