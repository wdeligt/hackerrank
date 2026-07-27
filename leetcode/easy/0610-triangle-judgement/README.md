# Triangle Judgement

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Table: `Triangle`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

```

 

Report for every three line segments whether they can form a triangle.

Return the result table in  **any order**.

The result format is in the following example.

 

 **Example 1:** 

```
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

```

## Solution

**Language:** SQL  
**Runtime:** 361 ms (beats 12.50%)  
**Memory:** 0B (beats 100.00%)  
**Submitted:** 2026-07-27T12:33:40.127Z  

```sql
# Write your MySQL query statement below
SELECT x, y, z, 
    CASE
        WHEN z >= y AND z >= x AND z < x + y THEN 'Yes'
        WHEN z >= y AND z >= x AND z >= x + y THEN 'No'
        WHEN y >= z AND y >= x AND y < x + z THEN 'Yes'
        WHEN y >= z AND y >= x AND y >= x + z THEN 'No'
        WHEN x >= y AND x >= z AND x < y +z THEN 'Yes' 
        WHEN x >= y AND x >= z AND x >= y +z THEN 'No' 
    END AS triangle
    FROM Triangle;

```

---

[View on LeetCode](https://leetcode.com/problems/triangle-judgement/)