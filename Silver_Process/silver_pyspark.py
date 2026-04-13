from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, month

# -----------------------------------
# 1. CREATE SPARK SESSION
# -----------------------------------
spark = SparkSession.builder \
    .appName("Silver Layer Final") \
    .getOrCreate()

# -----------------------------------
# 2. PATHS
# -----------------------------------
bronze_path = "data_lake/bronze/traffic_crashes"
silver_path = "data_lake/silver/traffic_crashes"

print("Reading data...")

# -----------------------------------
# 3. READ JSON FILES
# -----------------------------------
df = spark.read \
    .option("multiline", "true") \
    .option("recursiveFileLookup", "true") \
    .json(bronze_path)

print("Data loaded")

# -----------------------------------
# 4. DEBUG (SEE COLUMNS)
# -----------------------------------
print("Columns in dataset:")
print(df.columns)

# -----------------------------------
# 5. DATA CLEANING
# -----------------------------------

# Use correct column name
df = df.dropna(subset=["crash_record_id", "crash_date"])

# Remove duplicates
df = df.dropDuplicates(["crash_record_id"])

# Convert date
df = df.withColumn("crash_date", to_timestamp(col("crash_date")))

# Add year & month
df = df.withColumn("year", year(col("crash_date"))) \
       .withColumn("month", month(col("crash_date")))

# -----------------------------------
# 6. WRITE TO SILVER LAYER
# -----------------------------------
df.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet(silver_path)

print("✅ Silver layer created successfully!")

# -----------------------------------
# 7. STOP SPARK
# -----------------------------------
spark.stop()