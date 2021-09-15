import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            #정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


#sorted()함수는 list로 return > 딕셔너리의 key로 지정할수 없다는 것
#join()함수로 리스트를 벗긴다.