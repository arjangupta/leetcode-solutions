# leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Solved date: 2023-08-23

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        all_1s_lists = []
        curr_1s_list = []
        for i in range(len(nums)):
            e = nums[i]
            if e == 0 or i == (len(nums) - 1):
                if e == 1:
                    curr_1s_list.append(e)
                all_1s_lists.append(curr_1s_list)
                curr_1s_list = []
            else:
                curr_1s_list.append(e)
        # print(all_1s_lists)
        if len(all_1s_lists) == 1:
            if len(all_1s_lists[0]) > 0:
                return len(all_1s_lists[0]) - 1
            else:
                return 0
        elif len(all_1s_lists) == 0:
            return 0
        else:
            max_total = 0
            for i in range(len(all_1s_lists)-1):
                curr_total = len(all_1s_lists[i]) + len(all_1s_lists[i+1])
                if curr_total > max_total:
                    max_total = curr_total
            return max_total
