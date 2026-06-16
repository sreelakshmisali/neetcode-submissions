class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # new_num = sorted(set(nums))
        # current_len = 1
        # max_len = 1
        # for i in range(len(new_num) - 1):
        #     if new_num[i]+1 == new_num[i+1]:
        #         current_len =current_len+1
        #     else:
        #         max_len=max(max_len,current_len)
        #         current_len=1

        # max_len = max(max_len, current_len)
        # return max_len
        max_len = 0

        for num in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            max_len = max(max_len, length)

        return max_len
        