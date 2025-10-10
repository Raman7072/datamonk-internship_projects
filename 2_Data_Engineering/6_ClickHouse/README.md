# ClickHouse Project — Data Engineering
Repository for DataMonk Internship Project

## Module 1: Data Compression
### Exercise 1 — Create Two Tables: With and Without Codecs

1. Create Table A (with codecs):

![](module1/exercise1/1.png)
---

2. Create Table B (without codecs):

![](module1/exercise1/2.png)
---

3. Insert 1 million rows:

![](module1/exercise1/3.png)
![](module1/exercise1/4.png)
---

4. Check sizes:

![](module1/exercise1/5.png)
---

5. Check row counts:

![](module1/exercise1/6.png)
---

### Exercise 2 — Guess the Best Codec
1. Create tables for testing codecs:

![](module1/exercise1/1.png)
---

2. Insert data:

![](module1/exercise1/1.png)
---

3. Compare disk usage:


---

## 🧱 Module 2: Columnar Storage
1. Load the same dataset (e.g., people.csv) into PostgreSQL and ClickHouse.


---

2. Run analytical query (e.g., average age per city):


---

## ⚡ Module 3: Why ClickHouse is Fast
### Exercise 3 — Test Isolated Inserts and Queries
- Terminal 1 (insert continuously using Python):


---

- Terminal 2 (run SELECT repeatedly):


---

### Exercise 4 — Experiment with ReplacingMergeTree
1. Create table:


---

2. Insert duplicates:


---

3. Check before merge:


---

4. Trigger merge:


---

5. Check after merge:


---

### Exercise 5 — Write a Vectorized Query
1. Insert data:


---

2. Run aggregation:


---
