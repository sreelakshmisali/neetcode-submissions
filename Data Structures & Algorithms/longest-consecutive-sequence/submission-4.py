class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0

        for num in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            max_len = max(max_len, length)

        return max_len
        