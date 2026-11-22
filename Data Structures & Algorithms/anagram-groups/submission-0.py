class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}

        for s in strs:
            freq = {}

            for char in s:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 0

            representation = tuple(sorted(freq.items()))

            if representation in dict:
                dict[representation].append(s)
            else:
                dict[representation] = [s]

        return list(dict.values())