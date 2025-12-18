
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import sum

# Create Spark session
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
    ("North", "2024-01-01", 100),
    ("North", "2024-01-02", 200),
    ("North", "2024-01-03", 300),
    ("South", "2024-01-01", 50),
    ("South", "2024-01-02", 150)
]

# Define columns
columns = ["region", "date", "amount"]

# Create DataFrame
df = spark.createDataFrame(data, columns)
df.show()

# Group by region and sum amount
df.groupBy("region").sum("amount").show()

# Define window specification
window_spec = Window.partitionBy("region")

# Add a new column with region total using window function
df.withColumn(
    "region_total",
    sum("amount").over(window_spec)
