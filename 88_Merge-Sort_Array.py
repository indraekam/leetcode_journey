class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Inisialisasi pointer
        p1 = m - 1  # Pointer untuk elemen terakhir di nums1
        p2 = n - 1  # Pointer untuk elemen terakhir di nums2
        p = m + n - 1  # Pointer untuk posisi terakhir di nums1

        # Selama masih ada elemen di nums2
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
                
            # else :
                
        
            
        
