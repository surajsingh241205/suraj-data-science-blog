![cover](https://www.databricks.com/sites/default/files/2023-03/largest-open-source-apache-spark.png?v=1679038543) 

# Day 2 with Apache Spark on Databricks: From Architecture to Real Insights
When people say they’re “learning Spark,” most of the time they mean watching videos.
On Day 2, I decided to actually use Spark the way it’s meant to be used, clean DataFrames, lazy execution, and real insights.

### This post covers:
- Core Spark concepts (quickly, without fluff)
- Creating an in-memory Spark DataFrame (no CSVs)
- Performing real transformations
- Running Spark SQL correctly in Databricks
- Avoiding a very common notebook mistake

---

## Understanding Spark the Right Way
***Spark Architecture (In Simple Words)***
Spark works in a driver–executor model:

- **Driver**:
Your notebook’s brain. It builds the execution plan (DAG).
- **Executors**:
The workers. They actually process the data.
- **DAG (Directed Acyclic Graph)**:
Spark doesn’t execute line by line. It builds a plan first, then runs it efficiently.
***Nothing runs until you ask for a result.***

---

## Lazy Evaluation (Spark’s Superpower)
***In Spark:*** <br>
**select(), filter(), groupBy()** → nothing executes <br>
**show(), count(), write()** → execution happens

Spark waits, optimizes everything, then executes.
This is why Spark scales. And also why beginners get confused.

---

## DataFrames vs RDDs (2026 Reality Check)
- RDDs are low-level and manual
- DataFrames are optimized, readable, and production-ready
- If you’re using RDDs without a very specific reason, you’re doing it wrong.
- In this post, I use only DataFrames. One variable. One source of truth.

--- 
## Creating Dummy E-commerce Data (In-Memory)
Instead of reading CSVs, I created realistic e-commerce event data using NumPy and converted it directly into a Spark DataFrame.

![creating data using numpy](/static/images/code-1.PNG) 
### Why this approach?
- Faster iteration
- No file-system distractions
Perfect for learning, interviews, and prototyping

--- 
### Core DataFrame Operations
Selecting Relevant Columns
![Selecting the coulmns](/static/images/code-2.PNG)

This is how feature selection starts in real pipelines.

---
### Filtering High-Value Products
![Filtering](/static/images/code-3.PNG)

- This simple filter answers a business question:

How many interactions involve premium products?

---
### Grouping by Event Type
![Grouping](/static/images/code-4.PNG)

**Typical output shows:**

- Views dominate
- Purchases are much lower

That’s not a Spark issue, that’s e-commerce reality.

---
### Top Brands by Engagement
![Top brands](/static/images/code-5.PNG)

**This is the kind of aggregation used for:**

- Brand ranking
- Inventory prioritization
- Marketing decisions

---

### Revenue Insight (Actual Business Metric)
Counting events is fine.
Revenue is better.
![](/static/images/code-6.PNG)

*** Now Spark isn’t just processing data, it’s answering business questions.***

---

### Using Spark SQL (The Right Way in Databricks)

First, create a temporary view in a Python cell:

![](/static/images/code-7.PNG)

**Important Lesson I Learned**
You cannot mix Python and SQL in the same Databricks cell.

### %sql must be:
- The first line
- In its own cell

Most “Spark SQL errors” are actually notebook context errors.

---
### Key Takeaways from Day 2
- Spark is lazy by design—and that’s a good thing
- DataFrames are the default choice in modern Spark
- One clean DataFrame beats five confusing ones
- Spark SQL and PySpark work on the same execution engine
- Many errors come from notebook misuse, not Spark itself

---
### Final Thoughts

Day 2 wasn’t about learning more commands.
It was about learning how Spark thinks.

***Once you understand:***

- lazy evaluation
- DAGs
- clean DataFrame usage

Spark stops feeling magical and starts feeling predictable.

[Learn More](https://spark.apache.org/)



