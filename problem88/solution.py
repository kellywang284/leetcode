class Solution:
    def merge(self, nums1: list[int], m:
    int, nums2: list[int], n: int) -> None:
        # girl
        p1 = m - 1
        # boy
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            # if the tallest girl is taller than the tallest boy, set the tallest girl in the end of the line
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            # if the tallest boy is taller than the tallest gir. set the tallest boy in the end of the line
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1