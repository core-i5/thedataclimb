-- LeetCode 176: Second Highest Salary
-- Pattern: sql | Difficulty: Medium | Solved: 2026-10-26
-- Time: one sort / window pass | Took: 9 min | Peeked: no
-- Re-solve: +3d [ ]  +7d [ ]  +30d [ ]
-- Key insight (1 line): rank DISTINCT salaries, and return NULL (not zero rows) when no 2nd exists.
-- Gotchas: duplicate top salaries (100, 100, 90 -> 90), single-row table, empty table.
-- Dialect: PostgreSQL / MySQL 8+ / SQLite 3.25+

-- Approach A: DENSE_RANK — generalises to "Nth highest" by changing one number
SELECT MAX(salary) AS SecondHighestSalary          -- MAX over zero rows = NULL
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) ranked
WHERE rnk = 2;

-- Approach B: LIMIT/OFFSET inside a scalar subquery, so "no row" becomes NULL
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
