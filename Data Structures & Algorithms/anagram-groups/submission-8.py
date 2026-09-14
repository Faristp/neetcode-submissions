class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = dict()

        for word in strs:
            if "".join((sorted(word))) in hashmap:
                hashmap["".join(sorted(word))].append(word)
            else:
                hashmap["".join(sorted(word))] = [word]
        
        result = []
        for key in hashmap:
            result.append(hashmap[key])
        
        return result