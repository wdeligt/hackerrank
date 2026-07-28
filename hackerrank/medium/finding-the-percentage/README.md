# Nested Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The provided code stub will read in a dictionary containing key/value pairs of name:\[marks\] for a list of students.  Print the average of the marks array for the student name provided, showing 2 places after the decimal.  

**Example**  
$\text{marks key:value pairs are}$  
$\text{'alpha': [20, 30, 40]}$  
$\text{'beta': [30, 50, 70]}$  
$\text{query_name = 'beta'}$  

The **query_name** is 'beta'.  beta's average score is $(30+50+70)/3 = 50.0$.

**Input Format**

The first line contains the integer $n$, the number of students' records. The next $n$ lines contain the names and marks obtained by a student, each value separated by a space. The final line contains **query_name**, the name of a student to query.

**Constraints**

+ $2 \le n \le 10$  
+ $0 \le marks[i] \le 100$  
+ $\text{length of marks arrays} = 3$  

**Output Format**

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T15:58:09.316Z  

```py
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    nums = set([record[1] for record in records])
    ordered_nums = sorted(nums)
    second_lowest_grade = ordered_nums[1]
    names = sorted([record[0] for record in records if record[1] == second_lowest_grade])
    for name in names:
        print(name)
    
    

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/finding-the-percentage/problem)