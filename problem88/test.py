from problem88.solution import Solution
def test():
    app = Solution()

    numsa1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    numsb1 = [2, 5, 6]
    n1 = 3

    app.merge(numsa1, m1, numsb1, n1)
    print(numsa1)