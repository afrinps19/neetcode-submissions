class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,n in enumerate(nums):
            needed=target-n
            if needed in map:
                return [map[needed],i]
            map[n]=i    