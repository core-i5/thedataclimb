# LeetCode 217: Contains Duplicate
# Pattern: arrays-hashing | Difficulty: Easy | Solved: 2026-10-26
# Time: O(n) | Space: O(n) | Took: 6 min | Peeked: no
# Re-solve: +3d [ ]  +7d [ ]  +30d [ ]
# Key insight (1 line): a set gives O(1) membership — return the moment you see a repeat.
#
# Approaches considered (say these out loud before coding):
#   1. Compare every pair          O(n^2) time, O(1) space
#   2. Sort, compare neighbours    O(n log n) time, O(1) extra if sorting in place
#   3. Hash set with early exit    O(n) time, O(n) space   <- chosen
# Edge cases tested: [], [x], all equal, negatives, duplicate at the very end.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([]) is False
    assert s.containsDuplicate([7]) is False
    assert s.containsDuplicate([-1, -1]) is True
    assert s.containsDuplicate(list(range(100_000)) + [99_999]) is True
    print("ok")
