# IEEE RAS Task 6 – Python Basics

**Task Title:** Cover the Inside! – Python Data Types, Structures, and Control Flow

**Semester / Event:** IEEE Student Branch RAS – Introductory Tasks (2023/2024)

**Deadline:** Saturday, February 3rd, 2024 at 23:59

**Full Name:** Islam Elsayed

**University:** Zagazig University

**Department:** Electrical Engineering / Electronics

## Task Objectives

- Understand Python data types (e.g., int, float, bool) and operators (arithmetic, comparison, logical).
- Explore data structures like lists, strings.
- Master control flow with conditional statements (if/else) and loops (for, while).

## Resources Used

- Mastering Python by Nour (Arabic crash course – watched till 02:23:00).
- All-time favorite Python course (English crash course).
- Udacity Python course (English – till lesson 4).
- W3Schools (for revision).

## Task Requirements & Solutions

Solved 9 problems using basic Python without advanced built-ins. All solutions in a single .py file.

1. **Sum from 1 to n:**  
   Prompt user for n, use for loop to sum 1 to n. Example: n=5 → Sum=15.

2. **Second Largest and Second Smallest in List:**  
   Manually find max/min, then iterate again for seconds. No sorted() or min/max used. Example: [4,1,7,9,3] → Second largest:7, Second smallest:3.

3. **Two Numbers Adding to Target:**  
   Nested for loops to find indices where nums[i] + nums[j] == target. Example: [1,4,5,6], target=5 → Indexes:0 1.

4. **Split Strings into Halves:**  
   For each word, split at len//2 into two lists. Example: ["apple","Maid"] → ['app', 'Ma'] and ['le', 'id'].

5. **Minimum Distance Between Same Numbers:**  
   Nested loops to find min |j-i| where nums[i]==nums[j]. Example: [2,5,3,4,5,2] → Minimum distance:3 (between 5s).

6. **Output and Explanation:**  
   z=200/100 → 2.0 (float division).  
   k=(1.1+2.2 != 3.3) → True (floating-point precision: 1.1+2.2=3.3000000000000003).  
   y=k and isinstance(z, int) → False (z is float).  
   Printed values and explained floating-point issues.

7. **Output and Explanation:**  
   round(6.5)-round(3.5)==3 → False (round(6.5)=6, round(3.5)=4 → 6-4=2). Explained banker's rounding (even/odd bias).

8. **Factorial Using While Loop:**  
   Prompt for num, use while to multiply down to 1. Example: 3 → 6.

9. **Break Loop on 'q' Input:**  
   Infinite while, input until 'q', print inputs otherwise. Exits with "Loop exited!".

## Project Structure

```
Task6/
├── README.md                        ← This documentation file
├── Task_6.pdf                       ← Original task requirements PDF
└── task_6.py                        ← Python file with all solutions
```

## Key Learnings

- Data Types: Division always yields float; isinstance() checks types.
- Operators: Floating-point precision affects equality checks.
- Data Structures: Lists for storage; string slicing for halves.
- Control Flow: For/while loops for iteration; nested loops for comparisons; break for exiting.
- Avoid built-ins for manual logic to build fundamentals.
- Rounding: Python uses banker's rounding for .5 cases.

## How to Run

1. Open `task_6.py` in a Python interpreter (e.g., Python 3.x).
2. Run the file; each problem executes sequentially (some prompt inputs).
3. For problems with hardcoded inputs (e.g., lists), outputs print directly.

## Evaluation Notes

- Problems 1 to 9: 6/6 (All solved correctly without built-ins).
- Explanation Video: 4/4 (Covers code logic and explanations).

*Submitted for IEEE SB RAS – February 2024*  
*Prepared by: Islam Elsayed*