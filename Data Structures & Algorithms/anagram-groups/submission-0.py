class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  store how many characters are there in  amap
        # then you group same freq into one array

        sort = {}

        for words in strs:
            key  = ''.join(sorted(words))

            if key not in sort:
                sort[key] = []
            
            sort[key].append(words)
        
        return list(sort.values())
