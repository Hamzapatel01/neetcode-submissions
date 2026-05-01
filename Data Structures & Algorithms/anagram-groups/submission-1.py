class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a hashmap and then insert all the  

        sort = {}

        for word in strs:
            key = ''.join(sorted(word)) #key that will store all the sorted words
            if key not in sort:
                sort[key] = []
            sort[key].append(word)

        return list(sort.values())