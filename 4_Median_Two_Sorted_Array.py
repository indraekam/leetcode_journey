class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        idx_med = total // 2 + 1

        idx_nums1 = 0
        idx_nums2 = 0
        val = [0, 0]

        for i in range(idx_med):
            if idx_nums1 < len(nums1) and (idx_nums2 >= len(nums2) or nums1[idx_nums1] < nums2[idx_nums2]):
                val[0] = val[1]
                val[1] = nums1[idx_nums1]
                idx_nums1 += 1
            else:
                val[0] = val[1]
                val[1] = nums2[idx_nums2]
                idx_nums2 += 1

        if total % 2 == 1:
            return val[1]
        else:
            return (val[0] + val[1]) / 2
