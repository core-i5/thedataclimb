"""M01 — Python standard-library toolkit for coding interviews.

Reference snippets you should be able to write from memory in a plain editor.
Run `python stdlib_toolkit.py` — every assert must pass.
"""

import bisect
import heapq
from collections import Counter, defaultdict, deque
from functools import cache


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Counter.most_common is O(n log n); heapq.nlargest is O(n log k)."""
    counts = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, counts.items(), key=lambda kv: kv[1])]


def k_smallest(nums: list[int], k: int) -> list[int]:
    """Min-heap: heapify is O(n), each pop O(log n)."""
    heap = nums[:]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(min(k, len(heap)))]


def running_max_heap(nums: list[int]) -> list[int]:
    """Python only has a MIN-heap -> push negatives to get a max-heap."""
    heap: list[int] = []
    out = []
    for x in nums:
        heapq.heappush(heap, -x)
        out.append(-heap[0])
    return out


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Monotonic deque of indices, values decreasing -> O(n)."""
    dq: deque[int] = deque()
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


def count_in_range(sorted_nums: list[int], lo: int, hi: int) -> int:
    """bisect_left / bisect_right on a sorted list: O(log n)."""
    return bisect.bisect_right(sorted_nums, hi) - bisect.bisect_left(sorted_nums, lo)


@cache
def climb(n: int) -> int:
    """@cache turns top-down recursion into memoised DP."""
    return n if n <= 2 else climb(n - 1) + climb(n - 2)


def bfs_shortest(edges: list[tuple[str, str]], start: str, goal: str) -> int:
    """defaultdict(list) adjacency + deque BFS. Iterative = no recursion-limit surprises."""
    graph: defaultdict[str, list[str]] = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    q, seen = deque([(start, 0)]), {start}
    while q:
        node, dist = q.popleft()
        if node == goal:
            return dist
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, dist + 1))
    return -1


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert k_smallest([5, 1, 4, 2], 2) == [1, 2]
    assert running_max_heap([3, 1, 5, 2]) == [3, 3, 5, 5]
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert count_in_range([1, 2, 2, 3, 5, 8], 2, 5) == 4
    assert climb(40) == 165580141
    assert bfs_shortest([("a", "b"), ("b", "c"), ("c", "d")], "a", "d") == 3
    print("all toolkit checks passed")
