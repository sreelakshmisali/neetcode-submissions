class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else :
                freq[i]= freq[i] + 1

        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1]))
        result = list(sorted_dict.keys())[-k:]
        return result

        