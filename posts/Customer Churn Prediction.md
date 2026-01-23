# 📊 Customer Churn Prediction: An End-to-End Machine Learning Case Study

## 📌 Introduction
Customer churn is one of the most critical problems faced by subscription-based businesses, especially in the telecom industry. Acquiring new customers is significantly more expensive than retaining existing ones, making churn prediction a high-impact machine learning use case.

In this project, I built an **end-to-end machine learning pipeline** to predict whether a telecom customer is likely to churn based on demographic details, service usage, contract type, and billing information.

This project focuses not just on modeling, but on **structured thinking, business understanding, and clean data practices**.

---

## 🎯 Problem Statement
The goal of this project is to predict customer churn using historical customer data.

**Churn Definition:**  
A customer is considered churned if they stop using the telecom company’s services.

**Machine Learning Task:**  
Binary classification  
- `1` → Customer churned  
- `0` → Customer did not churn  

---

## 📂 Dataset Overview
- **Rows:** 7,043 customers  
- **Columns:** 33 (reduced to relevant features after cleaning)
- **Target Variable:** `Churn Label`

The dataset includes:
- Customer demographics
- Service subscriptions
- Contract and payment details
- Billing and tenure information

---

## 🧭 Project Workflow

The project followed a structured, professional workflow:

1. Problem understanding and business context
2. Data loading and inspection
3. Column grouping and planning
4. Minimal data cleaning
5. Exploratory Data Analysis (EDA)
6. Feature engineering
7. Encoding, scaling, and model building
8. Model evaluation and insights

Each step was documented with markdown explanations to ensure clarity and reproducibility.

---

## 🧹 Data Cleaning Strategy

### Minimal Cleaning Before EDA
Only essential cleaning steps were applied initially to avoid distorting insights:

- Dropped identifier, geographic, and leakage-prone columns
- Converted `Total Charges` from text to numeric
- Identified missing values introduced during type conversion

### Categorical Standardization
Service-related columns contained system-generated labels such as:
- `"No internet service"`
- `"No phone service"`

These were standardized to `"No"` to ensure:
- Meaningful category representation
- Reduced dimensionality during encoding
- Cleaner EDA and modeling

---

## 📊 Exploratory Data Analysis (EDA)

EDA focused on answering **business-relevant questions**, not producing excessive plots.

### Key Insights:
- The dataset is **imbalanced**, with more non-churned customers
- **Tenure** shows a strong inverse relationship with churn
- Customers on **month-to-month contracts** churn significantly more
- Higher **monthly charges** are associated with increased churn risk

---

## 🧠 Feature Engineering

Feature engineering was driven by EDA insights and business logic:

### 1. Average Monthly Spend
```text
Avg Monthly Spend = Total Charges / Tenure Months
