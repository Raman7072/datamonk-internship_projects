import polars as pl
from deltalake.writer import write_deltalake


delta_path = "/tmp/delta_weather_daily"

df = pl.read_csv("hourly_weather.csv")


df = (
    df
    .with_columns(
        pl.col("time").str.strptime(pl.Datetime, "%Y-%m-%d %H:%M")
                      .alias("timestamp")
    )
    .with_columns(
        pl.col("timestamp").dt.date().alias("day")
    )
)

print("Hourly schema:")
print(df.schema)
print(df.head())


df_daily = (
    df
    .group_by(["location_name", "day"])
    .agg([
        pl.col("temperature").mean().round(2).alias("avg_temp"),
        pl.col("humidity").mean().round(2).alias("avg_humidity"),
        pl.len().alias("hourly_count")  # ✅ fixed
    ])
    .with_columns(
        pl.col("day").cast(pl.Date)     # ✅ CRITICAL
    )
)

print("\nDaily aggregated data:")
print(df_daily.head())



write_deltalake(
    delta_path,
    df_daily,
    mode="overwrite"   # safe for first run
)

print("\nDelta table written (version 0)")


df_new = pl.DataFrame({
    "location_name": ["Mumbai"],
    "day": ["2025-05-18"],          # string initially
    "avg_temp": [33.1],
    "avg_humidity": [70.2],
    "hourly_count": [24]
}).with_columns(
    pl.col("day").str.strptime(pl.Date, "%Y-%m-%d")  # ✅ force Date
)

write_deltalake(
    delta_path,
    df_new,
    mode="append"
)

print("Appended new data (version 1)")

# Step 5: Time Travel
print("\nLatest version (v1):")
print(pl.read_delta(delta_path))

print("\nPrevious version (v0):")
print(pl.read_delta(delta_path, version=0))

# Step 6: Metadata pruning example
print("\nMumbai only records:")
print(pl.read_delta(delta_path).filter(pl.col("location_name") == "Mumbai"))


# Latest data
pl.read_delta(delta_path)

# Original data
pl.read_delta(delta_path, version=0)



df_mumbai = (
    pl.read_delta(delta_path)
    .filter(pl.col("location_name") == "Mumbai")
)


df_global = (
    pl.read_delta(delta_path)
    .group_by("location_name")
    .agg([
        pl.col("avg_temp").mean().round(2).alias("global_avg_temp"),
        pl.col("avg_humidity").mean().round(2).alias("global_avg_humidity"),
        pl.len().alias("days_observed")
    ])
)

print("\nGlobal city-level summary:")
print(df_global)
