# List Comprehensions

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given $n$ scores. Store them in a list and find the score of the runner-up. 




**Input Format**

The first line contains $n$. The second line contains an array $A[$ $]$ of $n$ integers each separated by a space.  



**Constraints**

+ $2 \le n \le 10$  
+ $-100 \le A[i] \le 100$



**Output Format**

Print the runner-up score.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T15:04:14.602Z  

```py
if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    n = int(input())
    
    out = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != n]
    print(out)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)