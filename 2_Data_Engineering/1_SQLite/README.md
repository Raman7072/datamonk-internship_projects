![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql0.png)

---
# Observantion

![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql1.png)

## Act 1: (people_small.csv ~1k rows)
- All queries under 0.05s
- Very smooth, no lag

![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql2.png)

---
## Act 2: (people_large.csv ~1M rows)
- Row count query still fast
- Filtering by age > 50 took noticeably longer
- Group by country + gender slower but still completed
- Some queries took several seconds

![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql3.png)

---
## Act 3: (Join people_large + jobs_large)
- Join query much slower (10s+)
- High memory usage
- Clear slowdown vs small dataset

![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql4.png)

---
## Conclusion:
SQLite is fine for lightweight queries but struggles with millions of rows + joins.
![](https://github.com/Raman7072/datamonk-internship_projects/blob/main/2_Data_Engineering/1_SQLite/screenshots/sql5.png)
