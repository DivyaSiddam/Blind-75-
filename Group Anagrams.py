# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/651b8ab0d4b2fac24039eb35
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as a key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        # Return grouped anagrams
        return list(anagram_map.values())
