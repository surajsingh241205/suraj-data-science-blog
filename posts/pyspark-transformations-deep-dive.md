![cover](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2A8Gvauu0TEOOhIVVA3Ah5vw.jpeg) 

# PySpark Transformations Deep Dive: From Pandas Thinking to Distributed Reality
When I started learning PySpark, I made a common mistake — I tried to apply Pandas style thinking while writing Spark code. The syntax looked familiar, the results appeared correct on small data, but conceptually I was missing the entire point of Spark.

PySpark is not about rows or immediate execution. It’s about defining transformations that Spark optimizes and executes lazily across a distributed system. This post captures my Day 3 learning, focused on PySpark transformations, window functions, and feature engineering using a synthetic e-commerce dataset.

---

## Why PySpark Is Fundamentally Different from Pandas
![Img](https://www.nitorinfotech.com/wp-content/uploads/2024/05/Pandas-vs-PySpark.jpg)
At a surface level, PySpark DataFrames look similar to Pandas DataFrames. Internally, they behave very differently.

Pandas works in memory on a single machine and executes code eagerly. PySpark works across a cluster and evaluates code lazily by building a logical execution plan (DAG). This difference forces a mindset shift instead of thinking row by row, you must think in terms of column transformations and data flow.

The biggest lesson here is that in PySpark, you don’t “run” computations immediately. You describe what you want, and Spark decides how to do it efficiently.

---

## Dataset Used: Synthetic E-commerce Events
![](https://storage.googleapis.com/kaggle-datasets-images/2265304/3799432/3c73cfe3d89a16abfe1cbe8344cfd139/dataset-cover.jpg?t=2022-06-14-08-39-08)

To keep the learning focused and reproducible, I generated a synthetic e-commerce dataset using NumPy and Pandas, and then converted it into a Spark DataFrame.

The dataset represents common user behavior such as product views, add-to-cart events, and purchases. Each row contains an event type, product name, brand, price, and user ID.

### **CODE (Dataset Generation):**

import numpy as np <br>
import pandas as pd <br><br>
np.random.seed(42) <br>
rows = 1000

pdf = pd.DataFrame({  <br>
"event_type": np.random.choice(["view", "add_to_cart", "purchase"], rows, p=[0.6, 0.25, 0.15]),<br>

"product_name": np.random.choice(["Laptop", "Phone", "Headphones", "Monitor", "Keyboard"], rows), <br>
"brand": np.random.choice(["Apple", "Samsung", "Dell", "HP", "Logitech"], rows), <br>
"price": np.random.randint(50, 2000, rows),<br>
"user_id": np.random.randint(1000, 5000, rows)})<br>

df = spark.createDataFrame(pdf) 
df.show(5)

---

### Top 5 Products by Revenue
In e-commerce analytics, revenue is generated only by purchase events. Views and cart additions may indicate intent, but they don’t generate revenue.

To calculate the top products by revenue, I filtered purchase events, grouped by product and brand, and summed the price.

### **CODE (Top Products by Revenue):**

from pyspark.sql import functions as F <br>

top__products = (
df
.filter(F.col("event_type") == "purchase")
    .groupBy("product_name", "brand") <br>
    .agg(F.sum("price").alias("total_revenue")) <br>
    .orderBy(F.desc("total_revenue")) <br>
    .limit(5) <br>
)

top_products.show(truncate=False)

This approach is efficient because it filters data early and avoids unnecessary transformations.

---

### Conversion Rate: View to Purchase
Conversion rate is one of the most important metrics in product and marketing analytics. It shows how effectively product views turn into purchases.

To calculate this, I grouped events by product and event type, pivoted the data, and computed the purchase-to-view ratio.

### **CODE (Conversion Rate):**

conversion_df = ( <br>
df <br>
    .groupBy("product_name", "event_type").count() <br>
    .groupBy("product_name") <br>
    .pivot("event_type", ["view", "purchase"]).sum("count").fillna(0) <br>
    .withColumn("conversion_rate_pct",F.when(F.col("view") > 0,(F.col("purchase") / F.col("view")) * 100).otherwise(0)) <br>

) <br>
conversion_df.show(truncate=False)

Handling null values and division safety is critical when working with real-world data.

---

### Window Functions: Ranking Users by Spending

Window functions allow calculations across related rows without collapsing the dataset. This makes them extremely powerful for analytics use cases.

Here, I ranked users based on their total purchase spend.

### **CODE (Window Function Example):**

from pyspark.sql.window import Window

user_spend = (
df
    .filter(F.col("event_type") == "purchase")<br>
    .groupBy("user_id")<br>
    .agg(F.sum("price").alias("total_spent"))<br>
)
<br>
rank_window = Window.orderBy(F.desc("total_spent"))
<br>
ranked_users = (
    user_spend <br>
    .withColumn("spend_rank", F.rank().over(rank_window))<br>
)
<br>
ranked_users.show(10)

This logic scales seamlessly from thousands of rows to billions.

---

## Derived Features for Analytics and Machine Learning

Feature engineering is where raw data becomes useful for analytics and machine learning models.

In this step, I created simple but effective derived features such as purchase flags and price buckets.

## **CODE (Derived Features):**

feature_df = (
df
.withColumn("is_purchase",F.when(F.col("event_type") == "purchase", 1).otherwise(0)) <br>
.withColumn("is_view",F.when(F.col("event_type") == "view", 1).otherwise(0))<br>
.withColumn("price_bucket",F.when(F.col("price") < 500, "low").when(F.col("price") < 1200, "medium").otherwise("high"))<br>
)

feature_df.show(5)

These features can be directly consumed by dashboards or ML pipelines.

---

### A Note on UDFs
![](https://play-lh.googleusercontent.com/V0AIRsCj7U3naDWJSpIDDsrMqzg2MIN7KrZ4Wcc6SHQYWJNkeeOVo1CMhwP1eZtEdxo)
Although PySpark supports user-defined functions, they should be avoided whenever possible. Built-in Spark SQL functions are faster, optimized, and easier to maintain.

**A simple rule to follow is:** if Spark SQL can do it, do not use a UDF.

---

### Key Takeaways
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHpMeDm9Xfqx74m8b_Aj29luxDButavwh59Q&s)

PySpark requires a different mindset than Pandas. Transformations should be declarative and column-based. Window functions enable powerful analytics without breaking scalability. Derived features bridge the gap between raw data and real business insights.

Spark rewards clarity and punishes inefficient thinking.

[Learn More](https://sparkbyexamples.com/pyspark/pyspark-window-functions/)


































