class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for s in strs:
            if ''.join(sorted(s)) not in anagrams_map:
                anagrams_map[''.join(sorted(s))] = [s]
            else:
                anagrams_map[''.join(sorted(s))].append(s)
        
        solution_list = []
        for s in anagrams_map:
            solution_list.append(anagrams_map[s])
        
        return solution_list

            