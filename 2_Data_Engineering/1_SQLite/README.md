# Observantion

## Act 1: (people_small.csv ~1k rows)
- All queries under 0.05s
- Very smooth, no lag

## Act 2: (people_large.csv ~1M rows)
- Row count query still fast
- Filtering by age > 50 took noticeably longer
- Group by country + gender slower but still completed
- Some queries took several seconds

## Act 3: (Join people_large + jobs_large)
- Join query much slower (10s+)
- High memory usage
- Clear slowdown vs small dataset

## Conclusion:
SQLite is fine for lightweight queries but struggles with millions of rows + joins.
