"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
"""

from typing import List
import logging

logging.basicConfig(level=logging.INFO)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        logging.debug(nums)
        nums[:] = [ *nums[-k:], *nums[:-k] ]
        logging.debug(nums)


sol = Solution()

test_inputs = [
    {
        "nums": [1,2,3,4,5,6,7],
        "k": 3,
        "rotated": [5,6,7,1,2,3,4],
    },
    {
        "nums": [-1,-100,3,99],
        "k": 2,
        "rotated": [3,99,-1,-100],
    },
]

for test_input in test_inputs:
    eval_nums = test_input["nums"].copy()
    logging.info(eval_nums)
    sol.rotate(eval_nums, test_input["k"])
    logging.info(eval_nums)
    expected = test_input["rotated"].copy()
    assert eval_nums == expected, "something awry"