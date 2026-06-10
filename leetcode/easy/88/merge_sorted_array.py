class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        marker_2 = n - 1
        marker_1 = m - 1

        for i in range(m + n - 1, -1, -1):
            if marker_2 < 0 or (marker_1 >= 0 and nums1[marker_1] >= nums2[marker_2]):
                nums1[i] = nums1[marker_1]
                marker_1 -= 1
            else:
                nums1[i] = nums2[marker_2]
                marker_2 -= 1

