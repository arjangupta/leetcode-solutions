# https://leetcode.com/problems/product-of-array-except-self/
# Solved: 2023-09-01

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prepro = [] # pre-product array
        postpro = [] # post-product array
        # Current products
        prepro_curr = 1
        postpro_curr = 1
        for i in range(len(nums)):
            if i > 0:
                prepro_curr *= nums[i-1]
                postpro_curr *= nums[len(nums)-i]
            prepro.append(prepro_curr)
            postpro.append(postpro_curr)
        postpro.reverse()
        output = []
        for i in range(len(nums)):
            output.append(prepro[i]*postpro[i])
        return output