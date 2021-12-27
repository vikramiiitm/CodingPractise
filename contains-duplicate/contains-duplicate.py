class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lis1 = set()
        for i in nums:
            if i not in lis1:
                lis1.add(i)
            else:
                return True
        