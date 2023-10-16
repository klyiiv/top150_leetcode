class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = len(nums1) - m
        b = len(nums2) - n
        for i in range(a):
            nums1.remove(nums1[-1])
        for i in range(b):
            nums2.remove(nums2[-1])
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        # nums1 = nums2[:n]
        # nums1.sort()
