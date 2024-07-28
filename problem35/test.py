from problem35.solution import Solution

def test():
    app = Solution()

    nums1 = [1, 3, 5, 6]
    target1 = 5

    nums2 = [1, 3, 5, 6]
    target2 = 2

    nums3 = [1, 3, 5, 6]
    target3 = 7

    result1 = app.searchInsert(nums1, target1)
    print(result1)

    result2 = app.searchInsert(nums2, target2)
    print(result2)

    result3 = app.searchInsert(nums3, target3)
    print(result3)
